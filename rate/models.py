from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from cars.models import Car


class Rate(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
