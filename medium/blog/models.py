from django.db import models

# Create your models here.


class User(models.Model):
    pass


class Post(models.Model):
    # a post has one author. link a foreignkey to author
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    # a comment only belongs to one post. link a foreignkey to post
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, related_name='comments')

    # a comment has one author. link a foreignkey to author
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='comments')
