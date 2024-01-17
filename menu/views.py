from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pizza


# Create your views here.

# /menu
def index(request):
    """pizzas = Pizza.objects.all()
    pizzas_names_price = [f"<b>{pizza.name} : {pizza.price} руб.</b> <br>" for pizza in pizzas]
    pizzas_names_str = "".join(pizzas_names_price)
    return HttpResponse(pizzas_names_str)"""
    pizzas = Pizza.objects.all().order_by("price")
    return render(request, "menu/index.html", {"Пицца": pizzas})


def pizza_info(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, "menu/pizza_info.html", {"pizza": pizza})

