import datetime


from django.db import models

# Create your models here.
from django.db import models

class ExpenseTypes(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    status = models.BooleanField(default=True, verbose_name='Active')
    dateCreated = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'expense_types'

    def _str_(self):
        return self.name