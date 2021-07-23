import json

from django.shortcuts import redirect, render

from order.forms import OrderForm

from calculator.models import Calculate

# Create your views here.


def order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    return render(request, 'order.html', {'form': form})


def thanks(request):
    context = {
         'is_worker': request.user.groups.filter(name='worker').exists(),
    }
    return render(request, 'thanks.html', context)


def my_data(request):
    data_form = request.POST.get('data_form')
    max_weight = max(data_form[2], data_form[3]*240)
    response = Calculate.objects.filter(cityto__exact=data_form[0]).filter(cityfrom__exact=data_form[1]).filter(weightto__gte=max_weight).filter(weightfrom__lte=max_weight)
    res_order = {
        'my_data': response
    }
    return json.dumps(res_order)
