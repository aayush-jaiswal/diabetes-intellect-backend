from userdata.models import UserData
from userdata.serializers import UserDataSerializer
from rest_framework import generics, permissions
from .permissions import IsOwner


class UserDataCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserDataSerializer


class UserDataDetail(generics.RetrieveAPIView):
    permission_classes = [IsOwner]

    serializer_class = UserDataSerializer
    lookup_field = "owner_id"

    def get_queryset(self):
        owner_id = self.kwargs["owner_id"]
        return UserData.objects.filter(owner=owner_id)
