from django.db import models


# class Employee(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     tag = models.ForeignKey('Category',on_delete=models.PROTECT, null=True)
#     def __str__(self):
#         return self.first_name
#
#     class Meta:
#         db_table = "Employee_Foreign"
#
# class Category(models.Model):
#     name = models.CharField(max_length=50, db_index=True)
#     # updated_by = models.ForeignKey('app_dir.Employee',default=None, related_name='+',on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "Category_Foreign"
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    # class Meta:
    #     db_table = 'Musician'


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    # class Meta:
    #     db_table = 'Album'


