import network
from umqtt.simple import MQTTClient
import sys
from machine import Pin, PWM


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD3(self):
        return self._SDD3

    @property
    def SDD2(self):
        return self._SDD2


class wifi:
    def __init__(self, ssid=None, password=None):
        """

        初始化wifi模組
        ssid:wifi
        password:wifi密碼
        """
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)
        self.ssid = ssid
        self.password = password
        self.ap_active = False
        self.sta_active = False
        self.ip = None

    def setup(self, ap_active=False, sta_active=False):
        """
        設定wifi模組
        ap_active:是否開啟AP模式
        sta_active:是否開啟STA模式
        使用方法:
        wi.setup(ap_active=True|faLSE,sta_active=True|False)
        """
        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        """
        搜尋WIFI
        傳回:WIFI列表

        使用方法:
        wi.scan()
        """
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("scan result")
            for wifi in wifi_list:
                print(wifi[0])
        else:
            print("sta mode is not active")

    def connect(self, ssid=None, password=None) -> bool:
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password

        if not self.sta_active:
            print("sta 模式未啟用")
            return False

        if ssid is None or password is None:
            print("WIFI名稱或密碼未設定")
            return False

        if self.sta_active:
            self.sta.connect(ssid, password)
            while not self.sta.isconnected():
                pass
            self.ip = self.sta.ifconfig()[0]
            print("connected to wifi", "IP:", self.ip)
            return True


class MQTT:
    def __init__(self, mqttClientID, mq_server, mqtt_username, mqtt_password) -> None:
        self.mq_server = mq_server
        self.mqttClientID = mqttClientID
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.mqClient0 = MQTTClient(
            mqttClientID,
            mq_server,
            user=mqtt_username,
            password=mqtt_password,
            keepalive=30,
        )

    def connect(self):
        try:
            self.mqClient0.connect()
        except:
            sys.exit()
        finally:
            print("connected mqtt server")

    def subscribe(self, topic, on_message):
        self.mqClient0.set_callback(on_message)  # 設定接收訊息時要呼叫的函式
        self.mqClient0.subscribe(topic)  # 設定想訂閱的主題

    def check_msg(self):
        self.mqClient0.check_msg()  # 等待以訂閱的主題發送資料
        self.mqClient0.ping()  # 持續確認是否還保持連線

    def publish(self, topic: str, msg: str):
        """
        發布訊息

        topic:主題
        msg:訊息

        使用方法:
        mqtt.publish("topic", "msg")
        """
        topic = topic.encode("utf-8")
        msg = msg.encode("utf-8")
        self.mqClient0.publish(topic, msg)


class servo:
    def __init__(self, sg_Pin):
        """
        伺服馬達類別用於控制伺服馬達
        屬性:
        sg_pin:伺服馬達的引脚sg(PWM): 伺服馬達

        方法:
            angle(angle: int): 控制伺服馬達的角度
        """
        self.sg = PWM(Pin(sg_Pin), freq=50)

    def angle(self, angle: int):
        """
        控制伺服馬達的角度
        參數:
        angle(int):馬達轉動角度
        """
        if 0 <= angle <= 180:
            self.sg.duty(int(1023 * (0.5 + angle / 90) / 20))
