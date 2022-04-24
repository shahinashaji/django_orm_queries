from django.db import models


# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=20, default='abc')
