from tkinter import * 
from tkinter.ttk import *
root = Tk() 
Label(root, text = 'GeeksforGeeks', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
photo = PhotoImage(file = r"C:\Users\894360\Desktop\bc\Trabalho\log-in.png") 
photoimage = photo.subsample(3, 3) 
  
Button(root, text = '', image = photoimage, 
                    compound = LEFT).pack(side = TOP) 
  
mainloop() 