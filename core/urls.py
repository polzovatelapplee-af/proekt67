from django.urls import path
from app import views  # или откуда вы импортируете views

urlpatterns = [
    # Обратите внимание на параметр name='home' в конце:
    path('', views.home_view, name='home'), 
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]