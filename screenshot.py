'''
Coded by: BadgerSnacks
'''

#Imports needed for the screenshot functions to run.
import mss
import numpy
import cv2
import time
import os
from datetime import datetime

current_time = datetime.now().strftime("%m-%d-%Y %H-%M-%S") #Creates variable of the current time the script is accessed
directory = "screenshots" + current_time #Creates new directory with the current time
os.makedirs(directory, exist_ok=True) #checks to see if the directory already exists

#Function to grab a set number of screenshots on a specific monitor
def screenshots(total_screenshots: int, monitor: int):
    with mss.mss() as sct: #Creates a multi screenshot object named sct
        monitor_var = sct.monitors[monitor] # creates a new monitor variable based on the provided argument from the function
        count = 0 #Variable for counting up to set number of screenshots.
        print("Capturing screenshots...") #Output to the terminal to show the function is working
        while count < total_screenshots: #Loops a set number of times based on provided arguments to the function
            screenshot = numpy.array(sct.grab(monitor_var)) #Creates a numpy array based on the screen grab of the monitor passed
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR) #Converts the screenshot from BGRA to BGR removing alpha channel

            cv2.imwrite(f"{directory}/screenshot{count:04d}.png", screenshot) #Uses cv2 to save the screenshot to the folder with the count appended

            count += 1 #Updates the count every loop

            time.sleep(1) #The wait time set between screenshots
    print("Finished capturing screenshots") #Output to the terminal to let user know the function has finished