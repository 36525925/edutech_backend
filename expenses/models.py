import datetime

from django.db import models

# Create your models here.
from django.db import models
from expensetypes.models import ExpenseTypes  # Assuming this is the model for expense_types

class Expenses(models.Model):
    amount = models.IntegerField()
    referenceNO = models.CharField(max_length=10)
    expenseID = models.ForeignKey(ExpenseTypes, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, verbose_name='Approved')  # Adjust default value and verbose_name as needed
    datePosted = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'expenses'

    def __str__(self):
        return f"Expense ID: {self.id}, Amount: {self.amount}, Status: {'Approved' if self.status else 'Pending'}"
