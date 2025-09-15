import time
import pyautogui
import subprocess
import os

prev_x, prev_y = 0, 0

from ppt_Control import next_slide, previous_slide, start_laser, click, draw_mode, erase_drawing, stop_drawing

# --- فتح ملف ppt تلقائيًا ---
def open_ppt(path):
    # فتح العرض التقديمي مباشرة في LibreOffice Impress
    subprocess.Popen(['libreoffice', '--show', path])
    time.sleep(3)  # وقت لإتاحة فتح النافذة

# --- تفعيل نافذة العرض للتأكد أن pyautogui يرسل الضغطات صحيحة ---
def activate_ppt_window():
    os.system('xdotool search --name "LibreOffice" windowactivate --sync')
    time.sleep(0.3)

def recognize_gesture(index_pos, thumb_pos, frame_shape, fingers=None):
    global prev_x, prev_y
    gesture = None

    if not index_pos or not thumb_pos:
        return None

    h, w = frame_shape[:2]

    # تفعيل نافذة العرض قبل أي فعل
    activate_ppt_window()

    # المسافة بين الإبهام والسبابة
    dist = ((index_pos[0]-thumb_pos[0])**2 + (index_pos[1]-thumb_pos[1])**2) ** 0.5

    # --- Gestures ---
    if dist < 40:
        gesture = "click"
        click()

    elif index_pos[0] - prev_x > 80:
        gesture = "swipe_right"
        next_slide()

    elif prev_x - index_pos[0] > 80:
        gesture = "swipe_left"
        previous_slide()

    elif index_pos[1] < h // 3:
        gesture = "laser"
        start_laser(index_pos[0]*2, index_pos[1]*2)

    # --- Drawing & Erasing using finger states ---
    if fingers:
        if fingers[1] == 1 and fingers[2] == 1 and sum(fingers) == 2:  # index + middle
            gesture = "draw"
            draw_mode()

        elif sum(fingers) == 0:  # fist
            gesture = "erase"
            erase_drawing()

        elif fingers[0] == 1 and sum(fingers) == 1:  # only thumb up
            gesture = "stop_drawing"
            stop_drawing()

    prev_x, prev_y = index_pos
    return gesture
