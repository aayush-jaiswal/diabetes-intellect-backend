from django.urls import path
from bloodsugar import views

urlpatterns = [
    path("", views.UserRecordCreate.as_view()),
    path("<int:owner_id>/", views.UserRecordDetail.as_view()),
]
