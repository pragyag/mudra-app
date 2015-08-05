from django.db import models

# Create your models here.

class Mudra(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    method = models.TextField()
    image = models.ImageField(upload_to='mudraimages')
    pointers = models.TextField()
    benefits = models.TextField()
    diseases = models.TextField()
    experiences = models.TextField()
