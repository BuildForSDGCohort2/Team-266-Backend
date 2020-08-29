from django.db import models
from django.contrib.auth.models import User
from sls.helpers.choices import student_choices
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    high_school = models.TextField()
    bursary = models.CharField(max_length=10, choices=student_choices.BURSARY_CHOICE)
    university = models.CharField(max_length=50)
    grade = models.CharField(max_length=2, choices=student_choices.GRADE_CHOICE, default=student_choices.GRADE_CHOICE[0][0])
    course = models.CharField(max_length=140)

    def __str__(self):
        return f'{self.user.username} - {self.grade}'