from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    dep_name=models.CharField(max_length=100)


class User(AbstractUser):
    usertype=models.CharField(max_length=50)

class Teacher(models.Model):
    tid=models.ForeignKey(User,on_delete=models.CASCADE)
    depid=models.ForeignKey(Department,on_delete=models.CASCADE)
    Age=models.PositiveIntegerField()
    Address=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=50)


class Student(models.Model):
    sid=models.ForeignKey(User,on_delete=models.CASCADE)
    depid=models.ForeignKey(Department,on_delete=models.CASCADE)
    Age=models.IntegerField()
    Address=models.CharField(max_length=100)
    Phoneno=models.IntegerField()

