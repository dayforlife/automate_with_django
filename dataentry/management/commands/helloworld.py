from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "prints hello world"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies user name')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        self.stdout.write(f'Hello world {name}')