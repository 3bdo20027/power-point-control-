from camera_setup import get_capture,get_farme
from hand_deyection import process_lm,drawing_landmarks,finger_posation,fingures_state
from gestrues import gestrue_recognization
import pyautogui
import time
import autopy
import numpy as np
import cv2




last_action_time=0
gestrue=None









def main():
    cap=get_capture()

    while True:
        global laser_on,pre_x,pre_y,c_x,c_y,smothing,frame_r,screen_h,screen_w,gestrue
        frame=get_farme(cap)

        results=process_lm(frame)
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:

            frame=drawing_landmarks(img=frame,results=results)

        
        lm_list,hand_lable=finger_posation(image=frame,results=results) #extract all landmarks posations [id,x,y]

        if len(lm_list)!=0:

            h,w,ch=frame.shape

            fiengures=fingures_state(lmlist=lm_list,hand_lable=hand_lable)

            fiengures_up=fiengures.count(1)

            #print(f'now fingures up is : {fiengures} for {hand_lable} hand')

            gestrue=gestrue_recognization(lm_list=lm_list,fingurs_up=fiengures,frame=frame)
           




            

                       



         #calc FPS (frame for second)
        global last_action_time
        current_time=time.time()
        fps=1/(current_time-last_action_time)
        last_action_time=current_time


        
        frame=cv2.putText(frame,f'{int(fps)} FPS',(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        frame=cv2.putText(frame,gestrue,(370,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
        

        cv2.imshow('main programe',frame)  


        if cv2.waitKey(2) & 0xff==ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
    

if __name__=="__main__":
    main()


