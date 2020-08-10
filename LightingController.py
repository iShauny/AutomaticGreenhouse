#################################################
# Author: Shaun Loughery (GitHub: iShauny)      #
# This script controls the lighting system for  #
# the greenhouse. It will operate specific      #
# hours of the dayand use a transistor          #
# with base connected to the pi.                #
#################################################

from datetime import datetime, time
import RPi.GPIO as GPIO
import threading

# These define the max operating hours of the environment
LED_MIN_START_TIME = time(11, 00)  # 11 AM
LED_MAX_END_TIME = time(21, 00)  # 9 PM


class LightingSystem:
    def __init__(self, ledPin):
        self.ledPin = ledPin
        GPIO.setup(self.ledPin, GPIO.OUT)

    def start(self, numLightHours):
        while (1):  # loop system forever
            if datetime.datetime.now().time() == LED_MIN_START_TIME:
                GPIO.output(self.ledPin, GPIO.HIGH)
                print("Lights On!")

                # determine ideal end time, convert to seconds
                endTime = LED_MIN_START_TIME + (60 * 60 * numLightHours)
                # check when we have reached our number of hours or end time
                while ((datetime.datetime.now().time() < LED_MAX_END_TIME)
                       and datetime.datetime.now().time() < endTime):
                    continue
                GPIO.output(self.ledPin, GPIO.LOW)
                print("Lights Off!")

    def run(self, numLightHours):
        t1 = threading.Thread(target=self.start(numLightHours))
        t1.start()
