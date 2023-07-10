# Generated by Django 4.2.1 on 2023-07-10 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0004_alter_asset_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_name',
        ),
        migrations.RemoveField(
            model_name='devicelog',
            name='asset',
        ),
        migrations.AddField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='condition',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
        migrations.AddField(
            model_name='deviceassignment',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.device'),
        ),
        migrations.AddField(
            model_name='deviceassignment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_management.employee'),
        ),
        migrations.AddField(
            model_name='devicelog',
            name='device_assignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.deviceassignment'),
        ),
    ]