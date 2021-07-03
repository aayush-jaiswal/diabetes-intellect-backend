from userdata.models import UserData
from userdata.serializers import UserDataSerializer
from rest_framework import generics


class UserDataList(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class UserDataDetail(generics.RetrieveAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
