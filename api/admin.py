from django.contrib import admin
from .models import *
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['employee_id','full_name','created']
    class Meta:
        ordering =["-created","employee_id"]
    
admin.site.register(Employee,EmployeeAdmin)