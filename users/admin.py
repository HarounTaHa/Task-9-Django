from django.contrib import admin
from .models import Customer, Employee,EmployeeCategory,JobType

# Register your models here.

admin.site.register([Customer, Employee,EmployeeCategory,JobType])
