from tkinter import *
import time
import threading
from threading import Thread
from random import randint
from tkinter import messagebox



def rando():
    dice_label.config(text=f'Dice Number: {randint(1,6)}')

def wait_time():
    time.sleep(5)
    label.config(text="Time over")
    messagebox.showinfo(message="GAME OVER", title="You Lose!")

def hilo():
    hilo_time=Thread(target=wait_time, args=())
    hilo_time.start()



window= Tk()

window.geometry("700x400")


label= Label(window)
label.pack(pady=20)

label.config(text="Su turno")
dice_label=Label(window,text="")
dice_label.pack(pady=20)

b1= Button(window,text= "Start", command=hilo)
b1.pack(pady=20)




b2= Button(window,text= "Lazar el dado", command=rando)
b2.pack(pady=20)

window.mainloop()