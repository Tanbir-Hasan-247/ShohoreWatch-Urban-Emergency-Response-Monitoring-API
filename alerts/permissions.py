from rest_framework import permissions
from alerts.models import Alert
from users.models import User

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user 
            and request.user.is_authenticated 
            and request.user.role == User.ADMIN
        )


class IsOfficerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.role == User.ADMIN:
            return True
        
        alert_id = view.kwargs.get('pk')
        if not alert_id:
            return False
        try:
            alert = Alert.objects.get(pk=alert_id)
        except Alert.DoesNotExist:
            return False

        return (
            request.user 
            and request.user.is_authenticated 
            and request.user.role == User.OFFICIAL
            and alert.is_verified == False
        )
        
class IsResponderOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.role == User.ADMIN:
            return True
        
        alert_id = view.kwargs.get('pk')
        if not alert_id:
            return False
        
        try:
            alert = Alert.objects.get(pk=alert_id)
        except Alert.DoesNotExist:
            return False

        return (
            request.user 
            and request.user.is_authenticated 
            and request.user.role == User.RESPONDER
            and alert.assigned_to == request.user
            and alert.status != Alert.RESOLVED
        )