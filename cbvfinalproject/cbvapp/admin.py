from django.contrib import admin
from cbvapp.models import Employees
# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['id','ename','empid','esal','eaddr']

admin.site.register(Employees,EmployeesAdmin)
