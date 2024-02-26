
from rest_framework import serializers
from expenses.models import Expenses


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['amount', 'referenceNO', 'expenseID','status','datePosted']
