from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField, ForeignKey, OneToOneField

class User(models.Model):
    pass

class Restaurant(models.Model):
    pass

class Order(models.Model):
    user = ForeignKey('User', related_name='orders', on_delete=CASCADE)
    restaurant = ForeignKey('Restaurant', related_name='orders', on_delete=CASCADE)
    

class FoodItem(models.Model):
    orders = ManyToManyField('Order', related_name='food_items', through='OrderFoodItem')

class OrderFoodItem(models.Model):
    order = ForeignKey('Order', related_name='order_food_items', on_delete=CASCADE)
    food_item = ForeignKey('FoodItem', related_name='order_food_items', on_delete=CASCADE)