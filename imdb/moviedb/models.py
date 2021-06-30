from django.db import models


class Actor(models.Model):
    movies = models.ManyToManyField(
        'Movie',
        through='Role',
        related_name='actors'
    )


class Movie(models.Model):
    # Either way works.
    pass
    # actors = models.ManyToManyField(
    #     Actor,
    #     through='Role',
    #     related_name='movies')
    # through specifies what the intermediate table is


class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')