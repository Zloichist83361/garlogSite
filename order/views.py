
from consignment.models import OrderConsignment
from django.shortcuts import  get_object_or_404, redirect, render
from django.views.generic import View
from order import forms
from order.forms import OrderForm


# Create your views here.

def order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks.html')
        print(form.errors)
    return render(request, 'order.html', {'form':form})
