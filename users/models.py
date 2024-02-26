import datetime
from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    middle_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='',
        related_name="customuser_groups",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",
        related_query_name="customuser",
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'

class UserAvatar(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    imgURL = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'useravatar'
