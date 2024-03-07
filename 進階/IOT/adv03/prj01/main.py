from machine import Pin, PWM
from time import sleep
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

while True:
    for i in range(0,1022):
            led.duty(i)
            sleep(0.01)
    for g in range(0,1022):
            led.duty(1023-g)
            sleep(0.01)

