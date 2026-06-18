from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import ResponderProfile
from zones.models import Zone

# Create your models here.
User = get_user_model()

class AlertCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    severity_default = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    response_time_default = models.IntegerField(help_text="Response time in minutes")
    icon = models.CharField(max_length=100, blank=True)
    color_hex = models.CharField(max_length=7, blank=True, help_text="Hex color code, e.g. #FF0000")
    
    def __str__(self):
        return self.name
    
class Alert(models.Model):
    PENDING = 'pending'
    ACTIVE = 'active'
    ACKNOWLEDGED = 'acknowledged'
    RESPONDING = 'responding'
    RESOLVED = 'resolved'
    FALSE_ALARM = 'false alarm'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACTIVE, 'Active'),
        (ACKNOWLEDGED, 'Acknowledged'),
        (RESPONDING, 'Responding'),
        (RESOLVED, 'Resolved'),
        (FALSE_ALARM, 'False Alarm'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(AlertCategory, on_delete=models.PROTECT, related_name='category_alerts')
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_alerts')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_alerts')
    severity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # image = models.ImageField(upload_to='alerts/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
    

class AlertImage(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='alerts/images/')
    
    def __str__(self):
        return f"Image for Alert: {self.alert.title}"


class AlertUpdate(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name='updates')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)