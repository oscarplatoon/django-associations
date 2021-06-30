from django.db import models

class Review(models.Model):
    product = models.ForeignKey('Product',
        on_delete=models.CASCADE,
        related_name='reviews')
    user = models.ForeignKey('User',
        on_delete=models.CASCADE,
        related_name='reviews')

class Shop(models.Model):
    owner = models.OneToOneField('User',
        on_delete=models.CASCADE,
        related_name='shop')

class Product(models.Model):
    shop = models.ForeignKey('Shop',
        on_delete=models.CASCADE,
        related_name='products')

class User(models.Model):
    pass

    

# ```
# shop.owner # should return a User
# shop.products # products sold by this shop

# product.shop
# product.reviews

# review.product
# review.user

# user.reviewed_products
# user.shop # if this user owns a shop, returns the shop. For most users this would return nil.
# ```