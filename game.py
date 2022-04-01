from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import os
from threading import Thread
import threading
import time
from pygame import mixer
global enemy_x
global enemy_y

enemy_x=650
enemy_y=50

mixer.init()

#***************Reproducir música***********************
def play(filename,loop):
    #path = os.path.join('Sounds',filename)
    effects= mixer.Sound(filename)
    effects.play(loops=loop)

def bgmusic():
    print("PLAY SONG")
    #play("song.mp3",-1)
    mixer.music.load("song.mp3")
    mixer.music.play(loops=-1)
        #time.sleep(1)

    
#***************Cargar Imagenes***********************
#Entrada: Nombre de la imagen
#Restricciones: el nombre de la imagen debe ser formato str
#Salida: Genera la imagen
def loadImage(filename):
    if isinstance(filename, str):
        path = os.path.join('Images',filename)
        #path="Images/"+filename
        imagen = PhotoImage(file=path)
        return imagen



def dibujar():
        global enemy_x
        global enemy_y
        window = Tk()
        window.title("GAME")
        window.minsize(800,600)
        window.resizable(width=NO, height=NO)
        window.configure(background="white")                
        cv= Canvas(window, width= 2000, height = 2000, bg="#d3c692")#d3c692
        cv.place(x=0,y=0)                
        img= loadImage("bg.png")
        f1= loadImage("p2.png")
        ship= loadImage("shiprm.png")
        bullet= loadImage("bullet.png")
        cv.create_image(425,320, image = img)                
        cv.create_image(enemy_x,enemy_y, image = f1, tags = "enemy")
        cv.create_image(170,140, image = ship, tags = "player")
        cv.create_image(140,enemy_y, image = bullet, tags = "bullet")
        #self.__r = Text(window,width=1,height=1,cv="#d3c692",fg="black",font=("Helvetica",15))#window de texto
        #self.__r.place(x=500,y=25)
        #botonAvanzar1 = Button(window, text="Lanzar P1", command=self.__jugar1,cv="#144214",fg="white",font=("Helvetica",15)).place(x=100,y=20)
        #botonAvanzar2 = Button(window, text="Lanzar P2", command=self.__jugar2,cv="#a9052e",fg="white",font=("Helvetica",15)).place(x=250,y=20)
        #botonSave = Button(window, text="Play Song", command=bgmusic, bg="#096654",fg="white",font=("Helvetica",15)).place(x=400,y=20)
        
        #time.sleep(5)
        #t4 = Thread(target=move_enemy, args=())
        #t4.start()
        move_enemy()
        def up(e):
           x = 0
           y = -20
           cv.move("player", x, y)
           play("move.wav",1)

        def down(e):
           x = 0
           y = 20
           cv.move("player", x, y)
           play("move.wav",1)
        window.bind("<Up>", up)
        window.bind("<Down>", down)

        

        def move_enemy():
            while (True):
                move_enemy_down()
                move_enemy_up()
            
        def move_enemy_down():
            global enemy_x
            global enemy_y
            while(enemy_y<=550):
                enemy_y+=25
                cv.move("enemy",enemy_x,25)
                time.sleep(1)
                print(enemy_y)

        def move_enemy_up():
            global enemy_x
            global enemy_y
            while(enemy_y>=50):
                enemy_y-=25
                cv.move("enemy",enemy_x,-25)
                time.sleep(1)
                print(enemy_y)

        window.mainloop()


t1= Thread(target=bgmusic, args=())
t2= Thread(target=dibujar, args=())
#t3= Thread(target=move_enemy, args=())
t1.start()
t2.start()
#t3.start()
