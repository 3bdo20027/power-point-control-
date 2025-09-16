import pyautogui
import time

from get_path import pick_file
import os



def open_file():
    file_path=pick_file()

    if file_path:

        try:

            os.startfile(file_path)

        except Exception as ex:

            print(f'Error : {ex}')
    else:
        print('No file selected')



def next_slide():
    
    pyautogui.press("right")
    

def previous_slide():
    """Go to previous slide"""
    pyautogui.press("left")
   

def start_laser():
    """Activate laser pointer and move to position"""
    pyautogui.hotkey("ctrl", "l")
   

def stop():
    
    pyautogui.press('esc')
   

def draw_mode():
    """Enable drawing mode (Ctrl+P in PowerPoint)"""
    pyautogui.hotkey("ctrl", "p")

def erase_drawing():
    """Erase drawings (Ctrl+E in PowerPoint)"""
    pyautogui.hotkey("ctrl", "e")


