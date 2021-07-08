from django.db import models

# Create your models here.
class User(models.Model):
    pass 
    

class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    product_reviews = models.ManyToManyField(User, through='Review')

class Review(models.Model): # this is your join table!!!!!
    # user is providing review
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    
    # we are reviewing the product, itself
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    
    # can also add--
    text = models.TextField()
