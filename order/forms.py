from django import forms

from consignment.models import OrderConsignment

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderConsignment
        fields = '__all__'