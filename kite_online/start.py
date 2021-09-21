#!/bin/python3

import requests
import os
from threading import Thread 
import time 

os.system("clear")
print("Starte Programm…")
print(f"")
print(f"Mit der Eingabetaste kann das Programm abgebrochen werden!")
print()

i = False
install = False
uhrzeit = ""
history = 0

def listen():
    global i
    input()
    i = True

listener = Thread(target=listen)
listener.start()

def status_toggle(bar):
    if bar[1] != history:
        print(f"{bar[0]} Wir haben einen {bar[1]} Fehler")
        return bar
    else:
        pass



def chek():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    uhrzeit = time_string
    r = requests.get("https://linux.kite.com")
    if r.status_code == 200:
        os.system("/opt/kite/kite-installer update")
        print(r.status_code)
        print(type(r))
        i = False
        install = True
        return 200
    else:
        sc = r.status_code
        time.sleep(2)
        listener.join()
        return uhrzeit, sc
    listener.join()

while True: 
    try:
        foo = chek()
        status_toggle(foo)
        history = foo[1]
    except:
        time.sleep(10)

listener.join()

if install:
    print(f"Kite ist um {uhrzeit} installiert worden")
else:
    print(f"Es wurde um {uhrzeit} abgebrochen")
