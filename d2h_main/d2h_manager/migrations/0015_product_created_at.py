# Generated by Django 5.0.3 on 2025-03-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d2h_manager', '0014_to_ret_product_box2_alter_sale_product_cable3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-03-08 12:00:00'),
            preserve_default=False,
        ),
    ]
