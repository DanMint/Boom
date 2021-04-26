# Generated by Django 3.1.7 on 2021-04-25 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_db', '0017_remove_comment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='womendressesproducts',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='products_db.womendressesproducts'),
        ),
    ]
