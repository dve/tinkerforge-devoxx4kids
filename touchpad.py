#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "pcf" # Auf die ID aus dem BrickViewer ändern!

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_multi_touch import BrickletMultiTouch


# Callback function for touch state callback
def cb_touch_state(state):
    s = ""

    if state & (1 << 12):
        s += "In proximity, "

    if (state & 0xfff) == 0:
        s += "No electrodes touched"
    else:
        s += "Electrodes "
        for i in range(12):
            if state & (1 << i):
                s += str(i) + " "
        s += "touched"

    print(s)
    
ipcon = IPConnection() # Verbindung mit dem Master herstellen
mt = BrickletMultiTouch(UID, ipcon) # Verbindung zum Touchpad anlegen

ipcon.connect(HOST, PORT) # Verbinden

mt.recalibrate() # Rekalibrieren, sonst wird das Touchpad nicht sauber ausgewertet

# Callback funktion anmelden
mt.register_callback(mt.CALLBACK_TOUCH_STATE, cb_touch_state)

input("Drücke ENTER zum beenden\n") # Auf irgendetwas warten, sonst habt Ihr keine Zeit etwas zu tun
ipcon.disconnect()  # Die Verbindung wieder abbauen