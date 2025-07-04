from django.core.management import call_command, CommandError


def migrate_schools(school_dbs, apps):
    for db in school_dbs:
        print(f'Migrating for {db}')
        for app in apps:
            try:
                print(f'Migrating app: {app}')
                call_command('migrate', app, database=db, interactive=False, verbosity=1)
                print(f'Done: {app} on {db}')
            except CommandError as ex:
                print(f'Error migrating app {app} on {db}: {ex}')
