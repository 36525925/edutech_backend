import datetime

from django.db import models
from users.models import CustomUser  # Assuming your User model is in an app named 'users'

class Students(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    regNumber = models.CharField(max_length=255)
    studentGender = models.CharField(max_length=255)
    deleteFlag = models.CharField(max_length=1, default="N")
    transferFlag = models.CharField(max_length=1, default="N")
    dob = models.DateField()  # Changed from CharField to DateField
    dateOfAdmission = models.DateField()  # Added this line
    healthStatus = models.CharField(max_length=255)
    classID = models.IntegerField()
    streamID = models.IntegerField()
    schoolStatus = models.CharField(max_length=255)
    dormitory = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.user.first_name} {self.user.middle_name} {self.user.last_name}"

    class Meta:
        db_table = 'students'  # Optional: specify the database table name

    class StudentsAvatar(models.Model):
        id = models.AutoField(primary_key=True)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        imgURL = models.CharField(max_length=200)
        dateCreated = models.DateTimeField(default=datetime.datetime.now)

        class Meta:
            db_table = 'studentsavatar'  # Optional: specify the database table name