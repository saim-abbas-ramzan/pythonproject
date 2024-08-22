def addstudent():
    def Submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d:%m:%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification',
                                            'id{} name{} added sucessfully..want to clean the form'.format(id, name),
                                            parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notification', 'Id already exist try another Id..', parent=addroot)
            strr = 'select * from studentdata1'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenmttable.insert('',END,values=vv)
################################################################that used to create  "connect to database" phase
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('student management system')
    addroot.config(bg='silver')
    addroot.iconbitmap('open.ico')
    addroot.resizable(False, False)
    ###########################################add student label that means button like "enter id" etc in welcome section
    idLabel = Label(addroot, text='Enter Id:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idLabel.place(x=10, y=10)

    nameLabel = Label(addroot, text='Enter Name:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    nameLabel.place(x=10, y=70)

    mobileLabel = Label(addroot, text='Enter Mobile:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobileLabel.place(x=10, y=130)

    emailLabel = Label(addroot, text='Enter Email:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emailLabel.place(x=10, y=190)

    addressLabel = Label(addroot, text='Enter Address:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addressLabel.place(x=10, y=250)

    genderLabel = Label(addroot, text='Enter Gender:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderLabel.place(x=10, y=310)

    dobLabel = Label(addroot, text='Enter D.O.B:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    dobLabel.place(x=10, y=370)

    ###########################################add student entry that write user
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    identry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
    ###################################### submit button in welcome section
    submitbtn = Button(addroot, text='submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='white',
                       activeforeground='yellow',
                       bg='khaki', command=Submitadd)
    submitbtn.place(x=150, y=420)

    addroot.mainloop()


########################################## data entry frame buttons relate to its function
def searchstudent():
    def Submitsearch():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d:%m:%Y")
        if (id != ''):
            strr = 'select * from studentdata1 where id=%s'
            mycursor.execute(strr, (id))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (name != ''):
            strr = 'select * from studentdata1 where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (email != ''):
            strr = 'select * from studentdata1 where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (address != ''):
            strr = 'select * from studentdata1 where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (gender != ''):
            strr = 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (dob != ''):
            strr = 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (addeddate != ''):
            strr = 'select * from studentdata1 where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('student management system')
    searchroot.config(bg='silver')
    searchroot.iconbitmap('open.ico')
    searchroot.resizable(False, False)
    ###########################################add student label that means button like "enter id" etc in welcome section
    idLabel = Label(searchroot, text='Enter Id:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idLabel.place(x=10, y=10)

    nameLabel = Label(searchroot, text='Enter Name:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    nameLabel.place(x=10, y=70)

    mobileLabel = Label(searchroot, text='Enter Mobile:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobileLabel.place(x=10, y=130)

    emailLabel = Label(searchroot, text='Enter Email:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emailLabel.place(x=10, y=190)

    addressLabel = Label(searchroot, text='Enter Address:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addressLabel.place(x=10, y=250)

    genderLabel = Label(searchroot, text='Enter Gender:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderLabel.place(x=10, y=310)

    dobLabel = Label(searchroot, text='Enter D.O.B:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    dobLabel.place(x=10, y=370)

    dateLabel = Label(searchroot, text='Enter Date:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    dateLabel.place(x=10, y=430)

    ###########################################add student entry that write user
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
    ###################################### submit button in welcome section
    submitbtn = Button(searchroot, text='submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='white',
                       activeforeground='yellow',
                       bg='khaki', command=Submitsearch)
    submitbtn.place(x=150, y=480)

    searchroot.mainloop()


def deletestudent():
    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','Id deleted sucessfully ...'.format(pp))
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        time = timeval.get()
        date = timeval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,time=%s,date=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,time,date,id))
        con.commit()
        messagebox.showinfo('Notification','id {} modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenmttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x540+220+200')
    updateroot.title('student management system')
    updateroot.config(bg='silver')
    updateroot.iconbitmap('open.ico')
    updateroot.resizable(False, False)
    ###########################################add student label that means button like "enter id" etc in welcome section
    idLabel = Label(updateroot, text='Enter Id:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idLabel.place(x=10, y=10)

    nameLabel = Label(updateroot, text='Enter Name:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    nameLabel.place(x=10, y=60)

    mobileLabel = Label(updateroot, text='Enter Mobile:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobileLabel.place(x=10, y=100)

    emailLabel = Label(updateroot, text='Enter Email:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emailLabel.place(x=10, y=140)

    addressLabel = Label(updateroot, text='Enter Address:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    addressLabel.place(x=10, y=180)

    genderLabel = Label(updateroot, text='Enter Gender:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderLabel.place(x=10, y=220)

    dobLabel = Label(updateroot, text='Enter D.O.B:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    dobLabel.place(x=10, y=260)

    dateLabel = Label(updateroot, text='Enter Date:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    dateLabel.place(x=10, y=300)

    timeLabel = Label(updateroot, text='Enter Time:', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timeLabel.place(x=10, y=340)

    ###########################################add student entry that write user
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=60)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=100)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=140)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=180)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=220)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=260)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=300)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=340)
    ###################################### submit button in welcome section
    submitbtn = Button(updateroot, text='submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='white',
                       activeforeground='yellow',
                       bg='khaki', command=update)
    submitbtn.place(x=150, y=410)

    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()


def sallstudent():      #sall means show all
    print("student show all")
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)


def exportstudent():
    ff = filedialog.asksaveasfile()
    gg = studenmttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenmttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
        dd = ['id','Name','Mobile','Email','Address','Gender','D.O.B','AddedDate','AddedTime']
        df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
        paths = r'{}.csv'.format(ff)
        df.to_csv(paths,index=False)
        messagebox.showinfo('Notification', 'student data is saved{}'.format(paths))


def exitstudent():
    #print("student exit")
    res = messagebox.askyesnocancel('notification', 'do you want to exit?')
    if (res == True):
        root.destroy()


##################################connect to database
def connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification', 'data is incorrect please try again')
            return
        try:
            strr = 'create database studentmangmentsystem1'
            mycursor.execute(strr)
            strr = ' use studentmangmentsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(15),mobile varchar(15),email varchar(15),address varchar(50),gender varchar(15),dob varchar(20),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'database created and Now you are connected to the database----',
                                parent=dbroot)
        except:
            strr = 'use studentmangmentsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'Now you are connected to the database----', parent=dbroot)
            dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('open.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='dimgray')
    ########################################connect label in button
    hostLabel = Label(dbroot, text='Enter Host', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    hostLabel.place(x=10, y=10)
    userLabel = Label(dbroot, text='Enter User', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    userLabel.place(x=10, y=70)
    passwordLabel = Label(dbroot, text='Enter Password', bg='khaki', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
    passwordLabel.place(x=10, y=130)
    ###########################################connectdb entry
    hostval = StringVar()
    # hostval.set('hello')    -> it means if you print with "hello"
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)
    ##############################################connectdb button
    submitbutton = Button(dbroot, text='Submit', font=('roman', 15, 'bold'), bg='khaki', bd=5, width=28,
                          activebackground='white',
                          activeforeground='yellow', command=submitdb)
    submitbutton.place(x=150, y=190)
    dbroot.mainloop()


def tick():
    time_string = time.strftime('%H:%M:%S')
    date_string = time.strftime('%d:%m:%y')
    Clock.config(text='Date :' + date_string + '\n' + 'Time :' + time_string)
    Clock.after(200, tick)


#####################################Intro slider diffrent colors
import random

Colors = ['red', 'green', 'blue', 'yellow', 'pink']
def IntroLabelColorTick():
    fg = random.choice(Colors)
    SliderLabel1.config(fg=fg)
    SliderLabel1.after(2, IntroLabelColorTick)

################################################### ss text word one after another line 640
def IntroLabelTick():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = ''
        SliderLabel1.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel1.config(text=text)
        count += 1
    SliderLabel1.after(200, IntroLabelTick)

from tkinter import *
from tkinter import Toplevel, messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import random
import time

root = Tk()
root.title("student mangment system")
root.config(bg="silver")
root.geometry('1174x700+200+50')
root.iconbitmap('open.ico')
root.resizable(True, True)

########################################################### dataentry frames
DataEntryFrame = Frame(root, bg='silver', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=600)

##########################################write "Welcome"
frontLabel = Label(DataEntryFrame, text="------------Welcome-----------", width=30, font=('arial', 22, 'italic bold'),
                   bg='silver')
frontLabel.pack(side=TOP, expand=True)

###################################################buttons create in data entry frame
addbtn = Button(DataEntryFrame, text='1.  Add Student', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                activebackground='white', relief=RIDGE,
                activeforeground='yellow', command=addstudent)
addbtn.pack(side=TOP, expand=True)
searchbtn = Button(DataEntryFrame, text='2.  Search Student', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                   activebackground='white', relief=RIDGE,
                   activeforeground='yellow', command=searchstudent)
searchbtn.pack(side=TOP, expand=True)
deletebtn = Button(DataEntryFrame, text='3.  Delete Student', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                   activebackground='white', relief=RIDGE,
                   activeforeground='yellow', command=deletestudent)
deletebtn.pack(side=TOP, expand=True)
updatebtn = Button(DataEntryFrame, text='4.  Update Student', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                   activebackground='white', relief=RIDGE,
                   activeforeground='yellow', command=updatestudent)
updatebtn.pack(side=TOP, expand=True)
sallbtn = Button(DataEntryFrame, text='5.  Show All', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                 activebackground='white', relief=RIDGE,
                 activeforeground='yellow', command=sallstudent)
sallbtn.pack(side=TOP, expand=True)
exportbtn = Button(DataEntryFrame, text='6.  Export data', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                   activebackground='white', relief=RIDGE,
                   activeforeground='yellow', command=exportstudent)
exportbtn.pack(side=TOP, expand=True)
exitbtn = Button(DataEntryFrame, text='7.  Exit', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                 activebackground='white', relief=RIDGE,
                 activeforeground='yellow', command=exitstudent)
exitbtn.pack(side=TOP, expand=True)

##########################################################showdata frame
showdataFrame = Frame(root, bg='silver', relief=GROOVE, borderwidth=5)
showdataFrame.place(x=550, y=80, width=620, height=600)

############################################################# show data frame ....uper side id,etc
style = ttk.Style()
style.configure('Treeview.Heading', font=('Roboto', 20, 'bold'), foreground='black')
style.configure('Treeview', font=('times', 15, 'bold'), background='silver', foreground='black')
scroll_x = Scrollbar(showdataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(showdataFrame, orient=VERTICAL)
studenmttable = Treeview(showdataFrame, columns=(
    'Id', 'Name', 'Mobile no', 'Email', 'Addres', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenmttable.xview)
scroll_y.config(command=studenmttable.yview)
studenmttable.heading('Id', text='Id')
studenmttable.heading('Name', text='Name')
studenmttable.heading('Mobile no', text='Mobile no')
studenmttable.heading('Email', text='Email')
studenmttable.heading('Addres', text='Addres')
studenmttable.heading('Gender', text='Gender')
studenmttable.heading('D.O.B', text='D.O.B')
studenmttable.heading('Added Date', text='Added Date')
studenmttable.heading('Added Time', text='Added Time')
studenmttable['show'] = 'headings'
studenmttable.column('Id', width=100)
studenmttable.column('Name', width=200)
studenmttable.column('Mobile no', width=200)
studenmttable.column('Email', width=300)
studenmttable.column('Addres', width=200)
studenmttable.column('Gender', width=100)
studenmttable.column('D.O.B', width=150)
studenmttable.column('Added Date', width=150)
studenmttable.column('Added Time', width=150)
studenmttable.pack(fill=BOTH, expand=1)
######################################################upper slider
ss = 'Welcome to student Mangment system'
count = 0
text = ''
SliderLabel1 = Label(root, text=ss, font=('arial', 20, 'italic bold'), relief=RIDGE, borderwidth=2, width=30,
                     bg='khaki')
SliderLabel1.place(x=180, y=0)
IntroLabelTick()
IntroLabelColorTick()

#######################################################################create clock box
Clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, bg='khaki')
Clock.place(x=0, y=0)
tick()
#########################################connect database buuton
Grid.columnconfigure(root, 0, weight=200)  #similary#these line used for buuton according size
connectbutton = Button(root, text="Connect to Database", width=23, font=('Roboto', 14, 'italic bold'), relief=RIDGE,
                       borderwidth=4, bg='burlywood',
                       activebackground='blue', activeforeground='white', command=connectdb)
connectbutton.grid(row=0, column=0, sticky="e")  ##these line used for buuton according size
root.mainloop()
