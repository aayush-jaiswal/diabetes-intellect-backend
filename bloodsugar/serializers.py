from rest_framework import serializers
from .models import *


class BloodSugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodSugar
        fields = "__all__"
