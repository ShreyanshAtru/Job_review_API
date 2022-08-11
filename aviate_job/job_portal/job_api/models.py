from argparse import _CountAction
from email.mime import image
from random import choices
from secrets import choice
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.

class Candidate(models.Model):
    AP= 'Apply'
    APL = 'APPLIED'
    ACC = 'ACCEPT'
    RJT = 'REJECT'
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=100)
    mobile_number = PhoneNumberField()
    image = models.ImageField(upload_to = 'profile_pic' , default='profile_pic/default.png')
    skills_set = models.TextField(max_length=50,null=True)
    professinal_expeience = models.IntegerField(default=0)
    STATUS_CHOICES = [
        (AP, 'APPLY'),
        (APL, 'APPLIED'),
        (ACC, 'ACCEPT'),
        (RJT, 'REJECT'),
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES,default=AP)
    document = models.FileField(upload_to='documents/',blank=True)


    def __str__(self):
        return self.first_name

