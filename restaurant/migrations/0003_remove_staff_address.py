# Generated by Django 3.2.9 on 2022-01-10 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_staff_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='address',
        ),
    ]
