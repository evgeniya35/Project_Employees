from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Employee(MPTTModel):
    name = models.CharField(max_length=150)
    parent = TreeForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    position = models.CharField(max_length=100)
    emp_date = models.DateField(verbose_name='Date of employment')
    salary = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ['name']
