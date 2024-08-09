from tkinter import *
from random import *
from tkinter import messagebox 

man=com=0

def g():
    xx.destroy()
    yy.destroy()
    btn()

def compres():
    global man,com
    if (user=='S' and comp=='P') or (user=='R' and comp=='S') or (user=='P' and comp=='R'):
        man+=1
        user2=Entry(win,font=('arial',20),width=5)
        user2.place(x=130,y=70)
        user2.insert(0,man)
        user2.configure(state='disabled')
        messagebox.showinfo("RPS", "\tYou win...!\t")

    elif(user=='R' and comp=='P') or (user=='P' and comp=='S') or (user=='S' and comp=='R'):
        comp2=Entry(win,font=('arial',20),width=5)
        comp2.place(x=595,y=70)
        com+=1
        comp2.insert(0,com)
        comp2.configure(state='disabled')
        messagebox.showinfo("RPS", "\tYou loose..!\t")

    else:
        messagebox.showinfo("RPS", "\tTie\t")
    z=messagebox.askquestion("RPS", "\tPlay Again....?\t")
    if z=='yes':
        g()
    else:
        win.destroy()

def btn():
    global btn1,btn2,btn3,sub1,qm
    btn1=Button(win,image=r1,border=4,command=rock)
    btn1.place(x=90,y=130)
    btn2=Button(win,image=p1,border=4,command=pap)
    btn2.place(x=90,y=270)
    btn3=Button(win,image=s1,border=4,command=sci)
    sub1=Button(win,image=sub,command=res,state="disabled")
    qm=Label(win,image=qmk)
    btn3.place(x=90,y=410)
    sub1.place(x=290,y=400)
    qm.place(x=470,y=170)


def btndest():
    global btn1,btn2,btn3,qm
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    qm.destroy()

def disab():
    btn1.configure(state='disabled')
    btn2.configure(state='disabled')
    btn3.configure(state='disabled')
    sub1.configure(state='active')
    

def rock():
    btn1.configure(bg='red')
    disab()
    global user
    user='R'

def pap():
     btn2.configure(bg='red')
     disab()
     global user
     user='P'
     
def sci():
     btn3.configure(bg='red')
     disab()
     global user
     user='S'
     

def res():
    U={"R":r,"S":s,"P":p}
    btndest()
    global xx
    xx=Label(win,image=U[user])
    xx.place(x=100,y=200)
    ch1=["R","P","S"]
    ch={'R':PhotoImage(file='rock.png').subsample(1,2),'S':PhotoImage(file='scissor.png').subsample(1,2),'P':PhotoImage(file='paper.png').subsample(1,2)}
    global comp
    comp=choice(ch1)
    global yy
    yy=Label(win,image=U[comp])
    yy.place(x=470,y=200)
    compres()

win=Tk()
win.geometry("750x550+500+150")
win.configure(bg='salmon')
Label(win,text="ROCK-PAPER-SCISSOR GAME",font=('courier',25,'bold'),bg='salmon',fg='blue').place(x=180,y=10)
Label(win,text="USER",font=('courier',20,'bold'),bg='salmon',fg='black').place(x=50,y=70)
Label(win,text="COMPUTER",font=('courier',20,'bold'),bg='salmon',fg='black').place(x=450,y=70)
user1=Entry(win,font=('arial',20),width=3)
user1.place(x=130,y=70)
user1.insert(0,man)
comp1=Entry(win,font=('arial',20),width=3)
comp1.insert(0,com)
comp1.configure(state='disabled')
user1.configure(state='disabled')
comp1.place(x=595,y=70)
r1=PhotoImage(file="rock1.png").subsample(1,1)
p1=PhotoImage(file="paper1.png").subsample(1,1)
s1=PhotoImage(file="scissor1.png").subsample(1,1)
r=PhotoImage(file='rock.png').subsample(1,1)
s=PhotoImage(file='scissor.png').subsample(1,1)
p=PhotoImage(file='paper.png').subsample(1,1)
qmk=PhotoImage(file="qmk.png").subsample(1,1)
sub=PhotoImage(file="sub.png").subsample(1,1)
sub1=Button(win,image=sub,command=res,state="disabled")
btn()
win.mainloop()
