# Generated by Django 3.1.7 on 2021-03-28 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_db', '0004_womenshirtsproducts_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='womenshirtsproducts',
            name='check',
        ),
    ]
