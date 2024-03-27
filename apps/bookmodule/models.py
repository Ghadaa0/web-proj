from django.db import models

    
class Publish(models.Model):
    address = models.CharField()
 
class Book(models.Model):
 title = models.CharField()
 author = models.CharField()
 edition = models.SmallIntegerField()
