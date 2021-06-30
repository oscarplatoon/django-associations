from django.db import models

# Create your models here.
### Models (a.k.a. Tables)
class User(models.Model):
    pass

class Restaurant(models.Model):
    pass

class Order(models.Model):
# - An order belongs to a user
# - A user has many orders
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='orders')

# - An order belongs to a restaurant
# - A restaurant has many orders
    restaurant = models.ForeignKey(Restaurant,
        on_delete=models.CASCADE,
        related_name='orders')


class FoodItem(models.Model):
    # This Many to Many relation ties Orders and Food Items together for Tests 5,6, and 7.
    orders = models.ManyToManyField('Order',
    related_name='food_items',
    through='OrderFoodItem')

class OrderFoodItem(models.Model):
    pass
# - An order_food_item belongs to a food_item
# - A food item has many order_food_items
    food_item = models.ForeignKey(FoodItem,
        on_delete=models.CASCADE,
        related_name='order_food_items')
# - An order_food_item belongs to an order
# - An order has many order_food_items
    order = models.ForeignKey(Order,
        on_delete=models.CASCADE,
        related_name='order_food_items')




### Associations
# - And finally if you have set up your associations correctly a user should have many food items through orders. See the final test. 
