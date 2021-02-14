from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50, default='Software Engineer')

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_time= models.DateTimeField()
    end_time= models.DateTimeField()

    def __str__(self):
    	return self.user.username

    
