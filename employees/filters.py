import django_filters

from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    # parent = django_filters.CharFilter()

    class Meta:
        model = Employee
        fields = ['name', 'parent', 'position', 'emp_date', 'salary'] 