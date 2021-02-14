from django.core.management.base import BaseCommand
from employee_register.views import GenerateFakeData

class Command(BaseCommand):
    # help = 'Displays current time'

    def handle(self, *args, **kwargs):
        GenerateFakeData()
        self.stdout.write("Dummy data created!")