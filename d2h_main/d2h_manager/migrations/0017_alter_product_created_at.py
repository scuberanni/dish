# Generated by Django 5.0.3 on 2025-03-08 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d2h_manager', '0016_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
