from django.core.management import BaseCommand
from django_seed import Seed

from lives.models import Program


class Command(BaseCommand):
    help = 'This command creates programs'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            default=1,
            type=int,
            help='How many programs do you want to create?',
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(Program, number)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} programs created!'))
