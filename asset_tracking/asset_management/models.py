from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Device(models.Model):
    device_name = models.CharField(max_length=20,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.device_name
    
class Asset(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    employees = models.ManyToManyField(Employee,related_name='employee')
    devices = models.ManyToManyField(Device,related_name='device')
    serial_number = models.CharField(max_length=100,unique=True)
    assigned_date = models.DateField(null=True,blank=True)
    return_date = models.DateField(null=True,blank=True)
    condition = models.CharField(max_length=20)
      
    def __str__(self):
        return self.serial_number
    
class DeviceLog(models.Model):
    asset = models.ForeignKey(Asset,on_delete=models.CASCADE,null=True)
    condition = models.CharField(max_length=30)
    log_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.asset} {self.condition}"