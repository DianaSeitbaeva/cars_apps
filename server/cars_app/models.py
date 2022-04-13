from turtle import speed
from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=255)
    year = models.DateField()
    speed = models.IntegerField()
    volume = models.FloatField()
    type_car = models.ForeignKey(
        'TypeCars',
        on_delete=models.PROTECT,
        null=False
    )
    pay = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class TypeCars(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.type
