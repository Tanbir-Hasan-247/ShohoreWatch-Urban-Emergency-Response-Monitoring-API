from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from zones.models import Zone


class User(AbstractUser):
    ADMIN = "admin"
    OFFICIAL = "official"
    RESPONDER = "responder"
    CITIZEN = "citizen"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (OFFICIAL, "Official"),
        (RESPONDER, "Responder"),
        (CITIZEN, "Citizen"),
    ]

    username = None

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CITIZEN)

    zone = models.ForeignKey(
        Zone, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    profile_picture = models.ImageField(
        upload_to="users/profile_pictures/", null=True, blank=True
    )

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"


class CitizenProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="citizen_profile"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Citizen: {self.user.email}"


class OfficialProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="official_profile"
    )
    employee_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    office_address = models.TextField(blank=True, null=True)
    office_phone = models.CharField(max_length=20, blank=True, null=True)
    joining_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.designation} - {self.user.email}"


class ResponderProfile(models.Model):
    AVAILABLE = "available"
    BUSY = "busy"
    OFFLINE = "offline"

    STATUS_CHOICES = [
        (AVAILABLE, "Available"),
        (BUSY, "Busy"),
        (OFFLINE, "Offline"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="responder_profile"
    )
    badge_number = models.CharField(max_length=50, unique=True)
    organization = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)
    availability_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=AVAILABLE
    )

    def __str__(self):
        return f"{self.organization} - {self.user.email}"
