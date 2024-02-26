from django.db import models

# Create your models here.
from students.models import Students
from feecategories.models import FeeCategories
from systeminfo.models import SystemInfo  # Assuming this is the model for system_info


class FeePayments(models.Model):
    studentID = models.ForeignKey(Students, on_delete=models.CASCADE)
    feeID = models.ForeignKey(FeeCategories, on_delete=models.CASCADE)
    referenceNO = models.CharField(max_length=100)
    amountPaid = models.DecimalField(max_digits=10, decimal_places=2)  # Adjusted to use DecimalField for currency
    datePosted = models.DateField(auto_now_add=True)
    sessionID = models.ForeignKey(SystemInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'fee_payments'
        verbose_name_plural = 'Fee Payments'

    def str(self):
        return