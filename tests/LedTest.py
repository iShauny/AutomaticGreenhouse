import time
import RPi.GPIO as GPIO

LED_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)


def main():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(LED_PIN, GPIO.LOW)


if __name__ == "__main__":
    main()
