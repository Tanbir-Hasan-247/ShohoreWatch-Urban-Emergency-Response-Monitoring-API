from alerts import models
from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import ResponderProfile

User = get_user_model()

class AlertCategorySerializer(serializers.ModelSerializer):
    alert_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.AlertCategory
        fields = ['id', 'name', 'slug', 'alert_count', 'severity_default', 'response_time_default', 'icon', 'color_hex']
        
    # def get_alert_count(self, obj):
    #     alert = models.Alert.objects.select_related('category').filter(category=obj)
    #     return alert.count()
    
class AlertImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlertImage
        fields = ['id', 'image']

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone']
        
class AlertSerializer(serializers.ModelSerializer):
    category = AlertCategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=models.AlertCategory.objects.all(),
        source='category',
        write_only=True
    )

    images = AlertImageSerializer(many=True, read_only=True)

    reported_by = UserMiniSerializer(read_only=True)
    assigned_to = UserMiniSerializer(read_only=True)

    class Meta:
        model = models.Alert
        fields = [
            'id',
            'title',
            'description',
            'category',
            'category_id',
            'zone',
            'reported_by',
            'assigned_to',
            'severity',
            'status',
            'latitude',
            'longitude',
            'images',
            'is_verified',
            'created_at',
            'resolved_at'
        ]
        read_only_fields = [
            'reported_by',
            'assigned_to',
            'created_at',
            'resolved_at'
        ]

class VerifyAlertSerializer(serializers.ModelSerializer):
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(
            role=User.RESPONDER,
            responder_profile__availability_status=ResponderProfile.AVAILABLE
        ),
        source='assigned_to',
        write_only=True,
        required=False
    )
    class Meta:
        model = models.Alert
        fields = ['id', 'is_verified', 'assigned_to_id']

class UpdateAlertStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alert
        fields = ['status']