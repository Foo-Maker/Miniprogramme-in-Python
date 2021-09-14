#!/bin/python3

import requests
import os
from threading import Thread 
import time 

print("Starte Programm…")
print(f"")
print(f"Mit der Eingabetaste kann das Programm abgebrochen werden!")
print()

i = False
install = False
uhrzeit = ""

def listen():
    global i
    input()
    i = True

listener = Thread(target=listen)
listener.start()


while not i:
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    uhrzeit = time_string
    r = requests.get("https://linux.kite.com")
    """
    if r.status_code == 3404:
        print(f"{time_string} kommt 404")
        time.sleep(2)
        continue
    elif r.status_code == 3502:
        print(f"{time_string} kommt 502")
        time.sleep(2)
        continue
    el
    """
    if r.status_code == 200:
        os.system("/opt/kite/kite-installer update")
        print(r.status_code)
        print(type(r))
        i = False
        install = True
    else:
        print(f"{uhrzeit} Wir haben einen {r.status_code} Fehler")
        time.sleep(2)

listener.join()

if install:
    print(f"Kite ist um {uhrzeit} installiert worden")
else:
    print(f"Es wurde um {uhrzeit} abgebrochen")
