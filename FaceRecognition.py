from importlib.resources import path
from multiprocessing.connection import wait
from sre_constants import SUCCESS
from time import time
from turtle import width
import cv2
from cv2 import cvtColor
import numpy as npy
import face_recognition as face_rec
import os
import pyttsx3 as textSpeach
from datetime import datetime
import bibu
import notification

engine = textSpeach.init()
name1="nayak"
while True:
    count=0
    if bibu.smoke==1 or bibu.alchol==1:
                def resize(img, size):
                    width = int(img.shape[1]*size)
                    height = int(img.shape[0]*size)
                    dimension = (width,height)
                    return cv2.resize(img, dimension,interpolation = cv2.INTER_AREA)

                path = 'images'
                studentimg = []
                studentName = []
                myList =os.listdir(path)
                #print(myList)

                for cl in myList:
                    cur_img = cv2.imread(f'{path}\{cl}')
                    studentimg.append(cur_img)
                    studentName.append(os.path.splitext(cl)[0])
                #print(studentName)

                def findEncodings(images):
                    encoding_list = []
                    for img in images :
                        img = resize(img, 0.50)
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        encodeimg = face_rec.face_encodings(img)[0]
                        encoding_list.append(encodeimg)
                    return encoding_list

                def MarkAttendence(name):
                    with open('Attendance.csv', 'r+') as f:
                        myDataList = f.readlines()
                        nameList =[]
                        for line in myDataList:
                            entry = line.split(',')
                            nameList.append(entry[0])

                        if name not in nameList:
                            now = datetime.now()
                            timeStr = now.strftime('%H: %M')
                            dateStr = now.strftime('%m/%d/%Y')
                            f.writelines(f'\n{name}, {timeStr}, {dateStr}')
                            statement = str(name)
                            engine.say(statement)
                            engine.runAndWait()



                encode_list = findEncodings(studentimg)

                vid = cv2.VideoCapture(0)
                while True:
                    if count>0:
                       break
                    success, frame = vid.read()
                    smaller_frames = cv2.resize(frame, (0,0),None,0.25,0.25)
                    #smaller_frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)

                    faces_in_frame = face_rec.face_locations(smaller_frames)
                    encode_in_frame = face_rec.face_encodings(smaller_frames,faces_in_frame)
                    
                                
                    for encodeFace, faceLoc in zip(encode_in_frame, faces_in_frame):
                        matches = face_rec.compare_faces(encode_list, encodeFace)
                        faceDis = face_rec.face_distance(encode_list,encodeFace)
                        #print(faceDis)
                        
                        matchIndex = npy.argmin(faceDis)

                        if matches[matchIndex] :
                            name = studentName[matchIndex].upper()

                            y1, x2, y2, x1 = faceLoc
                            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
                            cv2.rectangle(frame,(x1,y2-25),(x2,y2),(0,255,0),cv2.FILLED)
                            cv2.putText(frame , name, (x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
                            count=count+1
                            MarkAttendence(name)
                            print(name)
                            if name1!=name:
                                if bibu.alchol==1:
                                   print(name +" is alcoholic")
                                if bibu.smoke==1:
                                   print(name +"is smoker") 
                                name1=name
                                notification.msg()

                        cv2.imshow('video',frame)

                        cv2.waitKey(1)
                # cv2.destroyAllWindows()
                                       
                