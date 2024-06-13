#########################匯入模組#########################
import paho.mqtt.client as mqtt
import time
import getpass
import os
import whisper

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
model = ChatOpenAI(model="gpt-4o", temperature=0.2)
from langchain_core.messages import HumanMessage

model_whisper = whisper.load_model("base")
#########################主程式#########################
while True:
    ans = model_whisper.transcribe(
        "C:/Users/markc/Desktop/python/進階/IOT/adv13/prj01/1.m4a"
    )["text"]
    msg = model.invoke(
        [
            HumanMessage(
                content="""
                你是一個管家
                根據使用者說的話來判斷是否要開燈,關燈,不動作或打開車庫門或關閉車庫門
                你只能回答'on'或'off'或'none'或'open'或'close'
                你可以同時決定多個裝置的狀態
                'on'代表開燈
                'off'代表關燈
                'none'代表不動作
                'open'代表打開車庫門
                'close'代表關閉車庫門
                不能回答其他的字串
                """
            ),
            HumanMessage(content=ans),
        ]
    )
    result = client.publish("singular", msg.content)
    result.wait_for_publish()  # 等待發布完成
    # 檢查發布是否成功
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)
