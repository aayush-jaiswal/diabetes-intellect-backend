from datetime import date, timedelta
from rest_framework import serializers
from .models import *


class UserDataSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField("get_user_age")
    bmi = serializers.SerializerMethodField("get_bmi")

    def get_user_age(self, userdata):
        return (date.today() - userdata.date_of_birth) // timedelta(days=365.2425)

    def get_bmi(self, userdata):
        return userdata.weight / (userdata.height / 100) ** 2

    class Meta:
        model = UserData
        fields = "__all__"
