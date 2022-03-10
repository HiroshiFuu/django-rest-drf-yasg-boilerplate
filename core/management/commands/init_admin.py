from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Initilize admin user"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        if User.objects.all().count() == 0:
            User.objects.create_superuser(username='admin', password='password', email='hiroshifuu@outlook.com', first_name='Hao', last_name='FENG')
            print('admin user created')
        else:
            print('admin user already exists')
