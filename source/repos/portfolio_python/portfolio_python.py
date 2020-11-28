from bluetooth import *
import threading
from gpiozero import Motor
import time

name = “HC-06”
host = “01:23:45:67:89:AB”
port = 1


print("connected.  type stuff")

def myThread():
    while True:
        rdata = sock.recv(1024)
        print("received [%s]" % rdata)

th = threading.Thread(target=myThread, args=())
th.start()
motor = Motor(forward=20,backward=21)

while True:

    sock=BluetoothSocket( RFCOMM )
    if sock.connect((host, port)):
        data = raw_input("LED OFF")
        sock.send(data+'\n')
        motor.forward(speed=0.3)
        time.sleep(5)
    
        motor.backward(speed=0.5)
        time.sleep(5)
    else: break
    
th.join()
sock.close()
