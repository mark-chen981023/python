from machine import Pin, PWM, ADC
from time import sleep
import adv07.mcu as mcu

frequency = 1000
duty_cycle = 0
gpio = mcu.gpio()
light_sensor = ADC(0)
r = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
g = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
b = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)
while True:
    light_sensor_reading = light_sensor.read()
    if light_sensor_reading > 50:
        r.duty(light_sensor_reading)
        g.duty(light_sensor_reading)
        b.duty(light_sensor_reading)
    else:
        r.duty(0)
        g.duty(0)
        b.duty(0)
