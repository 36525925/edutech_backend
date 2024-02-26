from django.db import models
from feecategories.models import FeeCategories  # Assuming this is the model for fee_categories

class PaymentGroups(models.Model):
    feeID = models.ForeignKey(FeeCategories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'payment_groups'

    def _str_(self):
        return f"Payment Groups ID: {self.id}, Fee Categories: {self.feeID}"