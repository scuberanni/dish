# Generated by Django 5.0.3 on 2025-03-08 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d2h_manager', '0017_alter_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.AddField(
            model_name='box_product',
            name='collect_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
