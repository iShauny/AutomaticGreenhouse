from cozir import Cozir
from LightingController import LightingController
from TemperatureController import TemperatureController
import RPi.GPIO as GPIO

# Define our pin numbers for our transducers
LED_PIN = 37
HBRIDGE_FORWARD_PIN = 12
HBRIDGE_REVERSE_PIN = 16
FAN_PIN = 35
GSS_TXD_PIN = 8
GSS_RXD_PIN = 10

# Predefined user constants
# These vary based on the plant being grown
NUM_LIGHT_HOURS = 12  # The number of hours the plant should be receiving light
TEMP_LOWER_LIMIT = 21  # The minimum temperature threshold for the plant
TEMP_UPPER_LIMIT = 31  # The maximum temperature threshold for the plant

sensor = Cozir('/dev/ttyUSB0')  # COVIR sensor


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # start lighting system
    lightingSystem = LightingController(LED_PIN)
    lightingSystem.run(NUM_LIGHT_HOURS)

    # start temp system
    tempSystem = TemperatureController(sensor, HBRIDGE_FORWARD_PIN,
                                       HBRIDGE_REVERSE_PIN, TEMP_UPPER_LIMIT,
                                       TEMP_LOWER_LIMIT, FAN_PIN)
    tempSystem.run()
