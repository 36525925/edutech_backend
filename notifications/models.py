from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser
import datetime

class Notifications(models.Model):
    objects = None
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(default=datetime.datetime.now)
    read = models.BooleanField(default=False)

    def str(self):
        return self.title