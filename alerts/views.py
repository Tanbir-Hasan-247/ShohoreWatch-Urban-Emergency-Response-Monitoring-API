from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from alerts import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import ResponderProfile
from .permissions import IsAdminOrReadOnly, IsOfficerOrReadOnly, IsResponderOrReadOnly

# Create your views here.
class AlertCategoryViewSet(ModelViewSet):
    queryset = models.AlertCategory.objects.annotate(alert_count=Count('category_alerts'))
    serializer_class = serializers.AlertCategorySerializer


class AlertViewSet(ModelViewSet):
    queryset = models.Alert.objects.select_related(
        'category', 'zone', 'reported_by', 'assigned_to'
        ).prefetch_related('images')
    # serializer_class = serializers.AlertSerializer
    
    def get_permissions(self):
        if self.action == 'verify':
            return [IsOfficerOrReadOnly()]
        
        if self.action == 'update_status':
            return [IsResponderOrReadOnly()]

        return [IsAdminOrReadOnly()]

    def get_serializer_class(self):
        if self.action == 'update_status':
            return serializers.UpdateAlertStatusSerializer
        if self.action == 'verify':
            return serializers.VerifyAlertSerializer
        return serializers.AlertSerializer
    
    @action(detail=True, methods=['post'])
    def verify(self, request, pk=None):
        alert = self.get_object()

        serializer = serializers.VerifyAlertSerializer(
            alert,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        alert = serializer.save(is_verified=True)

        if alert.assigned_to:
            serializer.save(status=models.Alert.ACTIVE)
            responder = alert.assigned_to.responder_profile
            responder.availability_status = ResponderProfile.BUSY
            responder.save(update_fields=['availability_status'])

        return Response({
            "message": "Alert verified successfully",
            "alert_id": alert.id,
            "is_verified": alert.is_verified
        })  
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        alert = self.get_object()
        serializer = serializers.UpdateAlertStatusSerializer(alert, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Alert status updated successfully",
            "alert_id": alert.id,
            "new_status": alert.status
        })
    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)
        
        
class AlertImageViewSet(ModelViewSet):
    serializer_class = serializers.AlertImageSerializer
    
    def get_queryset(self):
        alert_id = self.kwargs.get('alert_pk')
        return models.AlertImage.objects.filter(alert_id=alert_id)
    
    def perform_create(self, serializer):
        alert_id = self.kwargs.get('alert_pk')
        alert = get_object_or_404(models.Alert, id=alert_id)
        serializer.save(alert=alert)