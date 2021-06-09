from django.urls import path

from common.views import landing_page, tracking_page, page_404, offices_page, price_page



urlpatterns = [
    path('', landing_page, name='index'),
    #path('contact/', contact_us_page, name="contact"),
    path('tracking/', tracking_page, name='tracking'),
    path('offices/', offices_page, name='offices'),
    path('price/', price_page, name='price'),
    path('page_404/', page_404, name='page_404'),
    
]