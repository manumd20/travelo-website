from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.fun,name='fun'),
    path('contact',views.contact, name='contact'),
    path('news',views.news, name='news')
]
