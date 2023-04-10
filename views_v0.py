from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'dht11/index.html', context={
        'temperature': '25C',
        'humidity': '60%',
    })


def temperature(request):
    return render(request, 'dht11/temperature.html', context={
        'temperature': '30C',
    })


def humidity(request):
    return render(request, 'dht11/humidity.html', context={
        'humidity': '50%',
    })


def dht11(request):
    return HttpResponse('<h1> dht11 statut: get Adafruit status code </h1>')
