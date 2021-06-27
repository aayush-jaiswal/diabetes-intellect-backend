from djoser.serializers import UserCreateSerializer, UserSerializer, UserDeleteSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

class UserDeleteSerializer(UserDeleteSerializer):
    class Meta:
        model = User