from django.shortcuts import redirect, render

from order.forms import OrderForm

# Create your views here.

def order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    return render(request, 'order.html', {'form':form})


def thanks(request):
    context = {
         'is_worker': request.user.groups.filter(name='worker').exists(),
    }
    return render(request, 'thanks.html', context)

