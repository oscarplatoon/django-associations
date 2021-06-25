from django.db import models
from django.db.models.deletion import CASCADE


class Actor(models.Model):
    pass


class Movie(models.Model):
    actors = models.ManyToManyField(
        Actor, through='Role', related_name='movies')
    # through specifies what the intermediate table is


class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=CASCADE, related_name='roles')
    movie = models.ForeignKey(Movie, on_delete=CASCADE, related_name='roles')
