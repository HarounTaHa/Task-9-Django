from django.contrib.auth.models import  User
from django.db import models


# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, unique=True)
    user = models.OneToOneField(User, related_name='customer',on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    has_project = models.BooleanField(default=False)

    def __str__(self):
        return f'Name:{self.first_name} {self.last_name} | email : {self.email}'


class EmployeeCategory(models.Model):
    category = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.category


class JobType(models.Model):
    type = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.type


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, related_name='employee',on_delete=models.CASCADE)
    employee_categories = models.ForeignKey(EmployeeCategory, null=True, on_delete=models.SET_NULL)
    employee_job_type = models.ForeignKey(JobType, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    is_supervisor = models.BooleanField(default=False)

    def __str__(self):
        return f'Name : {self.user}, Phone :{self.phone_number} , Job type : {self.employee_job_type},Categories : {self.employee_categories}'
