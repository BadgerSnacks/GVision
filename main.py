'''
By BadgerSnacks
'''

import subprocess
import sys

# Function to install missing packages.
def install_package(package):
    try:
        __import__(package) # checks to see if the package can be import into the program
    except ImportError: # runs if program cannot be imported
        print(f"Installing {package}...") # printline to show the user what is being installed
        subprocess.check_call([sys.executable, "-m", "pip", "install", package]) # sends this command to the terminal to install with pip, will not work if user does not have pip

install_package("mss")
install_package("numpy")
install_package("cv2")
#install_package("ultralytics")

import mss
import numpy
import cv2
#import ultralytics
#from ultralytics import YOLO

with mss.mss() as sct:
    screenshot = sct.grab(sct.monitors[1])

    cv2.imwrite("screenshot.png", screenshot)