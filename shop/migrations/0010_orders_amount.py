# Generated by Django 2.2.3 on 2019-07-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_orders_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
