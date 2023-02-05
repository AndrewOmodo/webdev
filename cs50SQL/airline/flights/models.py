from django.db import models

#Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city} ({self.code})'

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") #once deleted, all coresponding data is also deleted
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")   
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination}' #returns a more detailed info about flight data in the python shell