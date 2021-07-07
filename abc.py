import sys
sys.setrecursionlimit(5000)
block_cipher = None
import tkinter as tk
from tkinter import *
#from tkinter import Message, Text
from tkinter import messagebox
import cv2 , os
import shutil
import csv
import numpy as np
from PIL import Image , ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
LARGEFONT =("Verdana", 35) 



class tkinterApp(tk.Tk): 
      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs) 
        
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
        # initializing frames to an empty array 
        self.frames = {}   
   
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (StartPage, Page1, Page2, Page3): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(StartPage) 
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 
   
# first window frame startpage 
   
class StartPage(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        
        load = Image.open("au.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width = 30, bd = 5)
        T1.place(x=180, y=20)
        
        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width = 30, show='*', bd = 5)
        T2.place(x=180, y=80)
        
        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(Page2)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
         
        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)
        
        def register():
            window = tk.Tk()
            window.geometry("400x400")
            window.resizable(0,0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial",15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x = 200, y=10)
            
            l2 = tk.Label(window, text="Password:", font=("Arial",15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x = 200, y=60)
            
            l3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x = 200, y=110)
            
            def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("credential.txt", "w") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                        window.destroy()
                            
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            b1 = tk.Button(window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)
            
            #window.geometry("470x220")
            #window.mainloop()
            
        B2 = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        B2.place(x=650, y=20)
# second window frame page1  


        



class Page1(tk.Frame): 
      
    def __init__(self, parent, controller): 
          
        tk.Frame.__init__(self, parent) 
        load = Image.open("au.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                pass
            try:
                import unicodedata
                unicodedata.numeric(s)
                return True
            except(TypeError , ValueError):
                pass
            return False

        
        def gotopage2():
            controller.show_frame(Page2)
        def clear():
            txt1.delete(0,'end')
            txt2.delete(0,'end')
            txt3.delete(0,'end')
            res = ""
            message.configure(text=res)
        def TakeImages():
            name = (txt1.get())
            roll = (txt2.get())
            enroll =(txt3.get())
            sf = var.get()
            sf1 = var1.get()
            if(sf =='MCA'):
                if(sf1 =='1'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1
                                
                                cv2.imwrite("TrainingImages\MCA\year1\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\MCA\year1\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
                if(sf1 =='2'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1
                                
                                cv2.imwrite("TrainingImages\MCA\year2\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\MCA\year2\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
                if(sf1 =='3'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1
                                
                                cv2.imwrite("TrainingImages\MCA\year3\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\MCA\year3\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
            if(sf =='BCA'):
                if(sf1 =='1'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1
                                
                                cv2.imwrite("TrainingImages\BCA\year1\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\BCA\year1\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
                if(sf1 =='2'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1
                                
                                cv2.imwrite("TrainingImages\BCA\year2\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\BCA\year2\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
                if(sf1 =='3'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1                                
                                cv2.imwrite("TrainingImages\BCA\year3\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\BCA\year3\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
            if(sf =='PGDCA'):
                if(sf1 =='1'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1
                                
                                cv2.imwrite("TrainingImages\PGDCA\year1\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\PGDCA\year1\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
                if(sf1 =='2'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1
                                
                                cv2.imwrite("TrainingImages\PGDCA\year2\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\PGDCA\year2\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
                if(sf1 =='3'):
                    if(name.isalpha() and is_number(roll)):
                        cam = cv2.VideoCapture(0)
                        harcascadePath = "haarcascade_frontalface_default.xml"
                        detector = cv2.CascadeClassifier(harcascadePath)
                        sampleNum = 0
                        while(True):
                            ret , img = cam.read()
                            gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                            faces = detector.detectMultiScale(gray , 1.3 , 5) 
                            
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)    
                                sampleNum = sampleNum+1
                                
                                cv2.imwrite("TrainingImages\PGDCA\year3\ " +name+ "." + roll + "." +str(sampleNum) + ".jpg" , gray[y:y+h , x:x+h] )
                                cv2.imshow('frame',img)
                            if cv2.waitKey(100) & 0xFF  == ord('q'):
                                break
                            elif sampleNum > 60:
                                break
                        cam.release()
                        cv2.destroyAllWindows()
                        res = "image saved for roll no. :" + roll +  "Name : " +name 
                        row = [name , roll, enroll] 
                        sf = var.get()
                        sf1=var1.get()
                
                        with open('StudentDetails\PGDCA\year3\student_details.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                            
                    else:
                        if(is_number(name)):
                            res = "Enter Alphatical Name"
                            message.configure(text = res) 
        def Trainimage():
            
            harcascadePath="haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sf = var.get()
            sf1 = var1.get()
            if sf == 'MCA':    
                if(sf1=='1'):   
                    recognizer = cv2.face.LBPHFaceRecognizer_create()         
                    faces,roll = getImagesAndLabels("TrainingImages\MCA\year1")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\MCA\year1\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)
                if(sf1=='2'):  
                    recognizer = cv2.face.LBPHFaceRecognizer_create()          
                    faces,roll = getImagesAndLabels("TrainingImages\MCA\year2")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\MCA\year2\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)
                if(sf1=='3'):  
                    recognizer = cv2.face.LBPHFaceRecognizer_create()          
                    faces,roll = getImagesAndLabels("TrainingImages\MCA\year3")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\MCA\year3\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)
            if sf == 'BCA':    
                if(sf1=='1'):  
                    recognizer = cv2.face.LBPHFaceRecognizer_create()          
                    faces,roll = getImagesAndLabels("TrainingImages\BCA\year1")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\BCA\year1\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)
                if(sf1=='2'):    
                    recognizer = cv2.face.LBPHFaceRecognizer_create()        
                    faces,roll = getImagesAndLabels("TrainingImages\BCA\year2")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\BCA\year2\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)
                if(sf1=='3'):  
                    recognizer = cv2.face.LBPHFaceRecognizer_create()          
                    faces,roll = getImagesAndLabels("TrainingImages\BCA\year3")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\BCA\year3\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)     
            if sf == 'PGDCA':    
                if(sf1=='1'):  
                    recognizer = cv2.face.LBPHFaceRecognizer_create()          
                    faces,roll = getImagesAndLabels("TrainingImages\PGDCA\year1")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\PGDCA\year1\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)
                if(sf1=='2'): 
                    recognizer = cv2.face.LBPHFaceRecognizer_create()           
                    faces,roll = getImagesAndLabels("TrainingImages\PGDCA\year2")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\PGDCA\year2\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)
                if(sf1=='3'):  
                    recognizer = cv2.face.LBPHFaceRecognizer_create()          
                    faces,roll = getImagesAndLabels("TrainingImages\PGDCA\year3")
                    recognizer.train(faces, np.array(roll))
                    recognizer.save("TrainingImageLabel\PGDCA\year3\Trainner.yml")
                    res = "Image Trained" # + ",".join(str(f) for f in roll)
                    message.configure(text = res)
        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
            faces =[]
            rolls=[]
            for imagePath in imagePaths:
                pilImage =Image.open(imagePath).convert('L')
                imageNp=np.array(pilImage,'uint8')
                roll=  int(os.path.split(imagePath)[-1].split(".")[1])
                faces.append(imageNp)
                rolls.append(roll)          
            return faces,rolls

        def TrackImage():
            
            sf = var.get()
            sf1 = var1.get()
            
            #recognizer.read("TrainingImageLabel\Trainner.yml")
            if sf =='MCA':
                if sf1 =='1':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\MCA\year1\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\MCA\year1\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            print(roll) 
                            if 'roll' in df:
                        
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                print(roll)
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break   
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\MCA\year1\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)

                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                if sf1 =='2':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\MCA\year2\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\MCA\year2\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(conf) 
                            #print(df)
                            if 'roll' in df :
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first',inplace=False, ignore_index=False)
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\MCA\year2\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index= FALSE,mode ='a')
                    
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                if sf1 =='3':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\MCA\year3\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\MCA\year3\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\MCA\year3\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
            if sf == 'BCA':
                if sf1 == '1':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\BCA\year1\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\BCA\year1\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\BCA\year1\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                if sf1 =='2':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\BCA\year2\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\BCA\year2\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\BCA\year2\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                if sf1 =='3':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\BCA\year3\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\BCA\year3\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\BCA\year3\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
            if sf == 'PGDCA':
                if sf1 == '1':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\PGDCA\year1\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\PGDCA\year1\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\PGDCA\year1\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                

        lb6 =tk.Label(self , text = "Year", width =15 , height = 1,bg ="lavender", fg = "gray23", font=("TRomanimes New", 18 ,'bold'))
        lb6.place(x=200, y =195)

        var1 = tk.StringVar()
# initial value
        var1.set('1')

        choices = ['1', '2', '3']
        option = tk.OptionMenu(self, var1, *choices)
        option.pack(side='left', padx=10, pady=10)
        option.place(x=600 , y =195)
        sf1 = var1.get()

        lb5 =tk.Label(self , text = "Stream", width =15 , height = 1,bg ="lavender", fg = "gray23", font=("TRomanimes New", 18 ,'bold'))
        lb5.place(x=200, y =120)

        var = tk.StringVar()
# initial value
        var.set('MCA')
        
        choices = ['MCA', 'BCA', 'PGDCA']
        option = tk.OptionMenu(self, var, *choices)
        option.pack(side='left', padx=10, pady=10)
        option.place(x=600 , y =125)
        sf = var.get()
        #sf1 = var1.get()
        #print(sf)
        

        message1= tk.Label(self, text = "Face Recognition Attendance Managemesnt System", bg = "gray23" , fg ="white", width =50, height =2 ,font=("arial", 20 ,'italic bold underline'))
        message1.place(x = 200 , y = 20)        
        lb1 =tk.Label(self , text = "Enter Name", width =20 , height = 1,bg ="lavender", fg = "gray23", font=("arial", 20 ,'bold'))
        lb1.place(x=200 , y =260)

        txt1 = tk.Entry(self , width = 20, bg ="lavender", fg = "gray23",font=("arial", 15 ,'bold') )
        txt1.place( x = 600 , y = 265)

        lb2 =tk.Label(self , text = "Enter Roll No.", width =20 , height = 1,bg ="lavender", fg = "gray23", font=("arial", 20 ,'bold'))
        lb2.place(x=200 , y =330)

        txt2 = tk.Entry(self , width = 20, bg ="lavender", fg = "gray23",font=("arial", 15 ,'bold') )
        txt2.place( x = 600 , y = 335)

        lb3 =tk.Label(self , text = "Enter Enrollment No.", width =20 , height = 1,bg ="lavender", fg = "gray23", font=("arial", 20 ,'bold'))
        lb3.place(x=200 , y =400)

        txt3 = tk.Entry(self , width = 20, bg ="lavender", fg = "gray23",font=("arial", 15 ,'bold') )
        txt3.place( x = 600 , y = 405)

        lb4 =tk.Label(self , text = "Notification", width =20 , height = 1,bg ="lavender", fg = "gray23", font=("arial", 20 ,'bold'))
        lb4.place(x=200 , y =570)

        message = tk.Label(self , text ="", width = 30, bg ="lavender", fg = "gray23",font=("arial", 15 ,'bold') )
        message.place( x = 600 , y = 575)



        takeimage = tk.Button(self, text = "Take Image", command =TakeImages, bg ="lavender", fg = "gray23",width =10 , height =2, font=("arial", 20 ,'bold') )
        takeimage.place(x = 200, y = 470 )

        trainimage = tk.Button(self, text = "Train Image", command =Trainimage, bg ="lavender", fg = "gray23",width =10 , height =2, font=("arial", 20 ,'bold') )
        trainimage.place(x = 500, y = 470 )

        trackimage = tk.Button(self, text = "Track Image", command =TrackImage, bg ="lavender", fg = "gray23",width =10 , height =2, font=("arial", 20 ,'bold') )
        trackimage.place(x = 800, y = 470 ) 

        sub1 = tk.Button(self, text = "Submit", command =gotopage2, bg ="lavender", fg = "gray23",width =10 , height =1, font=("arial", 15 ,'bold') )
        sub1.place(x = 1000, y = 570 )

        clearbutton1 = tk.Button(self, text = "Clear", command =clear, bg ="lavender", fg = "gray23",width =15 , height =1 ,font=("arial", 20 ,'bold') )
        clearbutton1.place(x = 900, y = 220 )


      
# third window frame page2 
class Page2(tk.Frame):  
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        load = Image.open("au.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        def gotopage1():
            controller.show_frame(Page1)
        def gotopage3():
            controller.show_frame(Page3)

        lb1= ttk.Label(self, text = "Student Details",   background = 'steel blue',foreground ="orange", font = ("TRomanimes New ", 20))
        lb1.place(x=550 , y =50)
# label 
#lb2 = ttk.Label(window, text = "Select the Month :",   font = ("Times New Roman", 15))
#lb2.place(x= 180 , y = 100)

        sub1 = tk.Button(self, text = "Click Here To Fill Details OF New Students", command =gotopage1,bg ='orange red', fg = "black",width =50 , height =1, font=("TRomanimes New", 15 ,'bold') )
        sub1.place(x = 350, y = 150 )


        lb2= ttk.Label(self, text = "Mark Attendance",background = 'steel blue',foreground ="orange", font = ("TRomanimes New ", 20))
        lb2.place(x=550 , y =350)



        sub2 = tk.Button(self, text = "Click Here To Mark Attendance", command =gotopage3,  bg ='orange red',fg = "black",width =50 , height =1, font=("TRomanimes New", 15 ,'bold') )
        sub2.place(x =350, y = 450 )
        
class Page3(tk.Frame): 
      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        load = Image.open("au.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        def gotopage2():
            controller.show_frame(Page2)
        def TrackImage():
            
            sf = var.get()
            sf1 = var1.get()
            
            #recognizer.read("TrainingImageLabel\Trainner.yml")
            if sf =='MCA':
                if sf1 =='1':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\MCA\year1\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\MCA\year1\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names)
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll) 
                            if 'roll' in df:
                        
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                #print(roll)
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break   
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\MCA\year1\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                if sf1 =='2':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\MCA\year2\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\MCA\year2\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(conf) 
                            #print(df)
                            if 'roll' in df :
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first',inplace=False, ignore_index=False)
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\MCA\year2\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index= FALSE,mode ='a')
                    
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                if sf1 =='3':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\MCA\year3\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\MCA\year3\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\MCA\year3\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
            if sf == 'BCA':
                if sf1 == '1':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\BCA\year1\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\BCA\year1\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\BCA\year1\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                if sf1 =='2':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\BCA\year2\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\BCA\year2\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\BCA\year2\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                if sf1 =='3':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\BCA\year3\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\BCA\year3\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\BCA\year3\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
            if sf == 'PGDCA':
                if sf1 == '1':
                    recognizer= cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("TrainingImageLabel\PGDCA\year1\Trainner.yml")
                    harcascadePath="haarcascade_frontalface_default.xml"
                    faceCascade = cv2.CascadeClassifier(harcascadePath)
                    df = pd.read_csv("StudentDetails\PGDCA\year1\student_details.csv")
                    cam = cv2.VideoCapture(0)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    col_names= ['roll', 'name', 'Date', 'Time']
                    attendance = pd.DataFrame(columns = col_names )
                    while True:
                        ret , im = cam.read()
                        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.2 ,5)      
                        for (x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w, y+h), (255,0,0),2)  
                            roll , conf =recognizer.predict(gray[y:y+h , x:x+w])
                            #print(roll)
                            if 'roll' in df:
                                #print(conf)
                                #print(roll)
                                ts = time.time()
                                date = datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                                timeStamp =  datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
                                aa=df.loc[df['roll'] == roll]['name'].values
                                tt = str(roll) + "-" +aa
                                attendance.loc[len(attendance)] = [roll , aa ,date , timeStamp]
                                
                            else:
                                roll='UNKNOWN'
                                tt = str(roll)
                            if(conf>75):
                                noOFFile = len(os.listdir("ImagesUnknown"))+1
                                cv2.imwrite("ImagesUnknown\Image"+str(noOFFile) + ".jpg", im[y:y+h , x:x+w])
                            cv2.putText(im,str(tt), (x,y+h), font, 1 ,(255,255,255),2 )
                        attendance= attendance.drop_duplicates(subset=['roll'], keep='first')
                        cv2.imshow('im',im)
                        
                        if (cv2.waitKey(1) == ord('q')):
                            break
                        
                    ts=time.time()
                    date=datetime.datetime.fromtimestamp(ts).strftime('%Y - %m - %d')
                    timeStamp= datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')      
                    Hour , Minute , Second = timeStamp.split(":")
                    fileName = "Attendance\PGDCA\year1\Attendance_"+date+ ".csv"
                    attendance.to_csv(fileName, index=False,mode ='a')
                    cam.release()
                    cv2.destroyAllWindows()
                    res = attendance
                    message.configure(text = res)
                
        
        lb6 =tk.Label(self , text = "Year", width =15 , height = 1,bg ="lavender", fg = "gray23", font=("TRomanimes New", 18 ,'bold'))
        lb6.place(x=200, y =195)

        var1 = tk.StringVar()
# initial value
        var1.set('1')

        choices = ['1', '2', '3']
        option = tk.OptionMenu(self, var1, *choices)
        option.pack(side='left', padx=10, pady=10)
        option.place(x=600 , y =195)
        sf1 = var1.get()

        lb5 =tk.Label(self , text = "Stream", width =15 , height = 1,bg ="lavender", fg = "gray23", font=("TRomanimes New", 18 ,'bold'))
        lb5.place(x=200, y =120)

        var = tk.StringVar()
# initial value
        var.set('MCA')
        
        choices = ['MCA', 'BCA', 'PGDCA']
        option = tk.OptionMenu(self, var, *choices)
        option.pack(side='left', padx=10, pady=10)
        option.place(x=600 , y =125)
        sf = var.get()
        #sf1 = var1.get()
        #print(sf)
        

        message1= tk.Label(self, text = "Face Recognition Attendance Managemesnt System", bg = "gray23" , fg ="white", width =50, height =2 ,font=("arial", 20 ,'italic bold underline'))
        message1.place(x = 200 , y = 20)        
        trackimage = tk.Button(self, text ="Click Here To Take Attendance", command =TrackImage, bg ="lavender", fg = "gray23",width =25 , height =2, font=("arial", 15 ,'bold') )
        trackimage.place(x = 400, y = 270 )
        lb4 =tk.Label(self , text = "Notification", width =20 , height = 1,bg ="lavender", fg = "gray23", font=("arial", 20 ,'bold'))
        lb4.place(x=200 , y =375)

        message = tk.Label(self , text ="", width = 30, bg ="lavender", fg = "gray23",font=("arial", 20 ,'bold') )
        message.place( x = 600 , y = 375)
        sub1 = tk.Button(self, text = "Submit", command =gotopage2, bg ="lavender", fg = "gray23",width =10 , height =1, font=("arial", 15 ,'bold') )
        sub1.place(x = 500, y =480 )
 
# Driver Code 
app = tkinterApp() 
app.geometry('1280x720')
app.mainloop() 