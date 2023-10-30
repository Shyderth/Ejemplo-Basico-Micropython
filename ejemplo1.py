from machine import  Pin
import time

RED= Pin(13,Pin.OUT)
GREEN=Pin(12,Pin.OUT)
BLUE=Pin(14,Pin.OUT)

B1=Pin(27,Pin.IN)
B2=Pin(26,Pin.IN)
B3=Pin(25,Pin.IN)

while True :
    if not (B1.value()):
        RED.value(0)
    else:
        RED.value(1)
        
    if not (B2.value()):
        GREEN.value(0)
    else:
        GREEN.value(1)
    
    if not (B3.value()):
        BLUE.value(0)
    else:
        BLUE.value(1)