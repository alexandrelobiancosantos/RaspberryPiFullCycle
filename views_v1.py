import adafruit_dht
import board
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    dhtDevice = adafruit_dht.DHT11(board.D17)
    while True:
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            return render(request, 'dht11/index.html', context={
                'temperature': temperature_c,
                'humidity': humidity,
            })
        except RuntimeError as error:
            return render(request, 'dht11/index.html', context={
                'temperature': error.args[0],
                'humidity': error.args[0],
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
