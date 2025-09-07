import cv2



def get_capture():

    cap=cv2.VideoCapture(0)

    return cap



def get_farme(cap):

    sucsess,frame=cap.read()  #read frames

    if not sucsess:

        return print('Camera Not Found')

    frame=cv2.cvtColor(cv2.flip(frame,1),cv2.COLOR_BGR2RGB)

    return frame  #return RGB frame

    