#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time
import mcu


#########################函式與類別定義#########################
def on_message(topic, msg):
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
MQTT = mcu.MQTT("Mark", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")
MQTT.connect()
MQTT.subscribe("123", on_message)
#########################主程式#########################
while True:
    # 查看是否有訂閱主題發布的資料
    MQTT.check_msg()
    time.sleep(0.25)
