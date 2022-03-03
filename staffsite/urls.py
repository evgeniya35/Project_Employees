from django.contrib import admin
from django.urls import path
from employees.views import index, FilteredEmployeeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('employees/', FilteredEmployeeListView.as_view(), name='employees'),
]
