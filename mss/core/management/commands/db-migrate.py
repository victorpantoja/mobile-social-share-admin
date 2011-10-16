import os
import sys

from os.path import exists, abspath
from django.core.management.base import BaseCommand
from optparse import make_option
from django.conf import settings
from simple_db_migrate.config import InPlaceConfig
from simple_db_migrate.main import Main
from mss.core.locator import *

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--show-sql', action="store_true", dest='show_sql', default=False,
            help='Show sql script'),
        make_option('--env', dest='environment', default=None,
            help='Environment to migrate application'),
        make_option('--show-sql-only', action="store_true", dest='show_sql_only', default=False,
            help='Show sql script and no execute'),
        make_option('--drop', action="store_true", dest='drop', default=False,
            help='drop database before execution'),
        make_option('-m', '--migration', dest='target_migration', default=None,
            help='target version to migrate to'),
        make_option('--project', dest='project', default=None,
            help='Project deploy setting file'),
        make_option('-p', '--paused-mode', action="store_true", dest='paused_mode', default=False,
            help='exec in paused mode'),
        make_option('-l', '--log-level', dest='log_level', default=1,
            help='logging level'),
        make_option('--db-user', dest='db_user', default=settings.DATABASES['default']['USER'],
            help='database user'),
        make_option('--db-password', dest='db_password', default=settings.DATABASES['default']['PASSWORD'],
            help='database password'),
        make_option('--db-host', dest='db_host', default=settings.DATABASES['default']['HOST'],
            help='database host'),
        make_option('--db-name', dest='db_name', default=settings.DATABASES['default']['NAME'],
            help='database name'),
    )

    help = "Migrate databases."
    args = "[db_migrate_options]"

    def handle(self, *args, **options):
        if options.get('environment'):
            self.db_reset(*args, **options)
        else:
            self.db_migrate(*args, **options)

    def locate_migrations(self):
        files = locate_resource_dirs("migrations", "*.migration")

        if hasattr(settings, 'OTHER_MIGRATION_DIRS'):
            other_dirs = settings.OTHER_MIGRATION_DIRS
            if not isinstance(other_dirs, (tuple, list)):
                raise TypeError, 'A setting "OTHER_MIGRATION_DIRS" deve ser uma ' \
                      'tupla ou lista, contendo paths relativos'

            files.extend([abspath(x) for x in other_dirs])

        return ':'.join(files)

    def db_migrate(self, *args, **options):
        migration_dirs = self.locate_migrations()
        if migration_dirs == '':
            print 'No database migrations found.\n'
            sys.exit(0)
        
        config = InPlaceConfig(db_host=options.get('db_host'), db_user=options.get('db_user'),
                               db_password=options.get('db_password'), db_name=options.get('db_name'),
                               migrations_dir=migration_dirs)

        config.put("schema_version", options.get('target_migration'))
        config.put("show_sql", options.get('show_sql'))
        config.put("show_sql_only", options.get('show_sql_only'))
        config.put("new_migration", None)
        config.put("drop_db_first", options.get('drop'))
        config.put("log_level", int(options.get('log_level')))
        config.put("paused_mode", options.get('paused_mode'))
        Main(config).execute()

    def db_reset(self, *args, **options):
        command = "cap "

        if options.get('project', None) and options.get('environment'):
            command += "%s:%s" % (options.get('project'), options.get('environment'))
        else:
            print 'Parameters not found --project: %s , --env: %s. See --help.' % (options.get('project'), options.get('environment'))
            sys.exit(0)

        if options.get('drop'):
            command += " db:reset"
        else:
            command += " db:migrate"

        print "\n- Running '%s' ..." % command

        os.system(command)

