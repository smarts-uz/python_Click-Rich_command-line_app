# def init_django():
#     import django
#     from django.conf import settings
#
#     if settings.configured:
#         return
#
#     settings.configure(
#         INSTALLED_APPS=[
#             'app_dir',
#         ],
#     DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2',
#            'NAME': 'postgres',
#            'USER': 'postgres',
#            'PASSWORD': '1234',
#            'HOST': 'localhost',
#            'PORT': '5432',
#        }
#         }
#     )
#     django.setup()
#
#
# if __name__ == "__main__":
#     from django.core.management import execute_from_command_line
#
#     init_django()
#     execute_from_command_line()
# # from app_dir.models import Employee
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
