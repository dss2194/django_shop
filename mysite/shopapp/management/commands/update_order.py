from typing import Any
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order, Product

class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Create order")
        order = Order.objects.first()
        if not order:
            self.stdout.write("no order found")
        products = Product.objects.all()
        
        for product in products:
            order.products.add(product)
        
        order.save()

        self.stdout.write(
            self.style.SUCCESS(
            f"Siccesfully added products {order.products.all()} or oder {order}"))