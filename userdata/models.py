from django.db import models
import userauth

GENDER = (("M", "Male"), ("F", "Female"), ("O", "Other"))
DIET_TYPE = (
    ("V", "Vegetarian"),
    ("N", "Non-Vegetarian"),
)


class UserData(models.Model):
    owner = models.ForeignKey(userauth.models.User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    height = models.IntegerField()  # in cms
    weight = models.IntegerField()  # in kgs
    duration_of_diabetes = models.IntegerField()  # in years
    sex = models.CharField(max_length=1, choices=GENDER)
    diet_preference = models.CharField(max_length=1, choices=DIET_TYPE, default="V")
