from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    day = models.CharField(max_length=100)

def __str__(self):
    return self.title
