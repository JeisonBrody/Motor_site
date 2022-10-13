from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Car


class CarView(ListView):
    model = Car
    template_name = 'car.html'  # Выбор шаблона
    context_object_name = 'car'  # Обращение к объекту через 'car'


def login(request):
    return render(request, 'login.html')


def about_page(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'main.html')


def subaru(request):
    return render(request, 'engine/subaru.html')


