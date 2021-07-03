from django.urls import path
from userdata import views

urlpatterns = [
    path("", views.UserDataList.as_view()),
    path("<int:pk>/", views.UserDataDetail.as_view()),
]
