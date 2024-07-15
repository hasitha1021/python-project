from tkinter import *
from tkinter.ttk import *
window1= Tk()
window1.geometry("500x500")
window1.resizable(height=False,width=False)
def p(valuve):
    previous = lbl2.get()
    lbl2.delete(0,END)
    lbl2.insert(0,previous+valuve)

lbl1=Label(window1,text="s16310")
lbl1.grid(row=0)
lbl2=Entry(window1)
lbl2.grid(row=1)

frame1=Frame(window1)
frame1.grid(row=2)
btn1=Button(frame1,text="H",command=lambda :p("H"))
btn1.grid(row=0,column=0)
btn2=Button(frame1,text="A",command=lambda :p("A"))
btn2.grid(row=0,column=1)
btn3=Button(frame1,text="S",command=lambda :p("S"))
btn3.grid(row=0,column=2)
btn4=Button(frame1,text="I",command=lambda :p("I"))
btn4.grid(row=1,column=0)
btn5=Button(frame1,text="T",command=lambda :p("T"))
btn5.grid(row=1,column=1)
btn6=Button(frame1,text="E",command=lambda :p("E"))
btn6.grid(row=1,column=2)
btn7=Button(frame1,text="k",command=lambda :p("K"))
btn7.grid(row=2,column=0)
btn8=Button(frame1,text="N",command=lambda :p("N"))
btn8.grid(row=2,column=1)
btn9=Button(frame1,text="Y",command=lambda :p("Y"))
btn9.grid(row=2,column=2)
btn10=Button(frame1,text="Space",command=lambda :p(" "))
btn10.grid(row=3,column=0)
btn11=Button(frame1,text="Reverse")
btn11.grid(row=3,column=1)

lbl3=Label(window1,text="HASITHA EKANAYAKA")
lbl3.grid(row=3)

frame2=Frame(window1)
frame2.grid(row=4)
lbl4=Label(frame2,text="select the display color")
lbl4.grid(row=0,column=0)
lbl5=Label(frame2,background="red")
lbl5.grid(row=0,column=1)
lbl6=Label(frame2,background="blue")
lbl6.grid(row=0,column=2)
lbl7=Label(frame2,background="yellow")
lbl7.grid(row=0,column=3)
lbl8=Label(frame2,background="green")
lbl8.grid(row=0,column=4)









window1.mainloop()