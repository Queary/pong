from tkinter import *
from threading import Thread,Timer
import time
root = Tk()
root.title("Pong")

#направление
cn  = "right";
cx  = 10;
cy  = 25
cy2 = 55
n = "down"

speed = 5;
speed2 = 1;

y = 10;
y2= 100;

#стимул очки
o = 0;

def autoc():
    global cn,cx,c,root,y,y2,cy,cy2,n
    global speed,speed2
    global o,ot
    o+=1;
    c.delete("all")
    ot.configure(text=str(o))
    ot.pack()

    #повышение уровня сложности
    #speed+=0.0001
    #speed2+=0.001
    #попытка оптимизации(провалена)
    #or
    #c.create_oval(40+cx, 25, 70+cx, 55, width=2 outline="white")
    #меняет x
    #старый способ
    """
    if cn == "right":
        if cx < 530:
            cx+=speed;
            #time.sleep(0.05)
        else:
            #if y-30 > cy:
                cn = "left"
            #else:
            #    if cx > 640:
            #        print("faile")
            #        Label(c,text='FAILE', fg='white', bg='black').pack()
            #        return
        #print(cn)
    elif cn == "left":
        #print("on")
        if cx > 10:
            #print(cx)
            cx-=speed;
            #time.sleep(0.05)
        else:
            if y-30 < cy:
                cn = "right"
            else:
                cx-=speed;
                if cx < 0:
                    print("faile")
                    Label(c,text='FAILE', fg='white', bg='black').pack()
                    return
    """
    #новый способ
    if cn == "right":
        cx+=speed;
    if cn == "left":
        cx-=speed;
    if cx > 530:
        cn = "left"
    #if cx > 530 and y>cy and y2<cy2 :
    #    
    if cx < 10 and y<=cy+25 and y2>=cy2-25:
        cn = "right"
    #if cx < 10:
    #    cn = "right"

    
    #FAILE game
    if cx <= -80:
        print("faile")
        Label(c,text='FAILE', fg='white', bg='black').pack()
        return

    
    #меняет y
    #от персонажей(квадратов)
    if n == "down":
        #print((y2-y)/2)
        #print((cy2-cy)/2)
        #print("("+str(y2)+"-"+str(y)+"/2)>("+str(cy2)+"-"+str(cy)+"/2)")
        cx+=speed2
        cy+=speed2
        cy2+=speed2
    if cy2 > 400:
        n = "up"
    if n == "up":
        cx-=speed2
        cy-=speed2
        cy2-=speed2
    if cy == 0:
        n = "down"
    #print(cy2)
    #print(n)
    c.create_rectangle(50, y, 35, y2)
    c.create_rectangle(600, cy+50, 615, cy2-50)
    c.create_oval(40+cx, cy, 70+cx, cy2, width=2)
    Timer(0.0000001,autoc).start()
        

#87 83
def keys(event):
    global y,y2,root,c
    #up
    if event.keycode == 83:
        if y2 < 400:
            y+=10
            y2+=10
    #down
    elif event.keycode == 87:
        if y > 10:
            y-=10
            y2-=10
    c.delete("all")

ot = Label(root,text=o, fg='white', bg='black')
c = Canvas(root, width=640, height=400, bg='white')
c.pack()
root.bind("<KeyPress>",keys)
#Thread(target = autoc).start()
Timer(1,autoc).start()
root.mainloop()

