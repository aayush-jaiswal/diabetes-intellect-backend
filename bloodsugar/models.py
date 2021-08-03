from django.db import models
import userauth


RECORD_TIME = (
    ("before_breakfast", "Before Breakfast"),
    ("after_breakfast", "After Breakfast"),
    ("before_lunch", "Before Lunch"),
    ("after_lunch", "After Lunch"),
    ("before_dinner", "Before Dinner"),
    ("after_dinner", "After Dinner"),
)


class BloodSugar(models.Model):
    owner = models.ForeignKey(userauth.models.User, on_delete=models.CASCADE)

    date = models.DateField()
    blood_sugar = models.IntegerField()  # mg/dL
    at_what_time = models.CharField(max_length=16, choices=RECORD_TIME)
