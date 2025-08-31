from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class FullCustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_name", "user_type", "first_name", "last_name", "active_mode"]


class ListCustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_name"]
