from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для объектов User.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'registration_date')
