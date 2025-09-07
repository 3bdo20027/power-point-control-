from camera_setup import get_capture,get_farme
from hand_deyection import process_lm,drawing_landmarks
import cv2

def main():
    cap=get_capture()

    while True:

        frame=get_farme(cap)

        results=process_lm(frame)
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:

            frame=drawing_landmarks(img=frame,results=results)



        cv2.imshow('main programe',frame)  

        if cv2.waitKey(2) & 0xff==ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
    

if __name__=="__main__":
    main()


