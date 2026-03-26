'''
Coded by: BadgerSnacks
'''
if __name__ == '__main__':

    import subprocess
    import sys
    import os
    import time
    import screenshot

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
    install_package("keyboard")

    #imports that need to be installed first
    import keyboard

    #global variables
    running = True

    # text format variables !!! ALWAYS CLOSE STRING WITH RESET !!!
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RESET = "\033[0m"

    while running:
        print("Enter X to exit.")
        print("Enter 1 to start screenshots")

        user_input = input()

        match user_input.lower().strip():
            case "x":
                running = False
            case "1":
                screenshot_count = input("Number of screenshots: ")
                try:
                    screenshot_count = int(screenshot_count)
                except ValueError:
                    print(f"{RED}Please enter a number for screenshots!{RESET}")
                    continue
                monitor = input("Monitor number: ")
                try:
                    monitor = int(monitor)
                except ValueError:
                    print(f"{RED}Please enter a number for monitor!{RESET}")
                    continue
                screenshot.screenshots(screenshot_count, monitor)