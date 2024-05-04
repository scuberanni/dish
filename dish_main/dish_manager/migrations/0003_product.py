# Generated by Django 5.0.3 on 2024-03-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d2h_manager', '0002_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cable', models.PositiveIntegerField(default=0, max_length=50, null=True)),
                ('lnb', models.PositiveIntegerField(default=0, max_length=50, null=True)),
                ('dish', models.PositiveIntegerField(default=0, max_length=50, null=True)),
                ('kit', models.PositiveIntegerField(default=0, max_length=50, null=True)),
            ],
        ),
    ]
