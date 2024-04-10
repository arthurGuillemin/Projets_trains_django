from django.db import models

# Create your models here.
class Trains(models.Model) :
    trainsId = models.AutoField(primary_key=True)
    origine = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    heure_de_depart = models.CharField(max_length=20)
    heure_arrive = models.CharField(max_length = 20)
    description = models.CharField(max_length = 20000)


from trainsApp.models import Trains



