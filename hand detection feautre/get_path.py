import tkinter as tk #library for simple GUI

from tkinter import filedialog 



#create function to return path 

def pick_file():

    root=tk.Tk() #make empty window

    #root.withdraw() #hide this empty window
    file_path=None
    
    try:
      #allow only to get power point files
      file_path=filedialog.askopenfilename(title='Get path' ,filetypes=(('power point files',"*.pptx;*.ppt"),) )

      


    except Exception as ex:
       print(f'Error : {ex}')

    finally:
       root.destroy()

    

    if file_path:
       return file_path
    else :
       return None
    


if __name__=="__main__":
   
   path=pick_file()

   if path:
      print(path)
   else:
      print('no files')
    


