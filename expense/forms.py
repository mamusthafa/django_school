from django import forms
from .models import Expense


class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_date','title','amount']
        widgets = {
            'expense_date': DateInput(),
        }