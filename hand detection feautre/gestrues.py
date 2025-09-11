import pyautogui
import time
import autopy
import numpy as np
import cv2
from pynput.mouse import Button,Controller




state=None
gestrue=None 

mouse=Controller() #to click left on mouse and move mouse

#for delay and increase process 
last_action_time=0
delay=0


#paramiters for move mouse by aytopy or pynput library
smothing=7
frame_r=100
pre_x,pre_y=0,0 #last postion of mouse 
c_x,c_y=0,0 #current posation of mouse

#parmiters for check states of gestrues
laser_check=False
draw_check=False
is_drawing=False
erase_check=False

#get screen width and hight
screen_w,screen_h=pyautogui.size()

def gestrue_recognization(lm_list,fingurs_up,frame):

    global last_action_time,state,draw_check,mouse,is_drawing,erase_check,gestrue
    global pre_x,pre_y,laser_check,c_x,c_y,smothing,frame_r,screen_h,screen_w

    h,w,ch=frame.shape
    
    #use [0,1,1,1,1] mean all fingures up expect thump is down
     
    if state=='slide show'   and laser_check==False and draw_check==False and erase_check==False:
      

        if fingurs_up==[0,1,1,1,1]:
            if time.time()-last_action_time > 5:

                state='end slid show'
                print(state)
                pyautogui.press('f5')
                gestrue='end slid show'
                last_action_time=time.time()

                







    if fingurs_up==[0,1,1,1,1] and laser_check==False and draw_check==False and erase_check==False:
        if time.time()-last_action_time > 5:
            
            state='slide show'
            gestrue='slide show'
            print(state)
            pyautogui.press('f5')
            last_action_time=time.time()


   

     #logic of next slide gestrue
    
    if fingurs_up==[0,1,0,0,0] and state=='slide show' and laser_check==False and draw_check==False:

        if time.time()-last_action_time > 1.5:

            print('next slide')
            last_action_time=time.time()
            pyautogui.press('right')
            gestrue='next slide'



     #logic of next pervious gestrue
     
    elif fingurs_up==[0,1,1,0,0] and state=='slide show' and laser_check==False and draw_check==False:

        if time.time()-last_action_time > 1.5:

            print('last slide')
            last_action_time=time.time()
            pyautogui.press('left')
            gestrue='privous slide'


     #logic of start laser gestrue
    
    if fingurs_up==[1,1,0,0,0] and draw_check==False and state=='slide show' and erase_check==False:
            
            #draw rectangle about region for laser detection
            cv2.rectangle(frame, (frame_r, frame_r), (w - frame_r, h - frame_r),(255, 0, 255), 2)
            
            if not laser_check:

            
                pyautogui.hotkey('ctrl','l')

                laser_check=True
                print('start laser')
                gestrue='laser mode on'


            #x,y postions from camera to screen 
            screen_w,screen_h=autopy.screen.size()


            #convert x,y cordianits of frame camera to x,y for screen
            #من الاخر بيحول الاحدثيات بتاعت الكاميرا الاحثيات ممازويه للحجم الشاشه بتاعتي عشان لما احرك الماوس
            x=np.interp(lm_list[8][1],(frame_r,w-frame_r),(0,screen_w))
            y=np.interp(lm_list[8][2],(frame_r,h-frame_r),(0,screen_h))

            #clamp x,y if get error say out of bounds

            #x=np.clip(x,3,screen_w-10) 
            #y=np.clip(y,3,screen_h-10)

            
            c_x=pre_x+(x-pre_x)/smothing
            c_y=pre_y+(y-pre_y)/smothing

            #autopy.mouse.move(c_x,c_y) 

            mouse.position=(c_x,c_y)
            cv2.circle(frame, (lm_list[8][1], lm_list[8][2]), 13, (255, 255, 0), cv2.FILLED)
            pre_x,pre_y=c_x,c_y
    
    #logic of End laser mode
    elif fingurs_up==[1,1,1,1,1] and laser_check:
        
        
          
          pyautogui.hotkey('ctrl','a')
          
          laser_check=False
          print('stop laser')
          gestrue='laser mode off'


    #------------------------------------------------------------------>
    
    #logic of statr drawing mode 

    if fingurs_up==[0,1,1,1,0] and laser_check==False and state=='slide show' and erase_check==False:
            #draw rectangle about region of drawing 

            cv2.rectangle(frame, (frame_r, frame_r), (w - frame_r, h - frame_r),(255, 0, 255), 2)
            if not draw_check:

            
                pyautogui.hotkey('ctrl','p')
                draw_check=True
                print('start drawing')
                gestrue='start drawing'


            #x,y postions from camera to screen 
            screen_w,screen_h=autopy.screen.size()


            #mouse posations
            x=np.interp(lm_list[12][1],(frame_r,w-frame_r),(0,screen_w))
            y=np.interp(lm_list[12][2],(frame_r,h-frame_r),(0,screen_h))

            #clamp x,y

            #x=np.clip(x,3,screen_w-10)
            #y=np.clip(y,3,screen_h-10)


            c_x=pre_x+(x-pre_x)/smothing
            c_y=pre_y+(y-pre_y)/smothing

            
                
                 
                 

            #autopy.mouse.move(c_x,c_y)
            
            mouse.position=(c_x,c_y)

            
            mouse.press(Button.left) #click left on mouse


            #draw circle on fingure tip          
            cv2.circle(frame, (lm_list[12][1], lm_list[12][2]), 13, (255, 255, 0), cv2.FILLED)
           
            pre_x,pre_y=c_x,c_y

   
     #logic to end drawing mode
    if fingurs_up==[1,1,1,1,1] and draw_check and erase_check==False and laser_check==False:
         
        draw_check=False
        mouse.release(Button.left)
        pyautogui.hotkey('ctrl','a')
        print('stop drawing')
        gestrue='stop drawing'

    #logic to statr use erse      
    elif fingurs_up==[1,1,0,0,1] and draw_check==False and not erase_check and laser_check==False:
        
        
        
        draw_check=False
        mouse.release(Button.left)


        #draw rectangle about region for laserdetection

        cv2.rectangle(frame, (frame_r, frame_r), (w - frame_r, h - frame_r),(255, 0, 255), 2)
      

        
        pyautogui.hotkey('ctrl','e')
        erase_check=True
        print('start erase')
        gestrue='start erase'
        
       


        #x,y postions from camera to screen 
        screen_w,screen_h=autopy.screen.size()


    if erase_check:



            x=np.interp(lm_list[8][1],(frame_r,w-frame_r),(0,screen_w))
            y=np.interp(lm_list[8][2],(frame_r,h-frame_r),(0,screen_h))

                #clamp x,y

                #x=np.clip(x,3,screen_w-10)
                #y=np.clip(y,3,screen_h-10)


            c_x=pre_x+(x-pre_x)/smothing
            c_y=pre_y+(y-pre_y)/smothing

                
                    
                    
                    

            #autopy.mouse.move(c_x,c_y)
            mouse.position=(c_x,c_y)
            if time.time()-last_action_time > .5:
                 
               mouse.press(Button.left)


            
            cv2.circle(frame, (lm_list[8][1], lm_list[8][2]), 13, (255, 255, 0), cv2.FILLED)
            pre_x,pre_y=c_x,c_y

    #logic of end useing erse  
    if fingurs_up==[0,0,0,0,0] and erase_check:
            
            print('stop  erase')
            gestrue='stop  erase'
            mouse.release(Button.left)

            erase_check=False

        

        


        
          
        



    return gestrue

     #------------------------------------------------------------------>
    #erase
'''

    if fingurs_up==[1,1,1,1,1] and laser_check==False and state=='slide show':
            #draw rectangle about region for laserdetection

            cv2.rectangle(frame, (frame_r, frame_r), (w - frame_r, h - frame_r),(255, 0, 255), 2)
            if not erase_check:

            
                pyautogui.hotkey('ctrl','e')
                erase_check=True
                print('start erase')


            #x,y postions from camera to screen 
            screen_w,screen_h=autopy.screen.size()



            x=np.interp(lm_list[16][1],(frame_r,w-frame_r),(0,screen_w))
            y=np.interp(lm_list[16][2],(frame_r,h-frame_r),(0,screen_h))

            #clamp x,y

            #x=np.clip(x,3,screen_w-10)
            #y=np.clip(y,3,screen_h-10)


            c_x=pre_x+(x-pre_x)/smothing
            c_y=pre_y+(y-pre_y)/smothing

            
                
                 
                 

            #autopy.mouse.move(c_x,c_y)
            mouse.position=(c_x,c_y)
            
            mouse.press(Button.left)


          
            cv2.circle(frame, (lm_list[16][1], lm_list[16][2]), 13, (255, 255, 0), cv2.FILLED)
            pre_x,pre_y=c_x,c_y
    elif fingurs_up==[0,0,0,0,0] and erase_check:
        
        
        mouse.release(Button.left)
        erase_check=False

        


        
          
        pyautogui.hotkey('ctrl','a')
        print('stop erse')

    
    
    
'''


         

         

               
             


       

      
          

           
                

        
          
          
            







   

    
     
    
    






   

    
 

        





