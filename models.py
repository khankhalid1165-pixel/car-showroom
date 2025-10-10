from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, default="Unknown Customer")
    email = models.EmailField(default="example@example.com", unique=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100, default="Unknown Car")
    price = models.FloatField()
    image = models.ImageField(upload_to='cars/')
    model = models.CharField(max_length=100, default="Standard Model")
    register_year = models.IntegerField(default=2020)
    km_run = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)
    fuel_type = models.CharField(max_length=50, default="Petrol")
    status = models.CharField(max_length=50, default="Available")

    def __str__(self):
        return self.name

class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add=True)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.car.name} bought by {self.customer.name}"
    
    def save(self, *args, **kwargs):
        # Auto-calculate total price
        self.total_price = self.car.price
        super().save(*args, **kwargs)