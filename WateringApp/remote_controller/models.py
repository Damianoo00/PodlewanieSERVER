from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Programator(models.Model):
    time_wylewanie = models.IntegerField(default=0)
    time_I_pole = models.IntegerField(default=0)
    time_II_pole = models.IntegerField(default=0)
    time_III_pole = models.IntegerField(default=0)