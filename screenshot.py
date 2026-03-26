'''
Coded by: BadgerSnacks
'''

import mss
import numpy
import cv2
import time
import os
from datetime import datetime

current_time = datetime.now().strftime("%m-%d-%Y %H-%M-%S")
directory = "screenshots" + current_time
os.makedirs(directory, exist_ok=True)

def screenshots(total_screenshots: int, monitor: int):
    with mss.mss() as sct:
        monitor_var = sct.monitors[monitor]
        count = 0
        print("Capturing screenshots...")
        while count < total_screenshots:
            screenshot = numpy.array(sct.grab(monitor_var))
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

            cv2.imwrite(f"{directory}/screenshot{count:04d}.png", screenshot)

            count += 1

            time.sleep(1)
    print("Finished capturing screenshots")