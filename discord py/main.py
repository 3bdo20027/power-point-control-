import subprocess  #to open external apps by using python as terminal

import threading #useing to run tow codes or more paralles



def start_api():
     #as run this line in terminal: uvicorn api_module:app--reload 
    subprocess.run(["uvicorn", "api_module:app", "--reload"])
    


def run_bot():
    subprocess.run(["python3", "power_point_Bot.py"])




if __name__=="__main__":

    #make thread to run api in background

    thread=threading.Thread(target=start_api)

    #start this thread
    thread.start()

    #run bot in main 
    run_bot()





