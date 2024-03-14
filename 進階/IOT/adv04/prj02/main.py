#########################匯入模組#########################
import network
#########################函式與類別定義#########################

#########################宣告與設定#########################
wlan = network.WLAN(network.STA_IF) #初始化ST初始化STA模式
ap = network.WLAN(network.AP_IF) #初始化AP模式
ap.active(False) #關閉AP模式
wlan.active(True) #開啟STA模式
#搜尋WIFI
wifi_list = wlan.scan()
print("scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])
wLSSID = "SingularClass"
wLPWD = "Singular#1234"
wlan.connect(wLSSID, wLPWD)
while not (wlan.isconnected): #等待成功
    pass
print("connect successfully", wlan.ifconfig()) #顯示成功的IP
#########################主程式#########################