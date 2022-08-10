from tokenize import String
import serial
import time
i=0
alchol=0
smoke=0
ser=serial.Serial('COM3',9600)
while i<1:
   if(i>1):
      i=0
   else:
      while i<2:
         
         time.sleep(2)

         b=ser.readline()
         
         
         num_int = int(b)
         if i==0:
            smoke=num_int
         if i==1:
            alchol=num_int
             
         print(num_int)
         i=i+1
      time.sleep(15)
ser.close()
