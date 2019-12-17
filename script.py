import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
for i in range(1,20000000000):
  GPIO.output(20,GPIO.HIGH)
  time.sleep(.51)
  GPIO.output(18,GPIO.LOW)
  time.sleep(.2)
