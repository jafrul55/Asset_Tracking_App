# Generated by Django 4.2.1 on 2023-07-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0007_asset_remove_device_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_name',
            field=models.CharField(default=True, max_length=20),
        ),
    ]