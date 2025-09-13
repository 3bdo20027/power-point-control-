from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ppt_Control import next_slide, previous_slide, start_laser, click, draw_mode, erase_drawing, stop_drawing
from gestures import open_ppt
import os

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
    if not os.path.exists(file.path):
        raise HTTPException(status_code=404, detail="PPT file not found")
    open_ppt(file.path)
    return {"message": f"Presentation {file.path} opened"}

@app.post("/ppt/next")
def api_next_slide():
    next_slide()
    return {"message": "Moved to next slide"}

@app.post("/ppt/prev")
def api_prev_slide():
    previous_slide()
    return {"message": "Moved to previous slide"}

@app.post("/ppt/click")
def api_click():
    click()
    return {"message": "Click performed"}

@app.post("/ppt/draw/start")
def api_draw():
    draw_mode()
    return {"message": "Drawing mode activated"}

@app.post("/ppt/draw/stop")
def api_stop_draw():
    stop_drawing()
    return {"message": "Drawing stopped"}

@app.post("/ppt/draw/erase")
def api_erase():
    erase_drawing()
    return {"message": "Erased drawings"}

@app.post("/ppt/laser")
def api_laser(pos: Position):
    start_laser(pos.x, pos.y)
    return {"message": f"Laser activated at ({pos.x}, {pos.y})"}
