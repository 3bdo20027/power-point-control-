import pyautogui
import time

def next_slide():
    """Go to next slide"""
    pyautogui.press("right")
    

def previous_slide():
    """Go to previous slide"""
    pyautogui.press("left")
   

def start_laser(x, y):
    """Activate laser pointer and move to position"""
    pyautogui.hotkey("ctrl", "l")
    pyautogui.moveTo(x, y)

def click():
    """Simulate click (advance animation)"""
    pyautogui.click()
   

def draw_mode():
    """Enable drawing mode (Ctrl+P in PowerPoint)"""
    pyautogui.hotkey("ctrl", "p")

def erase_drawing():
    """Erase drawings (Ctrl+E in PowerPoint)"""
    pyautogui.hotkey("ctrl", "e")

def stop_drawing():
    """Switch back to normal pointer (Ctrl+A)"""
    pyautogui.hotkey("ctrl", "a")
