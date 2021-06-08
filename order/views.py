from django.shortcuts import render

# Create your views here.


def order(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'order.html', context)