import mediapipe as mp
import cv2


#setup hand detection module

mp_hands=mp.solutions.hands

#intialize the object 

hands=mp_hands.Hands(

    static_image_mode=False,  #use for process image not streaming
    max_num_hands=1,   #number of hands uses
    min_detection_confidence=.5,
    min_tracking_confidence=.5,

)


#setup hand drawing  module

mp_drawing=mp.solutions.drawing_utils

#make list for tips of fingeurs

tips=[4,8,12,16,20]



#process land marks function

def process_lm(src):


    #src.flags.writeable=False  #to increase process speed

    results=hands.process(src)

    #src.flags.writeable=True

    return results


#drawing landmarks function

def drawing_landmarks(img,results):

    for hand_marks in results.multi_hand_landmarks:

        mp_drawing.draw_landmarks(img,hand_marks,mp_hands.HAND_CONNECTIONS)
    return img





#function to extract all landmarks

def finger_posation(image,results,hand_number=0):

    land_marks_list=[]
    hand_lable=None


    if results.multi_hand_landmarks: #return none or [ [landmarks_of_hand1]]

        my_hand=results.multi_hand_landmarks[hand_number]

        #check the hand is right or left

        hand_lable=results.multi_handedness[0].classification[0].label


        #cordinaties return value of (x,y,z) as normalized mean from 0 to 1

        for id,cordinaties in enumerate(my_hand.landmark):

            h,w, ch=image.shape
           # Convert normalized coordinates to pixels
            cx,cy=int(cordinaties.x*w),int(cordinaties.y*h)

             # Append the landmark to the list

            land_marks_list.append([id,cx,cy])



    return land_marks_list,hand_lable


def fingures_state(lmlist,hand_lable,tips=[4,8,12,16,20]):


    fingures_up_list=[0,0,0,0,0]



    for finger in range(1,5):

        if lmlist[tips[finger]][2] < lmlist[tips[finger]-2][2]: #compare distance between tips and pips in lanmarks at y-axis

            fingures_up_list[finger]=1 #fingure is up
        else:
            fingures_up_list[finger]=0 #fingure is down

    
    if hand_lable=='Right': 
        #compare between distance for tip and Mcp at x-axis
        if lmlist[tips[0]][1] < lmlist[tips[0]-2][1]:
            fingures_up_list[0]=1
        else:
            fingures_up_list[0]=0

     
    if hand_lable=='Left': 
        #compare between distance for tip and Mcp at x-axis
        if lmlist[tips[0]][1] > lmlist[tips[0]-2][1]:
            fingures_up_list[0]=1
        else:
            fingures_up_list[0]=0
    
    return fingures_up_list






        
        

        