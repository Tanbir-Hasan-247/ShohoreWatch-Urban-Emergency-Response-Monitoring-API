from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User, CitizenProfile, OfficialProfile, ResponderProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if not created:
        return
    
    if instance.is_staff or instance.is_superuser:
        instance.role = User.ADMIN
        instance.save()

    if instance.role == User.CITIZEN:
        CitizenProfile.objects.create(user=instance)

    elif instance.role == User.OFFICIAL:
        OfficialProfile.objects.create(
            user=instance,
            employee_id=f"OFF-{instance.id}"
        )

    elif instance.role == User.RESPONDER:
        ResponderProfile.objects.create(
            user=instance,
            badge_number=f"RES-{instance.id}",
            organization="Not Assigned"
        )