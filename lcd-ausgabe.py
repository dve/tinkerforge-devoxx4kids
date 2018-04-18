#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "qA9" # Auf die ID aus dem BrickViewer ändern!

from tinkerforge.ip_connection import IPConnection # den Befehl für den Master-Brick bekannt machen
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4 # den Befehl für das LC-Display bekannt machen

# Ab hier fängt das "eigentliche Programm" an

ipcon = IPConnection() # Verbindung mit dem Master herstellen
lcd = BrickletLCD20x4(UID, ipcon) # Eine Verbindung zum LC-Display anlegen

ipcon.connect(HOST, PORT) # Verbinden

lcd.clear_display() # Bildschrim leer machen

lcd.backlight_on() # es werde Licht!

lcd.write_line(0, 0, "Hallo!") # Etas ausgeben (Zeile, Spalte, Text)

input("Drücke ENTER zum beenden\n") # Auf irgendetwas warten, sonst habt Ihr keine Zeit etwas zu tun

lcd.backlight_off() # der Letzte macht das Licht aus!

ipcon.disconnect() # Die Verbindung wieder abbauen