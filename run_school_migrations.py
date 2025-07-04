
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_one.settings")
django.setup()

from utils.migration_utils import migrate_schools

school_dbs = ['school_abc', 'school_xyz', 'school_test']
apps = ['students', 'teachers', 'fees']

migrate_schools(school_dbs, apps)

# You can create a simple script at the root of your Django project: [Explicit approach]
# python run_school_migrations.py
