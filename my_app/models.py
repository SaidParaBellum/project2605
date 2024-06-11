from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField('Name', max_length=50)
    brand = models.CharField("Brand", max_length=80)
    year = models.IntegerField('Year')
    price = models.IntegerField('Price')

    def __str__(self):
        return self.name

