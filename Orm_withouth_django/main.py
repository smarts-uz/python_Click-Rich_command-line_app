# import sys
# import inspect
# import os.path
# import click
# import logging
#
# sys.path.append(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_dir.settings')
#
# import django
#
# django.setup()
#
#
# @click.group()
# def cli():
#     pass
#
#
# @click.command()
# @click.option('--url',
#               prompt='URL',
#               help='The URL to fetch')
# @click.option('--cache/--no-cache',
#               help='Whether to cache or not',
#               default=True)
# def import_single(url, cache):
#     pass
#
#
# if __name__ == '__main__':
#     cli.add_command(import_single)
#     cli()
#
# from rich import pretty
# from rich.logging import RichHandler
#
# FORMAT = "%(message)s"
# logging.basicConfig(
#     level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
# )
# log = logging.getLogger("rich")
# log.info('[green]Data written to out file:[/] {}'.format(out_file), extra={'markup': True})

import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# Import your models for use in your script
from app_dir.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few users in the database
# list = ['Vanesa', 'Lila', 'Ziki']
# for i in list:
#     data = {'name': i}
x = Musician.objects.create(instrument='violonchel', last_name='sabi', first_name='Ldofa')
Album.objects.create(num_stars=5, release_date='2014-12-07',artist=x,name='Pehehia')