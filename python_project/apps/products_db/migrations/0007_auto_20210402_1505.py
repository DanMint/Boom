# Generated by Django 3.1.7 on 2021-04-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_db', '0006_womenshirtsproducts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandressshirtsproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='manpantsproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='manshirtsproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='mensweatersproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='womendressesproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='womenpantsproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='womenskirtsproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
