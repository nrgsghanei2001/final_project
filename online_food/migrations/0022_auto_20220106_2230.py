# Generated by Django 3.2.9 on 2022-01-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_food', '0021_alter_menuitem_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='order_time',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='order_time',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
