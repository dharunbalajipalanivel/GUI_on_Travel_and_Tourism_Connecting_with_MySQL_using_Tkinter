import tkinter
import time
from tkinter import *
import mysql.connector as mc
from datetime import date
tk=Tk()
con=mc.connect(host="localhost",
               user="root",
               password="system",
               database="details")
if con.is_connected==True:
    print("It is connected")
heading=tkinter.Label(text="TRAVEL AND TOURISM",
                      font="Times 22 bold",
                      fg="#01dc73",
                      bg="#8901be")
heading.place(x=75, y=0)
width_of_window=480
height_of_window=660
screen_width=tk.winfo_screenwidth()
screen_height=tk.winfo_screenheight()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)
tk.geometry("%dx%d+%d+%d"%(width_of_window,
                           height_of_window,
                           x_coordinate,
                           y_coordinate))
tk.title("Registration Form")
today=date.today()
dt=today.strftime("%d/%m/%y")
heading2=tkinter.Label(text="DATE : ", bg="#abcdef")
heading4=tkinter.Label(text="TIME : ")
heading2.place(x=25, y=40)
heading4.place(x=250, y=40)
time=time.strftime("%H:%M:%S")
timer=tkinter.Label(text=time, 
                    width=20,
                    borderwidth=3,
                    relief="groove",
                    bg="#3385ae")
timer.place(x=300, y=40)
lldate=tkinter.Label(text=dt,
                     width=20,
                     borderwidth=3,
                     relief="groove",
                     bg="#da658c")
lldate.place(x=75, y=40)
tk.configure(bg="#73edda")
def saveme():
    fninfo=fnentry.get()
    lninfo=ltentry.get()
    ageinfo=ageentry.get()
    genderinfo=genderentry.get()
    fromplaceinfo=fromplaceentry.get()
    toplaceinfo=toplaceentry.get()
    descriptioninfo=descriptionentry.get()
    busamountinfo=busentry.get()
    trainamountinfo=trainentry.get()
    stayamountinfo=stayentry.get()
    foodamountinfo=foodentry.get()
    childinfo=childentry.get()
    adultinfo=adultentry.get()
    dayinfo=dayentry.get()
    nightinfo=nightentry.get()
    noofticketsinfo=noofticketsentry.get()
    emailinfo=emailentry.get()
    phonenoinfo=phonenoentry.get()
    cr=con.cursor()
    #cr.execute("create table customer(firstname varchar(30),lastname varchar(30),age varchar(5), gender varchar(10),fromplace varchar(100),toplace varchar(100),description varchar(100),busamount varchar(5),trainamount varchar(10),stayamount varchar(10),foodamount varchar(40),child varchar(6),adult varchar(7),day varchar(5),night varchar(5), nooftickets varchar(3),email varchar(50),phoneno varchar(10))") 
    a=(fninfo,lninfo,ageinfo,genderinfo,
       fromplaceinfo,toplaceinfo,descriptioninfo,
       busamountinfo,trainamountinfo,stayamountinfo,
       foodamountinfo,childinfo,adultinfo,dayinfo,nightinfo,
       noofticketsinfo,emailinfo,phonenoinfo)
    b="insert into customer values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(b,a)
    print("Registered Successfully")
    con.commit()
    fnentry.delete(0, END)
    ltentry.delete(0, END)
    ageentry.delete(0, END)
    genderentry.delete(0, END)
    fromplaceentry.delete(0, END)
    toplaceentry.delete(0, END)
    descriptionentry.delete(0, END)
    busentry.delete(0, END)
    trainentry.delete(0, END)
    stayentry.delete(0, END)
    foodentry.delete(0, END)
    childentry.delete(0, END)
    adultentry.delete(0, END)
    dayentry.delete(0, END)
    nightentry.delete(0, END)
    noofticketsentry.delete(0, END)
    emailentry.delete(0, END)
    phonenoentry.delete(0, END)

fntxt=tkinter.Label(text="FIRST NAME :")
ltxt=tkinter.Label(text="LAST NAME :")
agetxt=tkinter.Label(text="AGE :")
gentxt=tkinter.Label(text="GENDER :")
fromplacetxt=tkinter.Label(text="FROM DESTINATION  :")
toplacetxt=tkinter.Label(text="TO DESTINATION   :")
placetxt=tkinter.Label(text="ADD PLACE   :")
descriptiontxt=tkinter.Label(text="DESCRIPTION  :")
busamounttxt=tkinter.Label(text="BUS AMOUNT  :")
trainamounttxt=tkinter.Label(text="TRAIN AMOUNT  :")
stayamounttxt=tkinter.Label(text="STAY AMOUNT   :")
foodamounttxt=tkinter.Label(text="FOOD AMOUNT  :")
childtxt=tkinter.Label(text="NUMBER OF CHILDREN  :")
adulttxt=tkinter.Label(text="NUMBER OF ADULT  :")
daytxt=tkinter.Label(text="NUMBER OF DAYS  :")
nighttxt=tkinter.Label(text="NUMBER OF NIGHTS   :")
nooftickettxt=tkinter.Label(text="NUMBER OF TICKETS  :")
gmailtxt=tkinter.Label(text="EMAIL ID  : ")
phnotxt=tkinter.Label(text="PHONE NUMBER  :")

fntxt.place(x=15, y=70)
ltxt.place(x=15, y=100)
agetxt.place(x=15, y=130)
gentxt.place(x=15, y=160)
fromplacetxt.place(x=15, y=190)
toplacetxt.place(x=15, y=220)
descriptiontxt.place(x=15, y=250)
busamounttxt.place(x=15, y=280)
trainamounttxt.place(x=15, y=310)
stayamounttxt.place(x=15, y=340)
foodamounttxt.place(x=15, y=370)
childtxt.place(x=15, y=400)
adulttxt.place(x=15, y=430)
daytxt.place(x=15, y=460)
nighttxt.place(x=15, y=490)
nooftickettxt.place(x=15, y=520)
gmailtxt.place(x=15, y=550)
phnotxt.place(x=15, y=580)

firstname=str()
lastname=str()
age=str()
gender=str()
fromplace=str()
toplace=str()
description=str()
busamount=str()
trainamount=str()
stayamount=str()
foodamount=str()
child=str()
adult=str()
day=str()
night=str()
nooftickets=str()
email=str()
phoneno=str()

fnentry=tkinter.Entry(textvariable=firstname, width='30')
ltentry=tkinter.Entry(textvariable=lastname, width='30')
ageentry=tkinter.Entry(textvariable=age, width='30')
genderentry=tkinter.Entry(textvariable=gender, width='30')
fromplaceentry=tkinter.Entry(textvariable=fromplace, width='30')
toplaceentry=tkinter.Entry(textvariable=toplace, width='30')
descriptionentry=tkinter.Entry(textvariable=description, width='30')
busentry=tkinter.Entry(textvariable=busamount, width='30')
trainentry=tkinter.Entry(textvariable=trainamount, width='30')
stayentry=tkinter.Entry(textvariable=stayamount, width='30')
foodentry=tkinter.Entry(textvariable=foodamount, width='30')
childentry=tkinter.Entry(textvariable=child, width='30')
adultentry=tkinter.Entry(textvariable=adult, width='30')
dayentry=tkinter.Entry(textvariable=day, width='30')
nightentry=tkinter.Entry(textvariable=night, width='30')
noofticketsentry=tkinter.Entry(textvariable=nooftickets, width='30')
emailentry=tkinter.Entry(textvariable=email, width='30')
phonenoentry=tkinter.Entry(textvariable=phoneno, width='30')

fnentry.place(x=180, y=70)
ltentry.place(x=180, y=100)
ageentry.place(x=180, y=130)
genderentry.place(x=180, y=160)
fromplaceentry.place(x=180, y=190)
toplaceentry.place(x=180, y=220)
descriptionentry.place(x=180, y=250)
busentry.place(x=180, y=280)
trainentry.place(x=180, y=310)
stayentry.place(x=180, y=340)
foodentry.place(x=180, y=370)
childentry.place(x=180, y=400)
adultentry.place(x=180, y=430)
dayentry.place(x=180, y=460)
nightentry.place(x=180, y=490)
noofticketsentry.place(x=180, y=520)
emailentry.place(x=180, y=550)
phonenoentry.place(x=180, y=580)

button=Button(tk,text="REGISTER",
              width='10',
              height='1',
              command=saveme)
button.place(x=50, y=610)
button = Button(text="Exit", command=tk.destroy)
button.place(x=150, y=610)
tk.mainloop()