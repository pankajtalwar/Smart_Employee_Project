import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from PIL import ImageTk,Image
from datetime import date
from tkinter.ttk import Combobox
from tkinter import filedialog
import shutil
import os
#from tkinter.ttk import Progressbar
#import threading
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import csv
import cv2
import sys, numpy


from glob import glob;from os.path import expanduser
top=Tk()
top.geometry('1400x730')

chart=StringVar()   
em1=" "
def login_page():
    
    def login():
        user=username1.get()
        passwd=password1.get()
        
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        sql=("select * from login_page where USERNAME='%s'and PASSWORD='%s'"%(user,passwd))
        cur.execute(sql)
        myresult=cur.fetchall()
        
        for x in myresult:
            page2()
            #login.destroy()
        
        myconn.rollback()
        myconn.close()

    top.title(".................LOGIN PAGE FOR SECURITY...................")

    bg=PhotoImage(file=r"image//banner1.png")
    myimage=Label(image=bg)
    myimage.place(x=0,y=0)
    
 
    bg1=PhotoImage(file=r"image//user (3).png")
    myimage=Label(image=bg1,bg="white")
    myimage.place(x=430,y=320)
    
    bg2=PhotoImage(file=r"image//lock.png")
    myimage=Label(image=bg2,bg="white")
    myimage.place(x=430,y=390)
    
    
    l4= Label(top,text="LOGIN PAGE", font=("times new roman", 25),bg="white").place(x=530,y=250)

    username1=StringVar()
    password1=StringVar()
    #newpassword1=StringVar()
    
    l1=Label(top,text="USERNAME",font=("times new roman bold", 15),bg="white").place(x=465,y=320) 
    e1=Entry(top,width=17, bd=5, font=("times new roman", 15),textvariable=username1).place(x=650,y=320)
    l2=Label(top,text="PASSWORD",font=("times new roman bold", 15),bg="white").place(x=470,y=390) 
    e1=Entry(top,show="*",width=17,bd=5,font=("times new roman",15),textvariable=password1).place(x=650,y=390)
    b1=Button(top,width=17,bd=5,text="SIGN IN",font=("times new roman",15),command=login,bg="white").place(x=535,y=470)
    #b2=Button(top,width=10,bd=5,text="BUTTEN ",font=("times new roman",10),bg="white",command=login).place(x=750,y=470)
    top.mainloop()
 
def login_destroy():
    login_page.destory()
    
def page2():

    im1=PhotoImage(file="image//ab.png")
    myimage=Label(image=im1)

    im2=PhotoImage(file="image//facial-recognition.png")
    myimage=Label(image=im2)

    im3=PhotoImage(file="image//workers.png")
    myimage=Label(image=im3)
    
    im4=PhotoImage(file="image//vision.png")
    myimage=Label(image=im4)
    
    im5=PhotoImage(file="image//secure.png")
    myimage=Label(image=im5)
    
    im6=PhotoImage(file="image//ai.png")
    myimage=Label(image=im5)
    
    im7=PhotoImage(file="image//immigration.png")
    myimage=Label(image=im5)
    
    im8=PhotoImage(file="image//team.png")
    myimage=Label(image=im8)
    
    im9=PhotoImage(file="image//workflow.png")
    myimage=Label(image=im9)
    
    im10=PhotoImage(file="image//b6.png")
    myimage=Label(image=im10)

    bg=PhotoImage(file=r"image//banner1.png")
    myimage=Label(image=bg)
    myimage.place(x=0,y=0)

    frame1=Frame(top,width=1400,height=80,highlightbackground="SKYBLUE",highlightthickness=1,bg="white").place(x=0,y=0)

    frame3=Frame(top,width=500,height=550,highlightbackground="black",highlightthickness=1,bg="white").place(x=353,y=102)
    b1=Button(top,width=145,bd=6,font=("arial",10),bg="WHITE",height=145,command=page3,image=im8).place(x=420,y=120)
    b3=Button(top,width=145,bd=6,font=("arial",10),bg="WHITE",height=145,command=page5,image=im7).place(x=630,y=120)
    b4=Button(top,width=145,bd=6,font=("arial",10),bg="WHITE",height=145,command=page4,image=im9).place(x=420,y=300)
    b7=Button(top,width=145,bd=6,font=("arial",10),bg="WHITE",height=145,image=im4,command=report).place(x=420,y=480)
    b8=Button(top,width=145,bd=6,font=("arial",10),bg="WHITE",height=145,command=page6,image=im5).place(x=630,y=300)
    b9=Button(top,width=145,bd=6,font=("arial",10),bg="WHITE",height=145,command=quit,image=im10).place(x=630,y=480)
    b10=Button(top,width=30,bd=5,font=("times new roman",15),bg="white",command=login_page,image=im1).place(x=15,y=90)
    
    
    l1= Label(top,text="MANAGEMENT" '\n' "EMPLOYEE DEPARTMENT", font=("times new roman", 9),bg="white").place(x=420,y=235)
    l3= Label(top,width=21,text="ATENDENCE REPORT", font=("times new roman", 10),bg="white").place(x=633,y=252)
    l4= Label(top,width=21,text="DEPARTMENT" '\n' " MANAGEMENT", font=("times new roman", 9),bg="white").place(x=424,y=418)
    l7= Label(top,width=21,text="ENTIRE DATA REPORT", font=("times new roman", 10),bg="white").place(x=420,y=612)
    l8= Label(top,width=21,text="CHANGE PASSWORD", font=("times new roman", 10),bg="white").place(x=630,y=430)
    l9= Label(top,width=21,text="EXIT", font=("times new roman", 10),bg="white").place(x=630,y=612)
    l10= Label(top,text="SMART EMPLOYEE  ATTANDANCE SYSTEM", font=("times new roman", 30),bg="white").place(x=200,y=10)
    
    top.mainloop()

def page3():
    
    def ondoubleclick(event):
        item=treev.selection()[0]
        a=treev.item(item,"text")
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        cur.execute("select * from employee_department where EMPLOYEE_ID='%s'" %(a))
        result=cur.fetchall()
        for row in result:
            empl=row[0]
            global em1
            em1=empl
            empl1.set(empl)
            dept=row[1]
            dept1.set(dept)
            name=row[2]
            name1.set(name)
            email=row[3]
            email1.set(email)
            gender=row[4]
            gender1.set(gender)
            dob=row[5]
            dob1.set(dob)
            doj=row[6]
            doj1.set(doj)
            proof_no=row[7]
            proof_no1.set(proof_no)
            proof_type=row[8]
            proof_type1.set(proof_type)
            address=row[9]
            address1.set(address)
            contact_no=row[10]
            contact_no1.set(contact_no)
          
        myconn.rollback()
        myconn.close()
        print("running")

    
    def add():

        dept=dept1.get()
        name=name1.get()
        email=email1.get()
        gender=gender1.get()
        dob=dob1.get()
        doj=doj1.get()
        proof_no=proof_no1.get()
        address=address1.get()
        proof_type=proof_type1.get()
        contact_no=contact_no1.get()
        photo=photo1.get()
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
        cur = myconn.cursor()
        sql = "insert into employee_department(DEPARTMENT,NAME,EMAIL,GENDER,DOB,DOJ,PROOF_NO,ADDRESS,PROFF_TYPE,CONTACT_NO)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (dept,name,email,gender,dob,doj,proof_no,address,proof_type,contact_no)
   
        myresult=cur.execute(sql,val)
    
        myconn.commit()
        messagebox.showinfo("employee_department","RECORD SAVED")
        print(cur.rowcount, "record saved!")
        myconn.close()  
        show()
        clear()

    def delete():
        empl=empl1.get()
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        sql="delete from employee_department where EMPLOYEE_ID='%s'"%(empl)
        val=(sql)
        cur.execute(sql)
        myconn.commit()
        messagebox.showinfo("employee_department","RECORD DELETED")

        print(cur.rowcount, "record deleted!")
        myconn.close()
        show()
        clear()
    
    def update():
        dept=dept1.get()
        empl=empl1.get()
        name=name1.get()
        email=email1.get()
        gender=gender1.get()
        dob=dob1.get()
        doj=doj1.get()
        proof_no=proof_no1.get()
        address=address1.get()
        proof_type=proof_type1.get()
        contact_no=contact_no1.get()
        
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        print("code runnning")
        sql="update employee_department set DEPARTMENT='%s', NAME='%s',EMAIL='%s',GENDER='%s',DOB='%s',DOJ='%s',PROOF_NO='%s',ADDRESS='%s',PROFF_TYPE='%s',CONTACT_NO='%s' where EMPLOYEE_ID='%s'" %(dept,name,email,gender,dob,doj,proof_no,address,proof_type,contact_no,empl)
        myresult=cur.execute(sql)
        myconn.commit()
        messagebox.showinfo("employee_department","RECORD updated")

        print(cur.rowcount,"record updated")
        myconn.close()
        show()
        clear()

    def show():
        for i in treev.get_children():
            treev.delete(i)
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
        cur = myconn.cursor()
        sql=("select *  from employee_department order by EMPLOYEE_ID DESC")
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            treev.insert('',0, text=row[0], values=(row[0],row[1], row[2], row[3], row[4], row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        myconn.rollback()
        myconn.close()


    def search1():
        for i in treev.get_children():
            treev.delete(i)
        sear=search11.get(),
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project") 
        cur = myconn.cursor()
        sql="select * from employee_department where EMPLOYEE_ID='%s'" % (sear)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            treev.insert('',0, text=row[0], values=(row[0],row[1], row[2], row[3], row[4], row[5],row[6],row[7],row[8],row[9],row[10]))
    
        myconn.rollback()
        myconn.close()

    def search2():
    
        empl=empl1.get()
        
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")   
        cur = myconn.cursor()
        sql="select * from employee_department where EMPLOYEE_ID='%s'" % (empl)
        cur.execute(sql)
        result = cur.fetchall()

        for row in result:
            empl=row[0]
            empl1.set(empl)
            dept=row[1]
            dept1.set(dept)
            name=row[2]
            name1.set(name)
            email=row[3]
            email1.set(email)
            gender=row[4]
            gender1.set(gender)
            dob=row[5]
            dob1.set(dob)
            doj=row[6]
            doj1.set(doj)
            proof_no=row[7]
            proof_no1.set(proof_no)
            proof_type=row[8]
            proof_type1.set(proof_type)
            address=row[9]
            address1.set(address)
            contact_no=row[10]
            contact_no1.set(contact_no)
    
    
        myconn.rollback()
        myconn.close()
        print("running..........")
        
    def combo_input():
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")   
        cur = myconn.cursor()
        sql="select DNAME from department_management"
        cur.execute(sql)
        result=[]
        for row in cur.fetchall():
            result.append(row[0])
        return result
       
    def clear():
      empl1.set('')
      dept1.set('')
      name1.set('')
      email1.set('')
      gender1.set('')
      dob1.set('')
      doj1.set('')
      proof_no1.set('')
      proof_type1.set('')
      address1.set('')
      contact_no1.set('')
      print("amkitt...")

    def csv_report():
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")   
        cur = myconn.cursor()
        sql="select * from employee_department"
        cur.execute(sql)
        header=[row[0]for row in cur .description]
        rows= cur.fetchall()
        f=open("employee_department" + ".csv","w")
        f.write(','.join(header)+'\n')
        for row in rows:
            f.write(','.join(str(r) for r in row)+'\n')
            
        f.close()
        print(str(len(rows))+'rows written successfully to'+ f.name)
        
    def updateSample():
        empl=empl1.get() 
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        print("code runnning")
        sql="update employee_department set photo='saved' where EMPLOYEE_ID ='%s'" %(em1)
        myresult=cur.execute(sql)
        myconn.commit()
        messagebox.showinfo("employee_department","RECORD updated")
        myconn.close()
    
    def face_detection():
        global em1
        print(em1)
        cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
        datasets = 'datasets'
        sub_data = str(em1)

        path = os.path.join(datasets, sub_data) 
        if not os.path.isdir(path):
            os.mkdir(path) 
            
        (width, height) = (130, 100)	 

        faceCascade = cv2.CascadeClassifier(cascPath)
        webcam = cv2.VideoCapture(0) 
        video_capture = cv2.VideoCapture(0)
        count = 1

        while count < 50:
                (_, im) = webcam.read() 
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
                faces = faceCascade.detectMultiScale(gray, 1.3, 4) 
                for (x, y, w, h) in faces:
                    cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
                    face = gray[y:y + h, x:x + w] 
                    face_resize = cv2.resize(face, (width, height))
                    cv2.imwrite('% s/% s.png' % (path, count), face_resize)
                count += 1
                cv2.imshow('OpenCV', im)
                key = cv2.waitKey(30) 
                if key == 27:
                    print("update smaple")
                    updateSample()
                    break	   	      
                   
        else:
            print("update sample run")
            updateSample()
        video_capture.release()
        cv2.destroyAllWindows()
        show()
        top.mainloop()
            
    top.title("................LOGIN PAGE FOR SECURITY................")

    bg=PhotoImage(file=r"image//banner1.png")
    myimage=Label(image=bg)
    myimage.place(x=0,y=0)
    
    empl1=StringVar()
    dept1=StringVar()
    name1=StringVar()   
    email1=StringVar()
    gender1=StringVar()
    dob1=StringVar()
    doj1=StringVar()
    proof_no1=StringVar()
    address1=StringVar()
    proof_type1=StringVar()
    contact_no1=StringVar()
    search11=StringVar()
    search12=StringVar()
    photo1=StringVar()
    
    im1=PhotoImage(file="image//ab.png")
    myimage=Label(image=im1)

    frame1=Frame(top,width=370,height=630,highlightbackground='black',highlightthickness=1,bg='white').place(x=10,y=60)
    
    l1 = Label(text="MANAGE EMPLOYEE AND DEPARTMENT...............", font=("times new roman", 20),bd=5,bg="white").place(x=350,y=5)
    l2 = Label(text="MANAGE EMPLOYEE", font=("times new roman", 20),bg="white").place(x=80,y=70)

    combobox = Combobox(top,values=combo_input(),textvariable=dept1).place(x=200, y=180)
    l3 = tk.Label(top, text="DEPARTMENT").place(x=30, y=180)

    l4=Label(top,text="EMPLOYEE ID").place(x=30,y=150) 
    e1=Entry(top,width=23,textvariable=empl1,bg="light blue").place(x=200,y=150)

    l5=Label(top,text="NAME").place(x=30,y=210) 
    e3=Entry(top,width=23,textvariable=name1,bg="light blue").place(x=200,y=210)

    l6=Label(top,text="EMAIL").place(x=30,y=240) 
    e1=Entry(top,width=23,textvariable=email1,bg="light blue").place(x=200,y=240)

    combobox = Combobox(top,values=['MALE','FEMALE'],textvariable=gender1).place(x=200, y=270)
    l7 = tk.Label(top, text="GENDER").place(x=30, y=270)

    l8=Label(top,text="D.O.B(dd-mm-yyy)").place(x=30,y=300) 
    e1=Entry(top,width=23,textvariable=dob1,bg="light blue").place(x=200,y=300)

    l9=Label(top,text="D.O.J(dd-mm-yyy)").place(x=30,y=330) 
    e1=Entry(top,width=23,textvariable=doj1,bg="light blue").place(x=200,y=330)

    l10=Label(top,text="PROOF NO.").place(x=30,y=360) 
    e1=Entry(top,width=23,textvariable=proof_no1,bg="light blue").place(x=200,y=360)


    l12=Label(top,text="ADDRESS").place(x=30,y=420) 
    e1=Entry(top,width=23,textvariable=address1,bg="light blue").place(x=200,y=420)

    combobox = Combobox(top,values=['ADHARCARD','PANCARD','DRIVING CARD','GREEN CARD','RASHAN CARD'],textvariable=proof_type1).place(x=200, y=390)
    l11= tk.Label(top, text="PROOF TYPE").place(x=30, y=390)


    l13=Label(top,text="CONTACT NO.").place(x=30,y=450) 
    e1=Entry(top,width=23,textvariable=contact_no1,bg="light blue").place(x=200,y=450)


#buttons()
    b1=Button(top,width=18,bd=10,text="UPDATE" '\n' "PHOTO SAMPLE",font=("times new roman",10),bg="white").place(x=160,y=550)
    b3=Button(top,width=18,bd=10,text="ADD" '\n' "PHOTO SAMPLE",font=("times new roman",10),bg="white",command=face_detection).place(x=160,y=615)
    b2=Button(top,width=10,bd=10,text="CLEAR",font=("times new roman",11),command=clear,bg="white").place(x=20,y=560)
    b4=Button(top,width=10,bd=10,text="UPDATE",font=("times new roman", 11),command=update,bg="white").place(x=20,y=620)
    b5=Button(top,width=18,bd=10,text="DELETE",font=("times new roman",10),command=delete,bg="white").place(x=160,y=500)
    b6=Button(top,width=10,bd=10,text="ADD",font=("times new roman",11),command=add,bg="white").place(x=20,y=500)
    b7=Button(top,width=30,bd=5,text="BACK",font=("times new roman",15),bg="white",command=page2,image=im1).place(x=10,y=15)
    b8=Button(top,width=18,bd=10,text="REPORT",font=("times new roman",10),bg="white",command=csv_report).place(x=60,y=15)


    frame2=Frame(top,height=620,width=940,highlightbackground="black",highlightthickness=1,bg="white").place(x=400,y=60)

    #combobox = Combobox(frame2,values=[]).place(x=620, y=75)
    l31 = tk.Label(frame2, text="DEPARTMENT",font=("times new roman", 20),bg="white").place(x=420, y=70)
    e11=Entry(top,width=15,font=20,textvariable=search11,bg="light blue").place(x=780,y=75)
    b8=Button(frame2,width=15,bd=5,text="SEARCH",font=("times new roman",10),command=search1,bg="white").place(x=925,y=70)
    b9=Button(frame2,width=15,bd=5,text="SHOW ALL",font=("times new roman",10),command=show,bg="white").place(x=1050,y=70)
    b10=Button(frame2,width=15,bd=2,text="search",font=("times new roman",10),command=search2,bg="white").place(x=200,y=120)

    treev = ttk.Treeview(frame2,height=5, selectmode='extended')
    treev.place(x=420, y=130,width=900,height=550)
    verscrlbar = ttk.Scrollbar(frame2, orient="horizontal", command=treev.xview)
    verscrlbar.place(x=405, y=670,width=930)
    treev.configure(xscrollcommand=verscrlbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6","7","8","9","10","11","12")
    treev['show'] = 'headings'

    treev.column("1", width=90, anchor='c')
    treev.column("2", width=90, anchor='se')
    treev.column("3", width=90, anchor='se')
    treev.column("4", width=90, anchor='se')
    treev.column("5", width=90, anchor='se')
    treev.column("6", width=90, anchor='se')
    treev.column("7", width=90, anchor='se')
    treev.column("8", width=90, anchor='se')
    treev.column("9", width=90, anchor='se')
    treev.column("10", width=90, anchor='se')
    treev.column("11", width=90, anchor='se')
    treev.column("12", width=90, anchor='se')

    #treev.bind("<Double-1>",ondoubleclick)

    treev.heading("1", text="EMPLOYEE_ID", anchor=CENTER)
    treev.heading("2", text="DEPARTMENT", anchor=CENTER)
    treev.heading("3", text="NAME", anchor=CENTER)
    treev.heading("4", text="EMAIL", anchor=CENTER)
    treev.heading("5", text="GENDER", anchor=CENTER)
    treev.heading("6", text="D.O.B", anchor=CENTER)
    treev.heading("7", text="D.O.J", anchor=CENTER)
    treev.heading("8", text="PROOF_NO", anchor=CENTER)
    treev.heading("9", text="ADDRESS", anchor=CENTER)
    treev.heading("10", text="PROOF_TYPE", anchor=CENTER)
    treev.heading("11", text="CONTACT_NO", anchor=CENTER)
    treev.heading("12", text="PHOTO_SAMPLE", anchor=CENTER)


    treev.column("1", stretch=YES, minwidth=30, width=70)
    treev.column("2", stretch=YES, minwidth=30, width=70)
    treev.column("3", stretch=YES, minwidth=30, width=70)
    treev.column("4", stretch=YES, minwidth=30, width=70)
    treev.column("5", stretch=YES, minwidth=30, width=70)
    treev.column("6", stretch=YES, minwidth=30, width=70)
    treev.column("7", stretch=YES, minwidth=30, width=70)
    treev.column("8", stretch=YES, minwidth=30, width=70)
    treev.column("9", stretch=YES, minwidth=30, width=70)
    treev.column("10", stretch=YES, minwidth=30, width=70)
    treev.column("11", stretch=YES, minwidth=30, width=70)
    treev.column("12", stretch=YES, minwidth=30, width=70)

    treev.bind("<Double-1>",ondoubleclick)
    show()
    top.mainloop()
    
def page4():
    
     def ondoubleclick(event):
        item=treev.selection()[0]
        a=treev.item(item,"text")
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        cur.execute("select * from department_management where DID='%s'"%(a))
        result=cur.fetchall()
        
        for row in result:
            did=row[0]
            did1.set(did)
            dname=row[1]
            dname1.set(dname)
        myconn.rollback()
        myconn.close()
        print("running")


     def save():
        did=did1.get()
        dname=dname1.get()
        msg=searchbyname()
        if(msg=="no found"):
        
            myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
            cur=myconn.cursor()
            print(did,dname)
            sql = "insert into department_management(DID,DNAME)value(%s,%s)"
            val = (did,dname)
            myresult=cur.execute(sql,val)
            myconn.commit()
            messagebox.showinfo("department","RECORD SAVED")
            myconn.close()
            show()
            clear()
    
        else:
            messagebox.showinfo("department","already exist")
        
     def delete():
        did=did1.get()
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        sql="delete from department_management where DID='%s'"%(did)
        val=(sql)
        cur.execute(sql)
        myconn.commit()
        messagebox.showinfo("department_management","RECORD DELETED")
        print(cur.rowcount, "record deleted!")
        myconn.close()  
        show()
        clear()
    
     def show():
        for i in treev.get_children():
            treev.delete(i)
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
        cur = myconn.cursor()
        sql=("select *  from department_management ORDER BY DID DESC")
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            treev.insert('',0, text=row[0], values=(row[0],row[1]))
        myconn.rollback()
        myconn.close()

     def fill():
        myconn=mysql.connector.connect(host="localhost",user="root",database=("face_project"))
        cur=myconn.cursor()
        sql=("select DNAME from department_management")
        cur.execute(sql)
        result=cur.execute(sql)
        myconn.commit()
        myconn.close()
    
     def SEARCH1():
        for i in treev.get_children():
            treev.delete(i)
   
        did=did1.get(),
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project") 
        cur = myconn.cursor()
        sql="select * from department_management where DID='%s'" % (did)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            treev.insert('',0, text=row[0], values=(row[0],row[1]))
            
        for row in result:
            did=row[0]
            did1.set(did)
            dname=row[1]
            dname1.set(dname)
        myconn.rollback()
        myconn.close()
        print("running")


     def update():
        did=did1.get()
        dname=dname1.get()
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        print("code runnning")
        sql="update department_management set DNAME='%s' where DID='%s'" %(dname,did)
        cur.execute(sql)
        myconn.commit()
        messagebox.showinfo("department_management","RECORD UPDATED")

        print(cur.rowcount,"record updated")
        myconn.close()
        show()
        clear()

     def clear():
        did1.set('')
        dname1.set('')
        print("amkitt...")

     def searchbyname():
        dname=dname1.get()
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        sql="select * from department_management where DNAME='%s' "%(dname)
        cur.execute(sql)
        result=cur.fetchall()
        msg="no found"
        for row in result:
            msg="found"
        myconn.rollback()
        myconn.close()
        return msg    
        show()

     def csv_report():
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        sql=("select * from department_management")
        cur.execute(sql)
        header=[row[0]for row in cur .description]
        rows= cur.fetchall()
        f=open("department_management" + ".csv","w")
        f.write(','.join(header)+'\n')
        for row in rows:
            f.write(','.join(str(r) for r in row)+'\n')
            
        f.close()
        print(str(len(rows))+'rows written successfully to'+ f.name)
        
        


     did1=StringVar()
     dname1=StringVar()
     var = StringVar(top)
     search1=IntVar()

#frame1=Frame(top,width=430,height=60,highlightbackground="black",highlightthickness=3,bg="grey").place(x=50,y=10)
#frame2=Frame(top,width=530,height=60,highlightbackground="grey",highlightthickness=3,bg="grey").place(x=5,y=185)
#frame3=Frame(top,width=520,height=60,highlightbackground="grey",highlightthickness=3,bg="grey").place(x=5,y=85)
#frame4=Frame(top,width=550,height=60,highlightbackground="grey",highlightthickness=3,bg="grey").place(x=0,y=185)

     bg=PhotoImage(file=r"image//banner1.png")
     myimage=Label(image=bg)
     myimage.place(x=0,y=0)
    
     im1=PhotoImage(file="image//ab.png")
     myimage=Label(image=im1)
    
     frame1=Frame(top,width=460,height=580,highlightbackground="black",highlightthickness=1,bg="white").place(x=420,y=100)


     l2=Label(top,text="DEPARTMENT NAME", font=("times new roman", 15),bg="white").place(x=430,y=170)
     l3=Label(top,text="DEPARTMENT ID", font=("times new roman", 15),bg="white").place(x=430,y=130)
     e3=Entry(top,width=15,font=("times new roman", 15),textvariable=did1,bg="light blue").place(x=640,y=130)


     combobox = Combobox(top,values=[],width=20,height=50,textvariable=fill).place(x=430, y=290)
     l1=Label(frame1,text="DEPARTMENT MANAGEMENT",font=("times new roman", 20),bg="white").place(x=450,y=10)
     e2=Entry(top,width=15,font=("times new roman", 15),textvariable=dname1,bg="light blue").place(x=640,y=170)
    #a=Entry(top,width=15,font=("time new romain",10),textvariable=did1).place(x=550,y=25)

     b10=Button(top,width=11,bd=3,text="REPORT",font=("times new roman",8),bg="white",command=csv_report).place(x=1100,y=127)

     b1=Button(top,width=11,bd=3,text="SEARCH",font=("times new roman",8),bg="white",command=SEARCH1).place(x=800,y=127)
     b2=Button(top,width=15,bd=5,text="SHOW ALL",font=("times new roman",8),bg="white",command=show).place(x=680,y=645)
     b3=Button(top,width=15,bd=5,text="CLEAR",font=("times new roman",8),bg="white",command=clear).place(x=770,y=240)
     b4=Button(top,width=15,bd=5,text="UPDATE",font=("times new roman", 8),bg="white",command=update).place(x=655,y=240)
     b5=Button(top,width=15,bd=5,text="DELETE",font=("times new roman",8),bg="white",command=delete).place(x=430,y=240)
     b6=Button(top,width=15,bd=5,text="ADD",font=("times new roman",8),bg="white",command=save).place(x=545,y=240)
     b7=Button(top,width=30,bd=5,text="BACK",font=("times new roman",15),bg="white",command=page2,image=im1).place(x=15,y=10)
    
     treev = ttk.Treeview(top,height=5, selectmode='extended')
     treev.place(x=620, y=290,width=230,height=350)
#verscrlbar = ttk.Scrollbar(top, orient="horizontal", command=treev.xview)
#verscrlbar.place(x=300, y=670,width=930)
#treev.configure(xscrollcommand=verscrlbar.set)
     treev["columns"] = ("1", "2")
     treev['show'] = 'headings'

     treev.column("1", width=90, anchor='c')
     treev.column("2", width=90, anchor='c')

     treev.heading("1", text="DEPT ID", anchor=CENTER)
     treev.heading("2", text="DEPARTMENT", anchor=CENTER)

     treev.column("1", stretch=YES, minwidth=30, width=70)
     treev.column("2", stretch=YES, minwidth=30, width=70)
     treev.bind("<Double-1>",ondoubleclick)
     show()
     top.mainloop()
    
    
def page5():
    def ondoubleclick(event):
        item=treev.selection()[0]
        a=treev.item(item,"text")
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        cur.execute("select * from attendence where ATTENDENCE_ID='%s'"%(a))
        result=cur.fetchall()
        
        for row in result:
            STUDENT_ID=row[1]
            STUDENT_ID1.set(STUDENT_ID)
            ATTENDENCE_DATE=row[3]
            ATTENDENCE_DATE1.set(ATTENDENCE_DATE)
            ATTENDENCE_STATUS=row[2]
            ATTENDENCE_STATUS1.set(ATTENDENCE_STATUS)
        myconn.rollback()
        myconn.close()
        print("running")
        
    def update():
        STUDENT_ID=STUDENT_ID1.get()
        ATTENDENCE_DATE=ATTENDENCE_DATE1.get()
        ATTENDENCE_STATUS=ATTENDENCE_STATUS1.get()
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        print("code runnning")
        sql="update attendence set ATTENDENCE_DATE='%s' , ATTENDENCE_STATUS='%s' where STUDENT_ID ='%s' " %(ATTENDENCE_DATE,ATTENDENCE_STATUS,STUDENT_ID)
        cur.execute(sql)
        myconn.commit()
        messagebox.showinfo("attendence","RECORD UPDATED")

        print(cur.rowcount,"record updated")
        myconn.close()
        show()
        clear()

    def clear():
        STUDENT_ID1.set('')
        ATTENDENCE_DATE1.set('')
        ATTENDENCE_STATUS1.set('')
        print("amkitt...")

    def save():
        STUDENT_ID=STUDENT_ID1.get()
        ATTENDENCE_DATE=ATTENDENCE_DATE1.get()
        ATTENDENCE_STATUS=ATTENDENCE_STATUS1.get()

        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        print(STUDENT_ID,ATTENDENCE_DATE,ATTENDENCE_STATUS)
        sql = "insert into attendence(STUDENT_ID,ATTENDENCE_DATE,ATTENDENCE_STATUS)value(%s,%s,%s)"
        val = (STUDENT_ID,ATTENDENCE_DATE,ATTENDENCE_STATUS)
        myresult=cur.execute(sql,val)
        myconn.commit()
        myconn.close()
        show()
        clear()
    
       
    def show():
        for i in treev.get_children():
            treev.delete(i)
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
        cur = myconn.cursor()
        sql=("select *  from attendence ORDER BY ATTENDENCE_ID DESC")
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            treev.insert('',0, text=row[0], values=(row[0],row[1],row[2],row[3]))
        myconn.rollback()
        myconn.close()
        
    def SEARCH1():
        for i in treev.get_children():
            treev.delete(i)
        sear=search11.get(),
       
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project") 
        cur = myconn.cursor()
        sql="select * from attendence where STUDENT_ID='%s'" % (sear)
        
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            treev.insert('',0, text=row[0], values=(row[0],row[1], row[2], row[3]))
    
        myconn.rollback()
        myconn.close()
        
    def csv_report():
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        sql=("select * from attendence")
        cur.execute(sql)
        header=[row[0]for row in cur .description]
        rows= cur.fetchall()
        f=open("attendence" + ".csv","w")
        f.write(','.join(header)+'\n')
        for row in rows:
            f.write(','.join(str(r) for r in row)+'\n')
            
        f.close()
        print(str(len(rows))+' rows written successfully to '+ f.name)
        
    ATTENDENCE_ID1=StringVar()
    STUDENT_ID1=StringVar()
    ATTENDENCE_DATE1=StringVar()
    ATTENDENCE_STATUS1=StringVar()
    search11=StringVar()
    
    bg=PhotoImage(file=r"image//banner1.png")
    myimage=Label(image=bg)
    myimage.place(x=0,y=0)
    

    im1=PhotoImage(file="image//ab.png")
    myimage=Label(image=im1)


    frame1=Frame(top,width=350,height=270,highlightbackground="black",highlightthickness=1,bg="white").place(x=10,y=80)
    frame10=Frame(top,width=350,height=50,highlightbackground="black",highlightthickness=1,bg="white").place(x=10,y=80)
    frame4=Frame(top,width=350,height=150,highlightbackground="black",highlightthickness=1,bg="white").place(x=10,y=360)
    frame5=Frame(top,width=350,height=40,highlightbackground="black",highlightthickness=1,bg="white").place(x=10,y=360)
    frame6=Frame(top,width=350,height=120,highlightbackground="black",highlightthickness=1,bg="white").place(x=10,y=560)
    frame7=Frame(top,width=350,height=50,highlightbackground="black",highlightthickness=1,bg="white").place(x=10,y=550)
    frame8=Frame(top,height=600,width=940,highlightbackground="black",highlightthickness=1,bg="white").place(x=400,y=70)
    frame9=Frame(top,height=50,width=940,highlightbackground="black",highlightthickness=1,bg="white").place(x=400,y=70)

    l1= Label(top,text="ATTENDANCE REPORT", font=("times new roman", 20),bg="white").place(x=500,y=5)
    l2 = Label(top,text="UPDATE ATTENDANCE", font=("times new roman", 15),bg="white").place(x=50,y=100)
    l7= Label(top,text="EXPORT IN EXCEL FILE", font=("times new roman", 15),bg="white").place(x=70,y=370)
    l8= Label(top,text="DELETE ATTENDANCE REPORT", font=("times new roman", 15),bg="white").place(x=30,y=570)

    #combobox = Combobox(top,values=[], font=("times new roman", 10)).place(x=550, y=83)
    l11 = tk.Label(top, text="SEARCH BY", font=("times new roman", 15)).place(x=420, y=80)
    e11=Entry(top,width=15,font=20,bg="light blue").place(x=550,y=83)
    b6=Button(top,width=15,bd=5,text="SEARCH",font=("times new roman",10),bg="white",command=SEARCH1).place(x=700,y=78)
    b7=Button(top,width=15,bd=5,text="SHOW ALL",font=("times new roman",10),bg="white",command=show).place(x=830,y=78)
    b8=Button(top,width=15,bd=5,text="TODAY'S REPORT",font=("times new roman",10),bg="white",command=csv_report).place(x=960,y=78)
    b9=Button(top,width=30,bd=5,text="BACK",font=("times new roman",15),bg="white",command=page2,image=im1).place(x=10,y=10)
    b10=Button(top,width=15,bd=5,text="REPORT TYPE",font=("times new roman",10),bg="white",command=type_report).place(x=1090,y=78)

   
    l9= Label(top,text="SELECT DATE", font=("times new roman", 10)).place(x=30,y=615)
    combobox = Combobox(top,values=[]).place(x=200, y=615)

    l3=Label(top,text="STUDENT ID").place(x=30,y=180) 
    e1=Entry(top,width=23,bg="light blue",textvariable=STUDENT_ID1).place(x=200,y=180)

    l5=Label(top,text="ATTENDANCE STATUS").place(x=30,y=240)
    combobox = Combobox(top,values=['PRESENT','LEAVE','ABSENT'],textvariable=ATTENDENCE_STATUS1).place(x=200,y=240)


    l6=Label(top,text="DATE(dd-mm-yy)").place(x=30,y=270) 
    e3=Entry(top,width=23,bg="light blue",textvariable=ATTENDENCE_DATE1).place(x=200, y=270)


    l8=Label(top,text="DATE(dd-mm-yy)").place(x=30,y=410)
    e4=Entry(top,width=23,bg="light blue").place(x=200,y=410)

    b1=Button(top,width=10,bd=5,text="UPDATE",font=("times new roman",10),bg="white",command=update).place(x=30,y=300)
    b6=Button(top,width=10,bd=5,text="ADD",font=("times new roman",10),bg="white",command=save).place(x=130,y=300)
    b2=Button(top,width=10,bd=5,text="CLEAR",font=("times new roman",10),bg="white",command=clear).place(x=230,y=300)
    b4=Button(top,width=25,bd=5,text="EXPORT AS CURRRENT DATE",font=("times new roman",10),bg="white").place(x=70,y=475)
    b5=Button(top,width=25,bd=5,text="DELETE RECORD",font=("times new roman",10),bg="white").place(x=70,y=645)

    treev = ttk.Treeview(top,height=5, selectmode='extended')
    treev.place(x=420, y=130,width=900,height=520)
    
    treev["columns"] = ("1", "2", "3", "4")
    treev['show'] = 'headings'

    treev.column("1", width=90, anchor='c')
    treev.column("2", width=90, anchor='c')
    treev.column("3", width=90, anchor='c')
    treev.column("4", width=90, anchor='c')
    
    treev.heading("1", text="ATTENDANCE ID", anchor=CENTER)
    treev.heading("2", text="STUDENT ID", anchor=CENTER)
    treev.heading("3", text="ATTENDANE STATUS", anchor=CENTER)
    treev.heading("4", text="DATE", anchor=CENTER)

    treev.column("1", stretch=YES, minwidth=30, width=70)
    treev.column("2", stretch=YES, minwidth=30, width=70)
    treev.column("3", stretch=YES, minwidth=30, width=70)
    treev.column("4", stretch=YES, minwidth=30, width=70)   
    treev.bind("<Double-1>",ondoubleclick)

    show()
    top.mainloop()

def page6():
    def update():
    
        old=oldpassword1.get()
        user=username1.get()
        new=newpassword1.get()
        
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        print("code runnning")
        sql="update login_page set  PASSWORD='%s' where USERNAME='%s' and PASSWORD='%s' "%(new,user,old)
        myresult=cur.execute(sql)
        myconn.commit()
        messagebox.showinfo("password","password UPDATED")
        print(cur.rowcount,"record updated")
        myconn.close()  

    im1=PhotoImage(file="image//ab.png")
    myimage=Label(image=im1)
    
    bg=PhotoImage(file=r"image//banner1.png")
    myimage=Label(image=bg)
    myimage.place(x=0,y=0)
    
    username1=StringVar()
    oldpassword1=StringVar()
    newpassword1=StringVar()

    frame1=Frame(top,width=460,height=420,highlightbackground="black",highlightthickness=1,bg="white").place(x=420,y=100)
    fame10=Frame(top,width=452,height=50,highlightbackground="lightblue",highlightthickness=1,bg="lightblue").place(x=425,y=100)
    
    l1=Label(top,text="!OLD PASSWORD",font=("times new roman bold", 15),bg="white").place(x=440,y=250)
    e1=Entry(top,show="*",width=17,bd=5,font=("times new roman",15),textvariable=oldpassword1).place(x=650,y=250)


    l2=Label(top,text="!NEW PASSWORD",font=("times new roman bold", 15),bg="white").place(x=440,y=320)
    e2=Entry(top,show="*",width=17,bd=5,font=("times new roman",15),textvariable=newpassword1).place(x=650,y=320)

    l3=Label(top,text="@ USERNAME",font=("times new roman bold", 15),bg="white").place(x=440,y=180) 
    e3=Entry(top,width=17, bd=5, font=("times new roman", 15),textvariable=username1).place(x=650,y=180)

    l4=Label(top,text="CHANGE PASSWORD",font=("times new roman bold", 20),bg="lightblue").place(x=510,y=105)
    
    b1=Button(top,width=17,bd=5,text="SAVE",font=("times new roman",15),bg="white",command=update).place(x=530,y=400)
    b7=Button(top,width=30,bd=5,text="BACK",font=("times new roman",15),bg="white",command=page2,image=im1).place(x=10,y=10)

    top.mainloop()
 

def report():
    
    bg=PhotoImage(file=r"image//banner1.png")
    myimage=Label(image=bg)
    myimage.place(x=0,y=0)
     

    im1=PhotoImage(file="image//ab.png")
    myimage=Label(image=im1)
  
    im2=PhotoImage(file="image//sale-report (1).png")
    myimage=Label(image=im2)  
  
    im3=PhotoImage(file="image//data.png")
    myimage=Label(image=im3)
    
    im4=PhotoImage(file="image//diagram.png")
    myimage=Label(image=im4)
    
    frame1=Frame(top,width=500,height=520,highlightbackground="black",highlightthickness=1,bg="white").place(x=380,y=100)
    
    fame10=Frame(top,width=500,height=100,highlightbackground="lightblue",highlightthickness=1,bg="lightblue").place(x=380,y=100)
        
    bg1=PhotoImage(file=r"image//statistics.png")
    myimage=Label(image=bg1)
    myimage.place(x=430,y=120)
    
    l1=Label(top,text="DATA ANALYTICS",font=("times new roman bold", 25),bg="lightblue").place(x=500,y=120)

    b1=Button(top,width=145,bd=6,text="DEPARTMENT" '\n' " REPORT",font=("times new roman",10),bg="white",height=145,command=department_report,image=im2).place(x=450,y=250)
    b2=Button(top,width=145,bd=5,text="EMPLOYEE" '\n' " REPORT",font=("times new roman",10),height=145,bg="white",command=employee_report,image=im3).place(x=650,y=250)
    b3=Button(top,width=145,bd=5,text="ATTENDANCE" '\n'" REPORT",font=("times new roman",10),height=145,bg="white",image=im4).place(x=550,y=450)
    b4=Button(top,width=30,bd=5,text="BACK",font=("times new roman",15),bg="white",command=page2,image=im1).place(x=10,y=10)
    l3=Label(top,width=14,text="DEPARTMENT" '\n' " REPORT",font=("times new roman bold", 13),bg="lightgrey").place(x=455,y=355)
    l4=Label(top,width=14,text="EMPLOYEE" '\n' " REPORT",font=("times new roman bold", 13),bg="lightgrey").place(x=655,y=355)
    l5=Label(top,width=14,text="ATTENDANCE" '\n'" REPORT",font=("times new roman bold", 13),bg="lightgrey").place(x=555,y=560)

    
    frame2=Frame(top,width=200,height=155,highlightbackground="black",highlightthickness=1,bg="white").place(x=950,y=100)
    frame3=Frame(top,width=200,height=53,highlightbackground="black",highlightthickness=1,bg="lightblue").place(x=950,y=200)

    combobox = Combobox(top,values=['BAR','PIE','LINE','SCATTER','HISTOGRAM'],textvariable=chart).place(x=970, y=100)
    l2=Label(top,text="TYPES" '\n' "OF GRAPHS ",font=("times new roman bold", 15),bg="lightblue").place(x=980,y=200)

    top.mainloop()
        #b9=Button(top,width=145,bd=6,font=("arial",10),bg="WHITE",height=145,command=quit,image=im10).place(x=700,y=480)

    
def department_report():
    global chart
    check=chart.get()
    
    myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
    cur = myconn.cursor()
    sql=("select DEPARTMENT, count(DEPARTMENT)  from employee_department group by DEPARTMENT")
    cur.execute(sql)
    result = cur.fetchall()
    Name=[]
    Data=[]
    for row in result:
        Name.append(row[0])
        Data.append(row[1])
    #myconn.rollback()
    #myconn.close()adminadmin1
    print(Name)
    print(Data)       
    myconn.rollback()
    myconn.close()
    if(check=="BAR"):
        plt.bar(Name,Data)
        plt.show()

    elif(check=="PIE"):
        #colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        plt.pie(Data,labels=Name,autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
        
    elif(check=="LINE"):
         myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
         cur = myconn.cursor()
         sql=("select  EMPLOYEE_ID, count(EMPLOYEE_ID)  from employee_department group by EMPLOYEE_ID")
         cur.execute(sql)
         result = cur.fetchall()
         Name=[]
         Data=[]
         for row in result:
             Name.append(row[0])
             Data.append(row[1])
    #myconn.rollback()
             print(Name)
             print(Data)       
         myconn.rollback()
         myconn.close()
    
         plt.plot(Name,label=Data,color='r')
         
         plt.show()
        
    elif(check=="SCATTER"):
        
        plt.scatter(Name,Data)
        plt.show()
        
    elif(check=="HISTOGRAM"):
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
        cur = myconn.cursor()
        sql=("select   DEPARTMENT, count(DEPARTMENT)  from employee_department group by DEPARTMENT")
        cur.execute(sql)
        result = cur.fetchall()
        Name=[]
        Data=[]
        for row in result:
            Name.append(row[0])
            Data.append(row[1])
    
            print(Name)
            print(Data)       
        myconn.rollback()
        myconn.close()
         
        plt.hist(Name,label=Data)
        plt.show()
        
    
    #top.mainloop()
 
def employee_report():
    
    global chart
    check=chart.get()
    if(check=="BAR"):
         myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
         cur = myconn.cursor()
         sql=("select DEPARTMENT, count(DEPARTMENT)  from employee_department group by DEPARTMENT")
         cur.execute(sql)
         result = cur.fetchall()
         Name=[]
         Data=[]
         for row in result:
             Name.append(row[0])
             Data.append(row[1])
    #myconn.rollback()
             print(Name)
             print(Data)       
         myconn.rollback()
         myconn.close()
         plt.bar(Name,Data)
         plt.show()
         
    elif(check=="PIE"):
         myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
         cur = myconn.cursor()
         sql=("select DEPARTMENT, count(DEPARTMENT)  from employee_department group by DEPARTMENT")
         cur.execute(sql)
         result = cur.fetchall()
         Name=[]
         Data=[]
         for row in result:
             Name.append(row[0])
             Data.append(row[1])
    #myconn.rollback()
             print(Name)
             print(Data)       
         myconn.rollback()
         myconn.close()
        #colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
         plt.pie(Data,labels=Name,autopct='%1.1f%%')
        #plt.axis('equal')
         plt.show()
    elif(check=="LINE"):
         myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
         cur = myconn.cursor()
         sql=("select  DNAME, count(DNAME)  from department_management group by DNAME")
         cur.execute(sql)
         result = cur.fetchall()
         Name=[]
         Data=[]
         for row in result:
             Name.append(row[0])
             Data.append(row[1])
    #myconn.rollback()
             print(Name)
             print(Data)       
         myconn.rollback()
         myconn.close()
    
         plt.plot(Name,label=Data,color='r')
    
         
         plt.show()
          
    elif(check=="SCATTER"):
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
        cur = myconn.cursor()
        sql=("select   DNAME, count(DNAME)  from department_management group by DNAME")
        cur.execute(sql)
        result = cur.fetchall()
        Name=[]
        Data=[]
        for row in result:
            Name.append(row[0])
            Data.append(row[1])
    
            print(Name)
            print(Data)       
        myconn.rollback()
        myconn.close()
         
        plt.scatter(Name,Data)
        plt.show()
    elif(check=="HISTOGRAM"):
        myconn = mysql.connector.connect(host="localhost", user="root", database="face_project")
        cur = myconn.cursor()
        sql=("select   DNAME, count(DNAME)  from department_management group by DNAME")
        cur.execute(sql)
        result = cur.fetchall()
        Name=[]
        Data=[]
        for row in result:
            Name.append(row[0])
            Data.append(row[1])
    
            print(Name)
            print(Data)       
        myconn.rollback()
        myconn.close()
         
        plt.hist(Name,label=Data,aligen='center')
        plt.show()
    top.mainloop()
      
def type_report():
    
    def csv_report():
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        sql=("select * from attendence")
        cur.execute(sql)
        header=[row[0]for row in cur .description]
        rows= cur.fetchall()
        f=open("attendence" + ".csv","w")
        f.write(','.join(header)+'\n')
        for row in rows:
            f.write(','.join(str(r) for r in row)+'\n')
            
        f.close()
        print(str(len(rows))+' rows written successfully to '+ f.name)
        
        
    def txt_report():
        myconn=mysql.connector.connect(host="localhost",user="root",database="face_project")
        cur=myconn.cursor()
        sql=("select * from attendence")
        cur.execute(sql)
        header=[row[0]for row in cur .description]
        rows= cur.fetchall()
        f=open("attendence" + ".txt","w")
        f.write(','.join(header)+'\n')
        for row in rows:
            f.write(','.join(str(r) for r in row)+'\n')
            
        f.close()
        print(str(len(rows))+' rows written successfully to '+ f.name)
    
            
        f.close()
        print(str(len(rows))+' rows written successfully to '+ f.name)
    
    bg=PhotoImage(file=r"image//banner1.png")
    myimage=Label(image=bg)
    myimage.place(x=0,y=0)
    
    im1=PhotoImage(file="image//ab.png")
    myimage=Label(image=im1)
    frame1=Frame(top,width=470,height=300,highlightbackground="black",highlightthickness=1,bg="lightyellow").place(x=395,y=150)
    
    #bg1=PhotoImage(file=r"D:\\New folder\\New folder\\image\\Webp.net-resizeimage (2).png")
    #myimage=Label(image=bg)
    #myimage.place(x=0,y=0)
    
    b1=Button(top,width=20,bd=6,text="CSV FILE",font=("times new roman",10),bg="lightblue",height=5,command=csv_report).place(x=450,y=250)
    b2=Button(top,width=20,bd=6,text="TEXT FILE",font=("times new roman",10),bg="lightblue",height=5,command=txt_report).place(x=650,y=250)
    b7=Button(top,width=30,bd=5,text="BACK",font=("times new roman",15),bg="white",command=page5,image=im1).place(x=15,y=10)

    top.mainloop()


def quit():
    top.destroy()

login_page()
top.mainloop()