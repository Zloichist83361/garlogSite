from django.urls import path

from order.views import order

urlpatterns = [
    path('order/', order, name='order'),
    
]