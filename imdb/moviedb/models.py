from django.db import models

# Create your models here.
class Actor(models.Model):
    pass

class Movie(models.Model): 
    # Go through Role table
    actors = models.ManyToManyField(Actor, through='Role', related_name='movies')

class Role(models.Model):
    actor = model.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    movie = model.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')
    character_name = models.CharField(max_length=100)