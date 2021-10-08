from django.db import models
from django.urls import reverse

# Create your models here.
class Employees(models.Model):
    ename=models.CharField(max_length=30)
    empid=models.PositiveIntegerField()
    esal=models.FloatField()
    eaddr=models.CharField(max_length=30)

    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('home')

