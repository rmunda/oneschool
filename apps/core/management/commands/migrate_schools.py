from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.management import call_command
from utils.migration_utils import migrate_schools


class Command(BaseCommand):
    help = 'Run migrations for all school databases and business apps'

    def add_arguments(self, parser):
        parser.add_argument(
            '--apps',
            nargs='+',
            type=str,
            help='List of app labels to migrate (default: students, teachers, fees)',
        )

    def handle(self, *args, **options):
        # Dynamically get DBs that start with "school_"
        school_dbs = [db for db in settings.DATABASES if db.startswith('school_')]
        if not school_dbs:
            self.stdout.write(self.style.WARNING('No school_* databases found in settings.DATABASES'))
            return

        # Get apps from args, or use default
        apps = options['apps'] or ['students', 'teachers', 'fees']

        self.stdout.write(self.style.SUCCESS(f'Running migrations on DBs: {school_dbs}'))
        self.stdout.write(self.style.SUCCESS(f'Apps: {apps}'))

        migrate_schools(school_dbs, apps)
