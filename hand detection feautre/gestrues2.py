import pyautogui
import time

state=None


#for delay
last_action_time=0
delay=0

#for swipe
swipe_threshold=70
index_x=0

pre_avg_x=None

def gestrue_recognization(lm_list,fingurs_up,state):

    global pre_avg_x,last_action_time

   

    
    if fingurs_up==[0,1,1,0,0]:

        #this gestrue for swipe left and right

        avg_x=(lm_list[6][1]+lm_list[10][1])// 2

        if pre_avg_x is not None:


            if avg_x > pre_avg_x+swipe_threshold:
                if time.time() - last_action_time >.5:
          
                    print('swipe right')
                    last_action_time=time.time()
                
            elif avg_x < pre_avg_x-swipe_threshold:
                 if time.time() - last_action_time >.5:
                    print('swipe left')
                    last_action_time=time.time()

        pre_avg_x=avg_x #for first frame and update this variable
       
    else:
        pre_avg_x=None 


            
       


        

        

        





