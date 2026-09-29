from django.contrib import admin
from employee.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'hire_date', 'birthday', 'email', 'hourly_rate', 'department',)
    search_fields = ('name',)


admin.site.register(Employee, EmployeeAdmin)