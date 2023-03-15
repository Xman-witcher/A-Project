from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=100)
    app = models.CharField(max_length=100)
    points = models.IntegerField() 
