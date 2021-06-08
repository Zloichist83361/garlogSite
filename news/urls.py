from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.PostList.as_view(), name='news'),
    path('news/<slug:slug>/', views.PostDetail.as_view(), name='news_detail'),
]