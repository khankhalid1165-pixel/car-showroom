from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('customers/', views.customers, name='customers'),
    path('sales/', views.sales, name='sales'),
    path('buy/<int:car_id>/', views.buy_now, name='buy_now'),
]