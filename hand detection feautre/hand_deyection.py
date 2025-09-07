import mediapipe as mp
import cv2


#setup hand detection module

mp_hands=mp.solutions.hands

#intialize the object 

hands=mp_hands.Hands(

    static_image_mode=False,  #use for process image not streaming
    max_num_hands=1,   #number of hands uses
    min_detection_confidence=.6,
    min_tracking_confidence=.7,

)


#setup hand drawing  module

mp_drawing=mp.solutions.drawing_utils

#make list for tips of fingeurs

tips=[4,8,12,16,20]



#process land marks function

def process_lm(src):


    src.flags.writeable=False  #to increase process speed

    results=hands.process(src)

    src.flags.writeable=True

    return results


#drawing landmarks function

def drawing_landmarks(img,results):

    for hand_marks in results.multi_hand_landmarks:

        mp_drawing.draw_landmarks(img,hand_marks,mp_hands.HAND_CONNECTIONS)
    return img
    



        
        

        