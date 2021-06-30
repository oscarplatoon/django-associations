from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('User',
    on_delete=models.CASCADE,
    related_name='posts')
class User(models.Model):
    pass

class Comment(models.Model):
    author = models.ForeignKey(User,
    on_delete=models.CASCADE,
    related_name='comments')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
