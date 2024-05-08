import pyautogui
from random import uniform
from pynput.keyboard import *
import time

# TODO: Ryanify code
# TODO: select button to include shift/ctrl/alt+hotkey combinations 



# Hotkey Settings
hotkey = KeyCode.from_char('r')


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
    print("-"*20)



def main():
    running = True

    listener = Listener(on_press=on_press)
    listener.start()
    display_controls()
    
    time.sleep(5) 
    while running:    
        # print(pyautogui.position())
        time.sleep(1.5)
        pyautogui.click(pyautogui.position(1739, 181))
        time.sleep(0.5)
        pyautogui.click(pyautogui.position(1739, 181))
        # pyautogui.PAUSE = delay
        
        time.sleep(1.5)
        pyautogui.click(pyautogui.position(788, 193))
        time.sleep(0.5)
        pyautogui.click(pyautogui.position(788, 193))
        
    listener.stop()


if __name__ == "__main__":
    main()