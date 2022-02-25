from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.db.models import F

from cars.models import Car
from data_services.models import RatedTimesCar


class Rate(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if RatedTimesCar.objects.filter(car=self.car).exists() is True:
            RatedTimesCar.objects.filter(car=self.car).update(times_voted=F("times_voted")+1)
        else:
            RatedTimesCar(car=self.car, times_voted=1).save()

        super(Rate, self).save(force_insert, force_update, using, update_fields)
