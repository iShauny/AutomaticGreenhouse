#################################################
# Author: Shaun Loughery (GitHub: iShauny)      #
# This script controls the temp. system for     #
# the greenhouse. It will operate specific      #
# ranges of temperature via H-Bridge control    #
# with lines connected to the pi. To aid in
# heating, a fan will be activated when the
# system is heating and will be turned off
# when the system is cooling.                   #
#################################################

import time
import RPi.GPIO as GPIO
import threading

# Peltier module takes time to cool down,
# so use buffer to turn off module early
TEMP_BUFFER = 5.0


class TemperatureController:
    def __init__(self, cozir, peltierForwardPin, peltierReversePin,
                 tempUpperLimit, tempLowerLimit, fanPin):
        self.cozir = cozir

        self.peltierForwardPin = peltierForwardPin  # heat
        self.peltierReversePin = peltierReversePin  # cool

        # max and min operating temps of the environment
        self.tempUpperLimit = tempUpperLimit
        self.tempLowerLimit = tempLowerLimit

        self.fanPin = fanPin

        GPIO.setup(self.peltierForwardPin, GPIO.OUT)
        GPIO.setup(self.peltierReversePin, GPIO.OUT)
        GPIO.setup(self.fanPin, GPIO.OUT)

    def start(self):
        while (1):  # loop forever

            # Temp too low, begin heating
            currentTemp = self.cozir.read_temperature()
            if (currentTemp < self.tempUpperLimit):
                GPIO.output(self.peltierReversePin, GPIO.LOW)
                # switching the peltier module too fast can damage it
                time.sleep(3)
                GPIO.output(self.peltierForwardPin, GPIO.HIGH)
                GPIO.output(self.fanPin, GPIO.HIGH)

            # Temp within acceptable range, turn module off
            elif (currentTemp > self.tempLowerLimit) \
                    and (currentTemp < (self.tempLowerLimit - TEMP_BUFFER)):
                GPIO.output(self.peltierForwardPin, GPIO.LOW)
                GPIO.output(self.peltierReversePin, GPIO.LOW)
                GPIO.output(self.fanPin, GPIO.LOW)
                # switching the peltier module too fast can damage it
                time.sleep(3)

            # Temp too high, begin cooling
            elif (currentTemp > self.tempUpperLimit):
                GPIO.output(self.peltierForwardPin, GPIO.LOW)
                # switching the peltier module too fast can damage it
                time.sleep(3)
                GPIO.output(self.peltierReversePin, GPIO.HIGH)
                GPIO.output(self.fanPin, GPIO.LOW)

    def run(self):
        t1 = threading.Thread(target=self.start)
        t1.start()
