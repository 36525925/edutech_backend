
# Create your models here.
from django.db import models

class UserGroup(models.Model):
    name = models.CharField(max_length=100)
    groupID = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


        class Meta:
            db_table = 'usergroup'  # Optional: specify the database table name