from enum import unique
from django import forms
from django.forms.widgets import Textarea

from consignment.models import  OrderConsignment


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderConsignment
        fields = '__all__'   
        widgets = {
            'date_cargo': DateInput(), 'comment': Textarea()
        }