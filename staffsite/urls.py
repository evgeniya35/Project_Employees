from django.contrib import admin
from django.urls import path, include
from employees.views import index, FilteredEmployeeListView, EmployeeViewSet, ajax_employees

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ajax_employees', EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('employees/', FilteredEmployeeListView.as_view(), name='employees'),
    path('api/', include(router.urls)),
    path('ajax_employees/', ajax_employees, name='ajax_employees')
]
