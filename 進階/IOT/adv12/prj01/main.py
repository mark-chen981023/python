# from machine import Pin, PWM
# import mcu
# import time


# def servo_angle(sg, angle):
#     if 0 <= angle <= 180:
#         sg.duty(int(1023 * (0.5 + angle / 90) / 20))


# gpio = mcu.gpio()
# sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)

# servo_angle(sg_pin, 180)  # 數值越大逆時針旋轉
# time.sleep(1)
# servo_angle(sg_pin, 90)  # 數值越小順時針旋轉
# time.sleep(1)
import mcu
import time

gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)

servo.angle(180)  # 數值越大逆時針旋轉
time.sleep(1)
servo.angle(90)  # 數值越小順時針旋轉
time.sleep(1)
