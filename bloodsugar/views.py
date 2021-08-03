from django.shortcuts import render
from rest_framework import generics, permissions
from bloodsugar.serializers import BloodSugarSerializer
from bloodsugar.models import BloodSugar


class UserRecordCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BloodSugarSerializer


class UserRecordDetail(generics.RetrieveAPIView):
    serializer_class = BloodSugarSerializer
    lookup_field = "owner_id"

    def get_queryset(self):
        owner_id = self.kwargs["owner_id"]
        return BloodSugar.objects.filter(owner=owner_id)
