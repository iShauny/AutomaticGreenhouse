import time
import RPi.GPIO as GPIO

FAN_PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(FAN_PIN, GPIO.OUT)


def main():
    GPIO.output(FAN_PIN, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(FAN_PIN, GPIO.LOW)


if __name__ == "__main__":
    main()
