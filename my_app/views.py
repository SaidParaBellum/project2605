from django.http import HttpResponse
from django.shortcuts import render

from my_app.models import Car


# Create your views here.
def get_all(request):
    car = Car.objects.all()
    return HttpResponse(f'''
    <p>{car.name}<p>
    <p>{car.brand}<p>
    <p>{car.year}<p>
    <p>{car.price}<p>
''')

def get_cars(request, pk):
    car = Car.objects.get(id=pk)
    return HttpResponse(f'''
    <p>{car.name}<p>
    <p>{car.brand}<p>
    <p>{car.year}<p>
    <p>{car.price}<p>
''')

def delete_car(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return HttpResponse('Машина удалена')