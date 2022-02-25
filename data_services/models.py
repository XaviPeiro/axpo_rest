from django.db import models

# Create your models here.
from cars.models import Car


class RatedTimesCar(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, db_index=True)
    times_voted = models.PositiveIntegerField()
