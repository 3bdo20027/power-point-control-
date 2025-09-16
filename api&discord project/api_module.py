from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ppt_Control import open_file,next_slide, previous_slide, start_laser, draw_mode, erase_drawing,stop
import os
import time
import pyautogui



last=0


app = FastAPI()

class PPTFile(BaseModel):
    path: str

class Position(BaseModel):
    x: int
    y: int


@app.get("/")
def root():

    return {"Hello": "PPT Gesture Control API"}



@app.post("/ppt/open")
def open_presentation(file: PPTFile):
    global last
    if not os.path.exists(file.path): #check if path exist 

        raise HTTPException(status_code=404, detail="File not found")
    try:
       
        os.startfile(file.path) #open file
        time.sleep(2)
        
        pyautogui.press('f5') #run slide show mode
            

        
        return {"message": f"Presentation {file.path} opened"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))



@app.post("/ppt/next") 

def api_next_slide():

    next_slide()
    return {"message": "Moved to next slide"}

@app.post("/ppt/prev")
def api_prev_slide():

    previous_slide()
    return {"message": "Moved to previous slide"}

@app.post("/ppt/stop")
def api_click():
    stop()
    return {"message": "Stoped"}

@app.post("/ppt/draw")
def api_draw():
    draw_mode()
    return {"message": "Drawing mode activated"}

@app.post("/ppt/stop")
def api_stop():
    stop()
    return {"message": "stopped"}

@app.post("/ppt/erase")
def api_erase():
    erase_drawing()
    return {"message": "Erased drawings"}

@app.post("/ppt/laser")
def api_laser():
    pyautogui.hotkey('ctrl','l')
    return {"message": f"Laser activated )"}
