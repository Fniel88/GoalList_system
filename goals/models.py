from django.db import models

# Create your models here.
class Goals(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)