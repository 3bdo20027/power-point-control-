from camera_setup import get_capture,get_farme
from hand_deyection import process_lm,drawing_landmarks,finger_posation,fingures_state
from gestrues import gestrue_recognization
import pyautogui
import time
import autopy
import numpy as np

last_action_time=0


laser_on=False
smothing=7
gestrue=None

frame_r=100



pre_x,pre_y=0,0

c_x,c_y=0,0

screen_w,screen_h=pyautogui.size()
import cv2

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
           
            '''          
            
        
             
            if fiengures==[0,1,1,1,0]:
               #draw rectangle about region for laserdetection

                cv2.rectangle(frame, (frame_r, frame_r), (w - frame_r, h - frame_r),(255, 0, 255), 2)
                #pyautogui.hotkey('ctrl','l')

                #x,y postions from camera to screen 

                scale=autopy.screen.scale()
                screen_w,screen_h=autopy.screen.size()


                x=np.interp(lm_list[12][1],(frame_r,w-frame_r),(0,screen_w))
                y=np.interp(lm_list[12][2],(frame_r,h-frame_r),(0,screen_h))

                #x=max(1,min(x,screen_w-1))
                #y=max(1,min(y,screen_h-1))


                c_x=pre_x+(x-pre_x)/smothing
                c_y=pre_y+(y-pre_y)/smothing

                autopy.mouse.move(c_x,c_y)
                cv2.circle(frame, (lm_list[12][1], lm_list[12][2]), 13, (255, 255, 0), cv2.FILLED)
                pre_x,pre_y=c_x,c_y'''





            

                       



         #calc FPS
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


