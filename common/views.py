
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

def landing_page(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'home.html', context)


def about_us_page(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'about_us.html', context)


def contact_us_page(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'contact_us.html', context)


def tracking_page(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'tracking.html', context)

def price_page(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'price.html', context)


def reglog(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'reglog.html', context)


def page_404(req):
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, '404_page.html', context)

