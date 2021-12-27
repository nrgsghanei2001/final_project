# Generated by Django 3.2.9 on 2021-12-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.ManyToManyField(related_name='customers', to='accounts.Address'),
        ),
    ]
