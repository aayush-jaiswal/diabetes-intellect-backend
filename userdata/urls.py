from django.urls import path
from userdata import views

urlpatterns = [
    path("", views.UserDataCreate.as_view()),
    path("<int:owner_id>/", views.UserDataDetail.as_view()),
]
