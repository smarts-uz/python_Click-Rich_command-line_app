# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_dir.settings")
# import django
# django.setup()
#
# from app_dir.models import Employee
#
# # retrieve objects from the database
# qs = Employee.objects.all()
# for obj in qs:
#     print(obj.name, obj.contact)
from django.conf import settings


settings.configure(
    DATABASE_ENGINE = "postgresql_psycopg2",
    DATABASE_NAME = "postgres",
    DATABASE_USER = "postgres",
    DATABASE_PASSWORD = "1234",
    DATABASE_HOST = "localhost",
    DATABASE_PORT = "5432",
    INSTALLED_APPS = "app_dir"
)
from django.db import models
from app_dir.models import models