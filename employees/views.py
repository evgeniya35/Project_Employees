from django.shortcuts import render
#from django_tables2 import RequestConfig

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from rest_framework import viewsets

from .models import Employee
from .tables import EmployeeTable
from .filters import EmployeeFilter
from .serializers import EmployeeSerializer

# Create your views here.


def index(request):
    """ Show Tree """
    #employees = Employee.objects.filter(level__lt=3).all()
    employees = Employee.objects.all()
    employee = Employee.objects.filter(level__lt=3).order_by('?').first()
    ancestors = employee.get_ancestors(include_self=True)
    family = employee.get_family()
    return render(request, 'employees/index.html', context={
        'employees': employees,
        'employee': employee,
        'ancestors': ancestors,
        'family': family,
    })


class FilteredEmployeeListView(SingleTableMixin, FilterView):
    model = Employee
    table_class = EmployeeTable
    template_name = 'employees/employees.html'

    filterset_class = EmployeeFilter


def ajax_employees(request):
    return render(request, 'employees/ajax_employees.html')

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer