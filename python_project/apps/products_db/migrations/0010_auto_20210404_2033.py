# Generated by Django 3.1.7 on 2021-04-04 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_db', '0009_auto_20210404_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='Mans_Sweaters_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products_db.mensweatersproducts'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='Women_Dresses_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products_db.womendressesproducts'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='Women_Pants_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products_db.womenpantsproducts'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='Women_Shirts_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products_db.womenshirtsproducts'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='Women_Skirts_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products_db.womenskirtsproducts'),
        ),
    ]