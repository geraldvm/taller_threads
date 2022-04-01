
from tkinter import *
import time
import threading
from random import randint
from tkinter import messagebox


#Define the tkinter instance
window= Tk()

#Define the size of the tkinter frame
window.geometry("700x400")

def rando():
    dice_label.config(text=f'Dice Number: {randint(1,6)}')
#Define the function to start the thread
def wait_time():
   label.config(text="Su turno")
   time.sleep(5)
   label.config(text="Time Over")
   messagebox.showinfo(message="GAME OVER", title="You Lose!")
   
label= Label(window)
label.pack(pady=20)
#Create button
b1= Button(window,text= "Start", command=threading.Thread(target=wait_time).start())

#b1= Button(window,text= "Start", command=wait_time)
b1.pack(pady=20)
b1= Button(window,text= "Lazar el dado", command=rando)
b1.pack(pady=20)

dice_label=Label(window,text="")
dice_label.pack(pady=20)


label.config(text="Su turno")

window.mainloop()


