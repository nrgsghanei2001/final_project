# Generated by Django 3.2.9 on 2021-12-26 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_food', '0005_branch_foods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='foods',
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('number_of_existance', models.PositiveIntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='online_food.food')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='menu',
            field=models.ManyToManyField(related_name='branches', to='online_food.Menu'),
        ),
    ]