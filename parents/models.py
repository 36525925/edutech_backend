import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import CustomUser  # Assuming your User model is in an app named 'users'



class Parents(models.Model):
    parentName = models.CharField(max_length=250)
    parentIdno = models.CharField(max_length=250)
    parentPhone = models.CharField(max_length=250)
    firstLogin = models.CharField(max_length=1, default="Y")
    deletedFlag = models.CharField(max_length=1, default="N")
    status = models.BooleanField(default=True)
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.parentName

    class Meta:
        db_table = 'parents'  # Optional: specify the database table name

    class ParentsAvatar(models.Model):
        id = models.AutoField(primary_key=True)
        # parent = models.ForeignKey(Parents, on_delete=models.CASCADE)
        imgURL = models.CharField(max_length=200)
        dateCreated = models.DateTimeField(default=datetime.datetime.now)

        class Meta:
            db_table = 'parentsavatar'  # Optional: specify the database table name