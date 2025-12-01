import RPi.GPIO as GPIO
from  time import sleep

LED_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 100)
pwm.start(0)

print("comeco")

try:
	while True:
		for dc in range(101):
			pwm.ChangeDutyCycle(dc)
			sleep(1)
except KeyboardInterrupt:
	print("alo")
finally:
	pwm.stop()
	GPIO.cleanup()
	print("tchau")
