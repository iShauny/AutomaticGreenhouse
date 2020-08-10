import time
import RPi.GPIO as GPIO

HBRIDGE_FORWARD_PIN = 18
HBRIDGE_REVERSE_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(HBRIDGE_FORWARD_PIN, GPIO.OUT)
GPIO.setup(HBRIDGE_REVERSE_PIN, GPIO.OUT)


def main():
    GPIO.output(HBRIDGE_FORWARD_PIN, GPIO.HIGH)
    GPIO.output(HBRIDGE_REVERSE_PIN, GPIO.LOW)
    time.sleep(60)
    GPIO.output(HBRIDGE_FORWARD_PIN, GPIO.LOW)
    time.sleep(3)  # too fast switching can damage peltier
    GPIO.output(HBRIDGE_REVERSE_PIN, GPIO.HIGH)
    time.sleep(60)
    GPIO.output(HBRIDGE_REVERSE_PIN, GPIO.LOW)


if __name__ == "__main__":
    main()
