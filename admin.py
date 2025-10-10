from django.contrib import admin
from .models import Car, Customer, Sale

# Car model admin
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image')  # Fields as defined in Car model

# Customer model admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')  # Fields as defined in Customer model

# Sale model admin
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'customer', 'sale_date')  # Fields as defined in Sale model
    list_filter = ('sale_date', 'car')  # Optional filters for better admin usability
    search_fields = ('customer__name', 'car__name')  # Optional search by customer or car
