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
mq_server = "mqtt.singularinnovation-ai.com"
mqttClientID = "Mark"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    mqttClientID, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)
try:
    mqClient0.connect()
except:
    sys.exit()
finally:
    print("connected mqtt server")
mqClient0.set_callback(on_message)  # 設定接收訊息時要呼叫的函式
mqClient0.subscribe("hello")  # 設定想訂閱的主題
#########################主程式#########################
while True:
    # 查看是否有訂閱主題發布的資料
    mqClient0.check_msg()  # 等待以訂閱的主題發送資料
    mqClient0.ping()  # 持續確認是否還保持連線
    time.sleep(0.25)
