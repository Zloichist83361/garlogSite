from django.urls import path

from calculator.views import calc

urlpatterns = [
    path('calc/', calc, name='calc'),
    
]