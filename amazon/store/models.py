from django.db import models


class User(models.Model):
    pass


class Shop(models.Model):
    owner = models.OneToOneField(
        'User', on_delete=models.CASCADE, related_name='shop')


class Product(models.Model):
    shop = models.ForeignKey(
        'Shop', on_delete=models.CASCADE, related_name='products')


class Review(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='reviews')
