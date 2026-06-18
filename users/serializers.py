from djoser.serializers import UserCreateSerializer as UCS, UserSerializer as US

from users.models import CitizenProfile, OfficialProfile, ResponderProfile, User


class UserCreateSerializer(UCS):
    class Meta(UCS.Meta):
        fields = ("id", "username", "email", "password", "first_name", "last_name", "phone")
        
class UserSerializer(US):
    class Meta(US.Meta):
        fields = ("id", "email", "first_name", "last_name", "phone", "role", "zone")
        
    def update(self, instance, validated_data):
        old_role = instance.role
        new_role = validated_data.get("role", old_role)

        instance = super().update(instance, validated_data)

        if old_role != new_role:

            if new_role == User.CITIZEN:
                CitizenProfile.objects.get_or_create(user=instance)

            elif new_role == User.OFFICIAL:
                OfficialProfile.objects.get_or_create(user=instance, employee_id=f"OFF-{instance.id}")

            elif new_role == User.RESPONDER:
                ResponderProfile.objects.get_or_create(user=instance, badge_number=f"RES-{instance.id}")

        return instance
    
    # def create(self, validated_data):
    #     role = validated_data.get("role", User.CITIZEN)

    #     user = super().create(validated_data)

    #     if role == User.CITIZEN:
    #         CitizenProfile.objects.create(user=user)

    #     elif role == User.OFFICIAL:
    #         OfficialProfile.objects.create(
    #             user=user,
    #             employee_id=f"OFF-{user.id}"
    #         )

    #     elif role == User.RESPONDER:
    #         ResponderProfile.objects.create(
    #             user=user,
    #             badge_number=f"RES-{user.id}",
    #             organization="Not Assigned"
    #         )

    #     return user
    
    