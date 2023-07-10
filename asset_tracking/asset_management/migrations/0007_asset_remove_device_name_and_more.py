# Generated by Django 4.2.1 on 2023-07-10 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0006_alter_deviceassignment_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('assigned_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('condition', models.CharField(max_length=20)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.company')),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='name',
        ),
        migrations.RemoveField(
            model_name='devicelog',
            name='device_assignment',
        ),
        migrations.AddField(
            model_name='device',
            name='device_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='condition',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='DeviceAssignment',
        ),
        migrations.AddField(
            model_name='asset',
            name='devices',
            field=models.ManyToManyField(related_name='device', to='asset_management.device'),
        ),
        migrations.AddField(
            model_name='asset',
            name='employees',
            field=models.ManyToManyField(related_name='employee', to='asset_management.employee'),
        ),
        migrations.AddField(
            model_name='devicelog',
            name='asset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.asset'),
        ),
    ]