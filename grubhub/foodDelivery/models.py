from django.db import models


class User(models.Model):
    pass


class Restaurant(models.Model):
    pass


class Order(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(
        'Restaurant', on_delete=models.CASCADE, related_name='orders')


class FoodItem(models.Model):
    orders = models.ManyToManyField(
        'Order', related_name='food_items', through='OrderFoodItem')


# orders and food_items have a many-to-many relationship
# we define order_food_items to be the intermediate table


class OrderFoodItem(models.Model):
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name='order_food_items')
    food_item = models.ForeignKey(
        'FoodItem', on_delete=models.CASCADE, related_name='order_food_items')
