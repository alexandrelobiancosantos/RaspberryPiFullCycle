import time

import adafruit_dht
import board

dhtDevice = adafruit_dht.DHT11(board.D17)

while True:
    try:
        #  Print values
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temperature: {:.1f} C  *  Humidity: {}%". format(temperature, humidity))
    except RuntimeError as error:
        #  Some commun dht sensor error - keep doing...
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        dhtDevice. exit()
        raise error
    time.sleep(2.0)