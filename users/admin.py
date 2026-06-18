from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CitizenProfile, OfficialProfile, ResponderProfile

class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("email", "first_name", "last_name", "role", "zone", "phone", "is_staff")

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "role", "zone", "phone")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "first_name", "last_name", "phone", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(CitizenProfile)
admin.site.register(OfficialProfile)
admin.site.register(ResponderProfile)