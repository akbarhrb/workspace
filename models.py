from django.db import models
from datetime import datetime

# Create your models here.
class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=300,  null=True )
    timeCreated = models.DateTimeField(default=datetime.now)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task    
    
class Dc(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50) 
    price = models.IntegerField() 

    def __str__(self):
        return self.name  