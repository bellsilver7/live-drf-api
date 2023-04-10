from django.core.management import BaseCommand
from django_seed import Seed

from lives.models import Host, Program


class Command(BaseCommand):
    help = 'This command creates hosts'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            default=1,
            type=int,
            help='How many hosts do you want to create?',
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        program = Program.objects.order_by("?").first()
        seeder.add_entity(Host, number, {
            'program': program,
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} hosts created!'))
