from pickle import TRUE
from tokenize import String
import serial
import time
i=0
c=0
d=0
ser=serial.Serial('COM3',9600)
while TRUE:
        while i<2:
        
           

           b=ser.readline()
           stripped_string = b.strip()
           num_int = int(stripped_string)
           if i==0:
               c=num_int
           if i==1:
               d=num_int

           print(num_int)
           i=i+1
        time.sleep(4)

ser.close()
