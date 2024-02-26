from django.db import models

# Create your models here.
from django.db import models
from students.models import Students
from feecategories.models import FeeCategories
from systeminfo.models import SystemInfo
from feepayments.models import FeePayments

class FeeExtensions(models.Model):
    studentID = models.ForeignKey(Students, on_delete=models.CASCADE)
    extensionPeriod = models.IntegerField()
    feeID = models.ForeignKey(FeeCategories, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SystemInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'fee_extensions'

    def __str__(self):
        return f"Fee Extension ID: {self.id}, Student: {self.studentID}, Extension Period: {self.extensionPeriod}"
