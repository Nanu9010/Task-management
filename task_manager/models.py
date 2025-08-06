from tkinter.constants import CASCADE

from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models



class Login(models.Model):

    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
    ]
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15, validators=[MinLengthValidator(8)])

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


    def __str__(self):
        return self.username


class SignUp(models.Model):
    GENDER_CHOICE =[('Male','Male'),('Female','Female')]
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15, validators=[MinLengthValidator(8)])
    next_password = models.CharField(max_length=15, validators=[MinLengthValidator(8)])
    birthdate = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE, default='Male')
    mail =models.EmailField()
    contact = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message= 'Enter 10 digit only : ')])
    address = models.CharField(max_length=100, validators=[RegexValidator(message='Enter your Address : ')])

class Task(models.Model):
    STATUS_CHOICE=[
        ('pending','pending'),
        ('process','process'),
        ('complete','complete')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')
    project_manager = models.ForeignKey(Login, on_delete=models.CASCADE, limit_choices_to={'role':'Employee'})

    def __str__(self):
        return self.title
