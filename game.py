from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import os
from playsound import playsound
from threading import Thread
import threading
import time

global enemy_x
global enemy_y
global player_x
global player_y
enemy_x=650
enemy_y=50
player_x=170
player_y=140



#***************Reproducir música***********************
def play(filename):
    #path = os.path.join('Sounds',filename)
    playsound(filename)

#***************Cargar Imagenes***********************
#Entrada: Nombre de la imagen
#Restricciones: el nombre de la imagen debe ser formato str
#Salida: Genera la imagen
def loadImage(filename):
    path = os.path.join('Images',filename)
    imagen = PhotoImage(file=path)
    return imagen

def bgmusic():
    print("Playing sound on bg")
    playsound("song.mp3")


#Funcion principal
def main():

    def wait_time(i):
        if(i<6):
            i=i+1
            print("Time elapsed: "+str(i)+ " seconds")
            time.sleep(1)
            return wait_time(i)
            
        else:
            #abel.config(text="Time Over")
            messagebox.showinfo(message="GAME OVER", title="You Lose!")
            return
    def hilo():
        hilo_time=Thread(target=wait_time, args=(0,))
        hilo_time.start()


    window = Tk()
    window.title("GAME")
    window.minsize(800,600)
    window.resizable(width=NO, height=NO)
    window.configure(background="white")  
    cv= Canvas(window, width= 2000, height = 2000, bg="white")
    cv.place(x=0,y=0)
    bg= loadImage("bg.png")
    f1= loadImage("p2.png")
    ship= loadImage("shiprm.png")
    #bullet= loadImage("bullet.png")
    cv.create_image(425,320, image = bg)  
    cv.create_image(enemy_x,enemy_y, image = f1, tags = "enemy")
    cv.create_image(170,140, image = ship, tags = "player")
    #cv.create_image(140,enemy_y, image = bullet, tags = "bullet")

    botonSTART = Button(window, text="START", command=hilo, bg="#096654",fg="white",font=("Helvetica",15)).place(x=400,y=20)


    #Move player
    def up(e):
        global player_y
        player_y-=20
        x = 0
        y = -20
        cv.move("player", x, y)
        play("move.mp3")

    def down(e):
        global player_y
        player_y+=20
        x = 0
        y = 20
        cv.move("player", x, y)
        play("move.mp3")

    def left(e):
        global player_x
        player_x-=20
        x = -20
        y = 0
        cv.move("player", x, y)
        play("move.mp3")

    def right(e):
         global player_x
         player_x+=20
         x = 20
         y = 0
         cv.move("player", x, y)
         play("move.mp3")

    window.bind("<Up>", up)
    window.bind("<Down>", down)
    window.bind("<Left>", left)
    window.bind("<Right>", right)
       
    window.mainloop()


hilo1= Thread(target=bgmusic, args=())
hilo2= Thread(target=main, args=())
hilo1.start()
hilo2.start()



