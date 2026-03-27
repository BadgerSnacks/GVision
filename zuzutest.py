'''
Coded by: BadgerSnacks
'''

import serial
import time

ser = serial.Serial('COM3', 9600, timeout=5)
time.sleep(2)

def hold_key(key, duration_ms):
    cmd = f"HOLD_{key.upper()}:{duration_ms}\n"
    ser.write(cmd.encode())
    response = ser.readline().decode().strip()
    print(f"ZuZu says: {response}")

hold_key("RIGHT", 2000)

ser.close()