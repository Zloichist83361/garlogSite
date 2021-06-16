from consignment.models import Cities, OrderConsignment
from django.shortcuts import redirect, render

from order.forms import OrderForm


# Create your views here.

def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            city_to = form.cleaned_data['city_to']
            city_from = form.cleaned_data['city_from']
            order_from = form.cleaned_data['address_from'] or form.cleaned_data['terminal_from']
            order_to = form.cleaned_data['address_to'] or form.cleaned_data['terminal_to']
            type_transporation = form.cleaned_data['type_transporation']
            nature_cargo = form.cleaned_data['nature_cargo']
            interval = form.cleaned_data['interval']
            dop = form.cleaned_data['declared_value'] or form.cleaned_data['insurance'] or form.cleaned_data['return_of_accompanying_documents'] or form.cleaned_data['sending_accompanying_documents']
            pay_cargo = form.cleaned_data['pay_cargo']
            
            return render(request, 'thanks.html')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})
