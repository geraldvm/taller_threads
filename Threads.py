from threading import Thread
import threading
import time

def imprimir1():
    i=6
    while(i > 0):
        print("Funcion 1: " + str(i))
        i-=1
        time.sleep(1)

def imprimir2():
    i=6
    while(i > 0):
        print("Funcion 2: " + str(i))
        i-=1
        time.sleep(2)

print("Threads with join")
t1= Thread(target=imprimir1, args=())
t1.start()
t1.join()
t2= Thread(target=imprimir2, args=())
t2.start()
t2.join()
