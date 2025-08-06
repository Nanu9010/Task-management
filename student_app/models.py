from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    std = models.CharField(max_length=5,
                           choices=[('I','I'),('II', 'II'),('III','III'),('IV','IV'),('V','V'),('VI','VI'),('VII','VII'),('VII','VII'),('XI','XI'),('X','X')],
                           default='I'
                           )

    science = models.IntegerField()
    maths = models.IntegerField()
    english = models.IntegerField()
    percentage = models.FloatField(blank=True, null=True)

class SignUp(models.Model):
    user_id = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)
    gender = models.Choices
    contact = models.CharField(max_length=10)
    Teacher = models.BooleanField()
    Principle = models.BooleanField()

    def __str__(self):
        return self.user_id

class Login(models.Model):
    user_id = models.CharField(max_length=25)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_id




#
# class Add(models.Model):
#     name = models.CharField(max_length=25)
#     std = models.CharField(max_length=5,
#                            choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'),('VII', 'VII'), ('VII', 'VII'), ('XI', 'XI'), ('X', 'X')],
#                            default='I'
#                            )
#     science = models.IntegerField()
#     maths = models.IntegerField()
#     english = models.IntegerField()
#     percentage = models.FloatField(blank=True, null=True)
#     # percentage = models.FloatField(max_length=5)
#

