from django.db import models
from django.utils import timezone

# Create your models here.

class Flow(models.Model):
    value = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.value

