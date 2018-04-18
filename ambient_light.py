#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "mbw" # Auf die ID aus dem BrickViewer ändern!

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ambient_light import BrickletAmbientLight

# Callback function, wird aufgerufen wenn die Helligkeit einen bestimmten Wert
# (threshold) übersteigt
def cb_illuminance_reached(illuminance):
    print("Helligkeit: " + str(illuminance/10.0) + " lx")
    print("Wo ist meine Sonnebrille!")
    
ipcon = IPConnection() # Verbindung mit dem Master herstellen
al = BrickletAmbientLight(UID, ipcon) # Verbindung zum Lichtsensor anlegen

ipcon.connect(HOST, PORT) # Verbinden

# Callback funktion anmelden
al.register_callback(al.CALLBACK_ILLUMINANCE_REACHED, cb_illuminance_reached)

# Schwellwert festlegen "größer als 200 lx"
al.set_illuminance_callback_threshold(">", 200*10, 0)

input("Drücke ENTER zum beenden\n") # Auf irgendetwas warten, sonst habt Ihr keine Zeit etwas zu tun
ipcon.disconnect()  # Die Verbindung wieder abbauen