# Generated by Django 3.1 on 2020-08-17 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
