# Generated by Django 3.2.4 on 2021-07-01 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='orders',
            field=models.ManyToManyField(related_name='food_item', through='foodDelivery.OrderFoodItem', to='foodDelivery.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='foodDelivery.restaurant'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='foodDelivery.user'),
        ),
        migrations.RemoveField(
            model_name='orderfooditem',
            name='food_item',
        ),
        migrations.AddField(
            model_name='orderfooditem',
            name='food_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_food_items', to='foodDelivery.fooditem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderfooditem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_food_items', to='foodDelivery.order'),
        ),
    ]
