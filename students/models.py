# students/models.py

from django.db import models
from django.urls import reverse # reverse 

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True) # roll_no 
    grade = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['roll_no'] # roll_no 

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

    def get_absolute_url(self):
       
        return reverse('student_detail', kwargs={'pk': self.pk})