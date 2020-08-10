from cozir import Cozir
import time

sensor = Cozir('/dev/serial0')  # COVIR sensor


def main():
    while True:
        print('CO2: {:.0f} ppm'.format(sensor.read_CO2()))
        print('temp: {:.1f} C'.format(sensor.read_temperature()))
        print('humid: {:.1f}% RH'.format(sensor.read_humidity()))
        time.sleep(2)


if __name__ == "__main__":
    print("Testing")
    main()
