from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=50, default='Dan')

    def __str__(self):
        return self.name

