from machine import Pin, PWM
from time import sleep
import mcu
frequency = 1000
duty_cycle = 0
gpio = mcu.gpio()
r = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
g = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
b = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)

# while True:
#     for a in range(0,1022):
#             r.duty(a)
#             sleep(0.001)
#     for b in range(0,1022):
#             r.duty(1023-b)
#             sleep(0.001)
#     for c in range(0,1022):
#             g.duty(c)
#             sleep(0.001)
#     for d in range(0,1022):
#             g.duty(1023-d)
#             sleep(0.001)
#     for g in range(0,1022):
#             b.duty(g)
#             sleep(0.001)
#     for f in range(0,1022):
#             b.duty(1023-f)
#             sleep(0.001)
#                                   主程式
while True:
    for duty_cycle in range(1023,-1,-1):
        r.duty(duty_cycle)
        g.duty(1023 - duty_cycle)
        sleep(0.002)
    for duty_cycle in range(1023,-1,-1):
        b.duty(duty_cycle)
        r.duty(1023 - duty_cycle)
        sleep(0.002)
    for duty_cycle in range(1023,-1,-1):
        g.duty(duty_cycle)
        b.duty(1023 - duty_cycle)
        sleep(0.002)