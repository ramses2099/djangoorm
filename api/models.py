from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Department
class Department(models.Model):
    department_id = models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="department_id")    
    dep_name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

# Student
class Student(models.Model):
    student_id = models.BigAutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name="student_id")
    stud_name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, 
                                  on_delete=models.CASCADE,
                                  verbose_name="department_id")
    created = models.DateTimeField(auto_now_add=True)
    
# Product
class Product(models.Model):
    product_id = models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name="product_id")
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    
# Customer
class Customer(models.Model):
    customer_id = models.BigAutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name="customer_id")
    name = models.CharField(max_length=250)
    product = models.ManyToManyField(Product)
    created = models.DateTimeField(auto_now_add=True)
    
# Employee
class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True,
                                      auto_created=True,
                                      verbose_name="employee_id")
    full_name = models.CharField(max_length=350)
    user = models.OneToOneField(User,
                                on_delete=models.SET_NULL,
                                null=True,                                
                                verbose_name="user")
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    
    # class Meta:
    #     ordering =[models.F("employee_id").desc()]
    