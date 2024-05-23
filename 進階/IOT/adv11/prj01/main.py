#########################匯入模組#########################
import time
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP=(wi.ip)")

MQTT = mcu.MQTT("Mark", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")
MQTT.connect()


#########################主程式#########################
while True:
    msg = input("input message:")
    MQTT.publish("123", msg)
    time.sleep(0.5)
