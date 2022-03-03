from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from employees.models import Employee


# Register your models here.

class EmployeeAdmin(MPTTModelAdmin):
    # raw_id_fields = ['chief']
    list_display = ('name', 'level', 'id', 'tree_id', 'position', 'parent', 'emp_date', 'salary',)

admin.site.register(Employee, EmployeeAdmin)