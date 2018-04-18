#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "qA9" # Auf die ID aus dem BrickViewer ändern!

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4

# Callback function, wird aufgerufen wenn eine Taste gedrückt wird
def cb_button_pressed(button):
    print("Button gedrückt: " + str(button))

# Callback function, wird aufgerufen wenn eine Taste losgelassen wird
def cb_button_released(button):
    print("Button losgelassen: " + str(button))

# Ab hier fängt das "eigentliche Programm" an

ipcon = IPConnection() # Verbindung mit dem Master herstellen
lcd = BrickletLCD20x4(UID, ipcon) # Eine Verbindung zum LC-Display anlegen

ipcon.connect(HOST, PORT) # Verbinden

# Callbacks registrieren, sonst wird nichts beim drücken / loslassen aufgerufen!
lcd.register_callback(lcd.CALLBACK_BUTTON_PRESSED, cb_button_pressed)
lcd.register_callback(lcd.CALLBACK_BUTTON_RELEASED, cb_button_released)

input("Drücke ENTER zum beenden\n") # Auf irgendetwas warten, sonst habt Ihr keine Zeit etwas zu tun
ipcon.disconnect() # Die Verbindung wieder abbauen