import random
import csv
import os

from django.db import transaction
from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import DynamicProvider

from employees.models import Employee


def get_professions():
    with open('professions.csv', 'r') as file:
        reader = csv.reader(file)
        return list(reader)


def add_employees(number, self):
    # employees = []
    professions_provider = DynamicProvider(
        provider_name='professions_provider',
        elements=get_professions()
    )
    for num, _ in enumerate(range(number), start=1):
        fake = Faker()
        fake.add_provider(professions_provider)
        employee = Employee(
            name=fake.name(),
            position=fake.professions_provider()[0],
            emp_date=fake.date_between(start_date='-10y', end_date='today'),
            salary=random.randrange(1500, 8000),
            parent=Employee.objects.filter(level__lt=4).order_by('?').first()
        )
        employee.save()
        # employees.append(employee)
        self.stdout.write(f'{num}/{number}')
    return num


class Command(BaseCommand):
    help = 'Generates test data for Employees'

    def add_arguments(self, parser):
        parser.add_argument(
            'n_emp',
            nargs='?',
            type=int,
            help='The number of employees',
            default=100
        )

    def handle(self, *args, **options):
        self.stdout.write('Deleting all data from Employee...')
        Employee.objects.all().delete()
        count_employees = add_employees(options['n_emp'], self)
