#every landmark have a informaitons

#1: postaion ---------------> (x,y,z) > z is a depth in camera
#2: orentaion about wriest
#3: confogration  الشكل : about defreent between (MCP,PIP,TIP)


import cv2
import mediapipe as mp
import pyautogui as gui
import time

#initialize the mediapip hand detection and drawutils 
hand_mp=mp.solutions.hands


#create object

hands=hand_mp.Hands(
    static_image_mode=False,   
    max_num_hands=1, 

    min_detection_confidence=.6,
    min_tracking_confidence=.5
)



mp_drawing=mp.solutions.drawing_utils


#make list contane figures tips

tips_ids=[4,8,12,16,20]


# Variables to store the current gesture state and control actions


state = None  # Tracks the current playback state (e.g., Play or Pause)
Gesture = None  # Placeholder for gesture recognition (not used in this code)


#function to extract all landmarks

def finger_posation(image,results,hand_number=0):

    land_marks_list=[]


    if results.multi_hand_landmarks: #return none or [ [landmarks_of_hand1]]

        my_hand=results.multi_hand_landmarks[hand_number]

        #cordinaties return value of (x,y,z) as normalized mean from 0 to 1

        for id,cordinaties in enumerate(my_hand.landmark):

            h,w,ch=image.shape
            # Convert normalized coordinates to pixels
            cx,cy=int(cordinaties.x*w),int(cordinaties.y*h)

             # Append the landmark to the list

            land_marks_list.append([id,cx,cy])
    return land_marks_list


#parmeters for delay

last_action_time=0
delay=0



#start capture video

cap=cv2.VideoCapture(0)


while True:


    ret,frame=cap.read()

   

    #flip and convert frame to rgb

    img=cv2.cvtColor(cv2.flip(frame,1),cv2.COLOR_BGR2RGB)

    #lock writable to better the process of detection

    img.flags.writeable=False

    #detect hand 

    results=hands.process(img)

    # Make the frame writeable again

    img.flags.writeable=True

     # Convert RGB back to BGR for display

    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    #draw hand landmarks on the farme

    if results.multi_hand_landmarks:

        for hand_landmark in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                img #src
                , hand_landmark ,hand_mp.HAND_CONNECTIONS
            )


    #get landmarks posations

    lmlist=finger_posation(image=img,results=results)

    #check if landmrks detected

    if len(lmlist)!=0:

        #detected finger uo or down if UP=1 if Down=0

        fingers=[] #list containe all fingers excpet thump

        #check value of y at tips lanmrks by use for loop

        for id in range(1,5): #id is a [8,12,16,20]

            if lmlist[tips_ids[id]][2] < lmlist[tips_ids[id]-2][2]: 

                #mean fingre is up

                fingers.append(1)
            else:

                fingers.append(0) #fingre down

        fingers_up=fingers.count(1)

        print(f'fingers up is {fingers_up}')


        #controle and actions of kebord

        if fingers_up==4:

            state='play' #if 4 fingers up start cotrol


        if fingers_up==0 and state=='play':
 
            if time.time()-last_action_time > delay: #dealy 1 s


             state='pause'

             gui.press('space')

             print('space')
             last_action_time=time.time()


        if fingers_up==1: #one fingrue up 

            h,w,c=img.shape

            if lmlist[8][1] < w//2: #check index figure

                if time.time()-last_action_time > 1.5:
                 

                 print('left key')

                 gui.press('left')
                 last_action_time=time.time()


                

            if lmlist[8][1] >w//2:
                if time.time()-last_action_time > 1.5:
                 print('right key')

                 gui.press('right')
                 last_action_time=time.time()


        if fingers_up==3:

            if lmlist[14][1] < w//2:

                if time.time()-last_action_time > 2.5:

                 print('MUTE') 
                 gui.press('m')
                 last_action_time=time.time() 


            if lmlist[14][1] > w//2:
                if time.time()-last_action_time >  2.5:
 
                 print('full screen')

                 gui.press('f')
                 last_action_time=time.time()

        if fingers_up==2:

            if lmlist[10][2] < h//2:

                if time.time()-last_action_time > .9:

                 print('up key') 
                 gui.press('up')
                 last_action_time=time.time()


            if lmlist[10][2] > h//2:
                if time.time()-last_action_time >  .9:
 
                 print('down key')

                 gui.press('down')
                 last_action_time=time.time()         


    h,w,c=img.shape
    img=cv2.line(img,(w//2,0),(w//2,h),(120,230,255),5)
    img=cv2.line(img,(0,h//2),(w,h//2),(255,120,77),5)  
   

    cv2.imshow('YOUTUBE controler',img)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break


cap.release()

cv2.destroyAllWindows()
 












        

    

                




            



    
    

   







