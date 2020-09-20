
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('glasses', views.glasses, name='glasses'),
    path('watches', views.watches, name='watches'),
    path('glass/<str:prodname>', views.glass, name='glass'),
    path('watch/<int:id>', views.watch, name='watch'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]