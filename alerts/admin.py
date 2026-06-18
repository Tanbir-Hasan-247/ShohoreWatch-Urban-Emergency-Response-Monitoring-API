from django.contrib import admin
from .models import AlertCategory, Alert, AlertUpdate

# Register your models here.
admin.site.register(AlertCategory)
admin.site.register(Alert)
admin.site.register(AlertUpdate)
