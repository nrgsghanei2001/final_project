# Generated by Django 3.2.9 on 2022-01-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_food', '0014_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='menu',
            field=models.ManyToManyField(related_name='orders', to='online_food.OrderItem'),
        ),
    ]
