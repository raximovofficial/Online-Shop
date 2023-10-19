from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=123)
    username = serializers.CharField(max_length=123)
    password = serializers.CharField(max_length=123, min_length=6)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'username': {'read_only': True}
        }