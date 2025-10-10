from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Customer, Sale

def home(request):
    total_cars = Car.objects.count()
    total_customers = Customer.objects.count()
    total_sales = Sale.objects.count()
    return render(request, 'showroom/home.html', {
        'total_cars': total_cars,
        'total_customers': total_customers,
        'total_sales': total_sales
    })

def inventory(request):
    cars = Car.objects.all()
    return render(request, 'showroom/inventory.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'showroom/car_detail.html', {'car': car})

def customers(request):
    all_customers = Customer.objects.all()
    return render(request, 'showroom/customers.html', {'customers': all_customers})

def sales(request):
    all_sales = Sale.objects.all()
    return render(request, 'showroom/sales.html', {'sales': all_sales})

def buy_now(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        if not name or not email:
            return render(request, 'showroom/buy_now.html', {
                'car': car, 
                'error': 'Please enter your name and email'
            })
        
        try:
            # Create or get customer
            customer, created = Customer.objects.get_or_create(
                email=email,
                defaults={
                    'name': name, 
                    'contact': phone,
                    'address': 'Address not provided'
                }
            )
            
            # Create sale
            sale = Sale.objects.create(car=car, customer=customer)
            
            return render(request, 'showroom/buy_success.html', {
                'name': name,
                'car': car
            })
            
        except Exception as e:
            return render(request, 'showroom/buy_now.html', {
                'car': car, 
                'error': f'Error processing purchase: {str(e)}'
            })
    
    return render(request, 'showroom/buy_now.html', {'car': car})