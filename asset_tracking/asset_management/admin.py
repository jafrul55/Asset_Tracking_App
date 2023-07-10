from django.contrib import admin
from .models import Company, Employee, Device, Asset, DeviceLog

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'company']

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'company', 'assigned_date', 'return_date', 'condition']

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ['asset', 'condition', 'log_date']
