from threading import Thread
import threading
import time

def imprimir1(i):

    if (i<0):
        return
    else:
        print("Funcion 1: " + str(i))
        time.sleep(1)
        return imprimir1(i-1)

def imprimir2(i):

    if (i<0):
        return
    else:
        print("Funcion 2: " + str(i))
        time.sleep(2)
        return imprimir2(i-1)

print("Threads with join")  
hilo1=Thread(target=imprimir1, args=(6,))
hilo2=Thread(target=imprimir2, args=(6,))
hilo1.start()
hilo1.join()
hilo2.start()
hilo2.join()