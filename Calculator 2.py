from tkinter import*
import math

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

def btnModulus():
    global operator
    operator = operator + "%"
    text_Input.set(operator)

def sqrts():
    global root
    root = root + "^1/2" 
    text_Input.set(root)



cal = Tk()
cal.title("Calculator")
operator=""
text_Input= StringVar()

txtDisplay= Entry(cal,font=("arial", 20, 'bold'), textvariable=text_Input, bd=64, insertwidth=1,bg="gray", justify='right').grid(columnspan=1000)

#xxxxxxxxxxxSECOND ROWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

btn7=Button(cal,padx=20,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="7",bg="black",command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(cal,padx=16,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="8", bg="black",command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(cal,padx=16.5,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="9", bg="black",command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(cal,padx=21.25,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="+", bg="black",command=lambda:btnClick("+")).grid(row=2,column=3)

btnop1=Button(cal,padx=13.5,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="^", bg="black",command=lambda:btnClick("**")).grid(row=2,column=4)

#xxxxxxxxxxxTHIRD ROWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

btn4=Button(cal,padx=20,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="4", bg="black",command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(cal,padx=16,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="5", bg="black",command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(cal,padx=16.5,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="6", bg="black",command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(cal,padx=24.75,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="-", bg="black",command=lambda:btnClick("-")).grid(row=3,column=3)

btnop=Button(cal,padx=16.5,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="(",bg="black",command=lambda:btnClick("(")).grid(row=3,column=4)

#xxxxxxxxxxxFORTH ROWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

btn1=Button(cal,padx=20,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="1", bg="black",command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="2", bg="black",command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(cal,padx=16.5,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="3", bg="black",command=lambda:btnClick(3)).grid(row=4,column=2)

Multiply=Button(cal,padx=21.75,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="x", bg="black",command=lambda:btnClick("*")).grid(row=4,column=3)

btnop2=Button(cal,padx=16.5,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text=")", bg="black",command=lambda:btnClick(")")).grid(row=4,column=4)

#xxxxxxxxxxxxxxxxxxFIFTH ROWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

btn0=Button(cal,padx=16.25,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="0", bg="black",command=lambda:btnClick(0)).grid(row=5,column=1)

btnClear=Button(cal,padx=16.75,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="C", bg="black",command=btnClearDisplay).grid(row=5,column=0)

btnEquals=Button(cal,padx=15.5,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="=", bg="black",command=btnEqualsInput).grid(row=5,column=2)

Division=Button(cal,padx=21.75,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="÷", bg="black",command=lambda:btnClick("/")).grid(row=5,column=3)

btnop2=Button(cal,padx=10,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="%", bg="black",command=btnModulus).grid(row=5,column=4)

btnsqrt=Button(cal,padx=16.25,pady=16,bd=8,fg="White", font=("arial", 20, 'bold'),
            text="SqRt", bg="black",command=sqrts).grid(row=5,column=5)


#xxxxxxxxxxxxxxxxxxSIXTH ROWxxxxxxxxxxxxxxxxxxxx










