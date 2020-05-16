from tkinter import *

def LeftClickBtn(event):
    BMI = float(txt2.get()) / (float(txt1.get()) / 100) ** 2
    if BMI >= 30:
        result = "อ้วนมาก"
    elif BMI >= 25:
        result = "อ้วน"
    elif BMI >= 23:
        result = "น้ำหนักเกิน"
    elif BMI >= 18.5:
        result = "น้ำหนักปกติ เหมาะสม"
    else:
        result = "ผอมเกินไป"
    print(BMI)
    labelBMI.configure(text=str(BMI))
    print(result)
    labelresult.configure(text=result)

mainwin = Tk()
mainwin.title = "BMI"
labelheight = Label(mainwin,text="ส่วนสูง<cm.>").grid(row=0,column=0)
txt1 = Entry(mainwin)
labelweight = Label(mainwin,text="น้ำหนัก<kg.>").grid(row=1,column=0)
txt2 = Entry(mainwin)
BMIbtn = Button(mainwin,text="Click Me")
BMIbtn.grid(row=2)
txt1.grid(row=0,column=1)
txt2.grid(row=1,column=1)
labelBMI = Label(mainwin,text="ผลลัพธ์")
labelBMI.grid(row=2,column=1)
labelresult = Label(mainwin,text="ผลลัพธ์",font=("Tahoma",16))
labelresult.grid(row=3,column=1)
BMIbtn.bind('<Button-1>',LeftClickBtn)
BMIbtn.grid(row=2,column=0)
mainwin.mainloop()
