# Generated by Django 5.0.3 on 2024-03-21 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d2h_manager', '0008_alter_box_product_b_slno_alter_box_product_b_vscno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='box_product',
            name='r_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='d2h_manager.retailer_master'),
        ),
    ]
