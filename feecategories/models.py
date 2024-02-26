from django.db import models
from systeminfo.models import SystemInfo  # Assuming this is the model for system_info

class FeeCategories(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    datePosted = models.DateField(auto_now_add=True)
    sessionID = models.ForeignKey(SystemInfo, on_delete=models.CASCADE)
    status = models.BooleanField(default=True, verbose_name='Active')

    class Meta:
        db_table = 'fee_categories'
        verbose_name_plural = 'Fee Categories'

    def _str_(self):
        return self.name