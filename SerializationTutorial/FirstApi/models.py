from django.db import models

# Create your models here.
class PassengerClass(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    rewards = models.IntegerField()

    def __str__(self):
        return self.name

