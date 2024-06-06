import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.2)
from langchain_core.messages import HumanMessage

while True:
    ans = input("請輸入想跟AI說的話:")
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
    print(msg.content)
