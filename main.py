import pyautogui
from random import uniform
from pynput.keyboard import *
import time

# TODO: Ryanify code
# TODO: select button to include shift/ctrl/alt+hotkey combinations 

# Delay Settings
startCPS = 6
CPS = 7
startDelay = 1/startCPS
goalDelay = 1/CPS


# Hotkey Settings
hotkey = KeyCode.from_char('r')

# Default Values
pause = True
running = True
startSwitch = True


def on_press(key):
    """Function that activates when the hotkey is pressed"""
    global running, pause
    if pause and key == hotkey:
        startSwitch = True
        pause = False
        print("--> Started")
    elif key == hotkey:
        pause = True
        startSwitch = True
        print("--> Paused")
    else:
        pass
    

def display_controls():
    print("-"*20)
    print("--Settings--")
    print("CPS: ", CPS, "\nDelay: ", round(goalDelay, 4), "sec")
    print("--Controls--")
    print("Hotkey = R")
    print("-"*20)



def main():
    delay = startDelay
    switch = True
    startSwitch = True
    delayRange = 0.5


    listener = Listener(on_press=on_press)
    listener.start()
    display_controls()
    

    while running:        
        print(pyautogui.position())
        # pyautogui.click(pyautogui.position())
        # pyautogui.PAUSE = delay
        
        time.sleep(0.1)

    listener.stop()


if __name__ == "__main__":
    main()