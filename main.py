from tkinter import *
from tkinter import font
from math import *
from random import *

window = Tk()
myfont = font.Font(size=15, weight="bold")
window.title("Pro_Calculator")
window.geometry("680x240")
window.config(bg="white")
# MAIN ENTRY
entry = Entry(window, width=73, borderwidth=5, bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=10, ipady=15)
operator = ""
num1 = '0'
entry.insert(0, '0')


#########.........First Function..............################
def show(obj):
    if entry.get() == '0':
        s = obj
        entry.delete(0, END)
        entry.insert(0, s)
    else:
        s = entry.get() + obj
        entry.delete(0, END)
        entry.insert(0, s)


#########.........2nd Function..............################
def clear():
    global num1
    num1 = '0'
    entry.delete(0, END)
    entry.insert(0, '0')


#########.........3rd  Function..............################
def plus_minus():
    global num1
    num1 = entry.get()
    entry.delete(0, END)
    num2 = float(num1) * -1
    entry.insert(0, num2)


#########.........4th Function..............################
def percent():
    global num1
    num1 = entry.get()
    entry.delete(0, END)
    num2 = float(num1) / 100
    entry.insert(0, num2)


#########.........5th  Function..............################
def devide():
    global num1
    global operator
    num1 = entry.get()
    entry.delete(0, END)
    operator = "devide"


#########.........6th  Function..............################
def multiply():
    global num1
    global operator
    num1 = entry.get()
    entry.delete(0, END)
    operator = "multiply"


#########.........7th  Function..............################
def minus():
    global num1
    global operator
    num1 = entry.get()
    entry.delete(0, END)
    operator = "minus"


#########.........8th  Function..............################
def add():
    global num1
    global operator
    num1 = entry.get()
    entry.delete(0, END)
    operator = "add"


#########.........9th  Function..............################

def equal():
    num2 = entry.get()
    entry.delete(0, END)
    if operator == "add":
        s = float(num1) + float(num2)
        entry.insert(0, s)
    if operator == "minus":
        s = float(num1) - float(num2)
        entry.insert(0, s)
    if operator == "multiply":
        s = float(num1) * float(num2)
        entry.insert(0, s)
    if operator == "devide":
        s = float(num1) / float(num2)
        entry.insert(0, s)
    if operator == "root":
        a = num2.replace("Enter root : ", "")
        entry.insert(0, float(num1) ** (1 / float(a)))
    if operator == "xpowery":
        a = num2.replace("Enter power : ", "")
        entry.insert(0, float(num1) ** (float(a)))


#########.........10th  Function..............################
def is_prime():
    global num1
    num1 = entry.get()
    num2 = int(num1)
    if num2 == 2:
        prime = True
    if num2 < 2:
        prime = False
    if num2 > 2:
        for i in range(2, num2):
            if (num2 % i) == 0:
                prime = False
                break
            else:
                prime = True
    if prime:
        entry.delete(0, END)
        entry.insert(0, "Number " + num1 + "  is Prime")
    else:
        entry.delete(0, END)
        entry.insert(0, "Number " + num1 + "  is Not Prime")


#########.........11th  Function..............################
def x_power_2():
    global num1
    num1 = entry.get()
    num2 = float(num1)
    entry.delete(0, END)
    entry.insert(0, pow(num2, 2))


#########.........12th  Function..............################
def x_power_3():
    global num1
    num1 = entry.get()
    num2 = float(num1)
    entry.delete(0, END)
    entry.insert(0, pow(num2, 3))


#########.........13th  Function..............################
def x_power_y():
    global operator
    operator = "xpowery"
    global num1
    num1 = entry.get()
    entry.delete(0, END)
    entry.insert(0, "Enter power : ")


#########.........14th  Function..............################
def e_power():
    global num1
    num1 = entry.get()
    num2 = float(num1)
    entry.delete(0, END)
    entry.insert(0, pow(e, num2))


#########.........15th  Function..............################
def ten_power():
    global num1
    num1 = entry.get()
    num2 = float(num1)
    entry.delete(0, END)
    entry.insert(0, pow(10, num2))


#########.........16th  Function..............################
def reverse():
    try:
        global num1
        num1 = entry.get()
        num2 = float(num1)
        entry.delete(0, END)
        entry.insert(0, 1 / num2)
    except ZeroDivisionError as error:
        entry.insert(0, error)


#########.........17th  Function..............################
def square_root():
    global num1
    num1 = entry.get()
    num2 = float(num1)
    entry.delete(0, END)
    entry.insert(0, sqrt(num2))


#########.........18th  Function..............################
def cube_root():
    global num1
    num1 = entry.get()
    num2 = pow(float(num1), (1 / 3))
    entry.delete(0, END)
    entry.insert(0, num2)


#########.........19th  Function..............################
def root():
    global operator
    operator = "root"
    global num1
    num1 = entry.get()
    entry.delete(0, END)
    entry.insert(0, "Enter root : ")


#########.........20th  Function..............################
def lnx():
    global num1
    num1 = entry.get()
    entry.delete(0, END)
    entry.insert(0, log(float(num1), e))


#########.........21st  Function..............################
def logx():
    global num1
    num1 = entry.get()
    entry.delete(0, END)
    entry.insert(0, log10(float(num1)))


#########.........22nd  Function..............################
def fact():
    try:
        global num1
        num1 = entry.get()
        num2 = int(num1)
        entry.delete(0, END)
        entry.insert(0, factorial(num2))
    except ValueError:
        entry.delete(0, END)
        entry.insert(0, "Enter Whole number")


#########.........23th  Function..............################
def sinx():
    global num1
    num1 = entry.get()
    num2 = (float(num1) * 2 * pi) / 360
    entry.delete(0, END)
    entry.insert(0, sin(num2))


#########.........24th  Function..............################
def cosx():
    global num1
    num1 = entry.get()
    num2 = (float(num1) * 2 * pi) / 360
    entry.delete(0, END)
    entry.insert(0, cos(num2))


#########.........25th  Function..............################
def tanx():
    global num1
    num1 = entry.get()
    num2 = (float(num1) * 2 * pi) / 360
    entry.delete(0, END)
    entry.insert(0, tan(num2))


#########.........26th  Function..............################
def show_exp():
    entry.delete(0, END)
    entry.insert(0, e)


#########.........27th  Function..............################
def cotx():
    global num1
    num1 = entry.get()
    num2 = (float(num1) * 2 * pi) / 360
    entry.delete(0, END)
    cot = 1 / tan(num2)
    entry.insert(0, cot)


#########.........28th  Function..............################
def radian():
    global num1
    num1 = entry.get()
    num2 = (float(num1) * 2 * pi) / 360
    entry.delete(0, END)
    entry.insert(0, num2)


#########.........29th  Function..............################
def sinhx():
    global num1
    num1 = entry.get()
    num2 = float(num1)
    entry.delete(0, END)
    entry.insert(0, sinh(num2))


#########.........30th  Function..............################
def coshx():
    global num1
    num1 = entry.get()
    num2 = float(num1)
    entry.delete(0, END)
    entry.insert(0, cosh(num2))


#########.........31st  Function..............################
def tanhx():
    global num1
    num1 = entry.get()
    num2 = float(num1)
    entry.delete(0, END)
    entry.insert(0, tanh(num2))


#########.........32nd  Function..............################
def show_pi():
    entry.delete(0, END)
    entry.insert(0, pi)


#########.........33th  Function..............################
def rand():
    global num1
    num1 = random()
    entry.delete(0, END)
    entry.insert(0, num1)


# row one
button_open_par = Button(window, text="(", padx=6, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                         state=DISABLED)
button_close_par = Button(window, text=")", padx=6, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                          state=DISABLED)
button_mc = Button(window, text="mc", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                   state=DISABLED)
button_m_plus = Button(window, text="m+", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                       state=DISABLED)
button_m_minus = Button(window, text="m-", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                        state=DISABLED)
button_mr = Button(window, text="mr", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                   state=DISABLED)
button_ac = Button(window, text="AC", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                   command=clear)
button_plus_minus = Button(window, text="+/-", padx=7, pady=6, fg="white", highlightbackground='#000000', font=myfont,
                           command=plus_minus)
button_percent = Button(window, text="%", padx=8, pady=6, fg="white", highlightbackground='#000000', font=myfont,
                        command=percent)
button_devide = Button(window, text="/", padx=8, pady=6, fg="white", highlightbackground="orange", font=myfont,
                       command=devide)
# insert row one
button_open_par.grid(row=1, column=0, ipadx=25)
button_close_par.grid(row=1, column=1, ipadx=25)
button_mc.grid(row=1, column=2, ipadx=12)
button_m_plus.grid(row=1, column=3, ipadx=10)
button_m_minus.grid(row=1, column=4, ipadx=10)
button_mr.grid(row=1, column=5, ipadx=10)
button_ac.grid(row=1, column=6, ipadx=10)
button_plus_minus.grid(row=1, column=7, ipadx=11)
button_percent.grid(row=1, column=8, ipadx=12)
button_devide.grid(row=1, column=9, ipadx=18)
# row 2
button_prime = Button(window, text="P", padx=8, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                      command=is_prime)
button_x2 = Button(window, text="x2", padx=5, pady=4, fg="white", highlightbackground='#000000', font=myfont,
                   command=x_power_2)
button_x3 = Button(window, text="x3", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                   command=x_power_3)
button_xy = Button(window, text="xy", padx=6, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                   command=x_power_y)
button_ex = Button(window, text="ex", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                   command=e_power)
button_10x = Button(window, text="10x", padx=5, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                    command=ten_power)
button_seven = Button(window, text="7", padx=7, pady=5, fg="white", highlightbackground="grey", font=myfont,
                      command=lambda: show('7'))
button_eight = Button(window, text="8", padx=8, pady=5, fg="white", highlightbackground="grey", font=myfont,
                      command=lambda: show('8'))
button_nine = Button(window, text="9", padx=8, pady=5, fg="white", highlightbackground="grey", font=myfont,
                     command=lambda: show('9'))
button_multiply = Button(window, text="x", padx=7, pady=5, fg="white", highlightbackground="orange", font=myfont,
                         command=multiply)
# insert row 2
button_prime.grid(row=2, column=0, ipadx=22)
button_x2.grid(row=2, column=1, ipadx=20)
button_x3.grid(row=2, column=2, ipadx=14)
button_xy.grid(row=2, column=3, ipadx=13)
button_ex.grid(row=2, column=4, ipadx=12)
button_10x.grid(row=2, column=5, ipadx=8)
button_seven.grid(row=2, column=6, ipadx=16)
button_eight.grid(row=2, column=7, ipadx=17)
button_nine.grid(row=2, column=8, ipadx=15)
button_multiply.grid(row=2, column=9, ipadx=17)
# row 3
button_reverse = Button(window, text="1/x", padx=4, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                        command=reverse)
button_sqrt = Button(window, text="√", padx=7, pady=6, fg="white", highlightbackground='#000000', font=myfont,
                     command=square_root)
button_curt = Button(window, text="3√", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                     command=cube_root)
button_root = Button(window, text="y√", padx=6, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                     command=root)
button_ln = Button(window, text="ln", padx=7, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                   command=lnx)
button_log = Button(window, text="log", padx=5, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                    command=logx)
button_four = Button(window, text="4", padx=7, pady=5, fg="white", highlightbackground="grey", font=myfont,
                     command=lambda: show('4'))
button_five = Button(window, text="5", padx=8, pady=5, fg="white", highlightbackground="grey", font=myfont,
                     command=lambda: show('5'))
button_six = Button(window, text="6", padx=8, pady=5, fg="white", highlightbackground="grey", font=myfont,
                    command=lambda: show('6'))
button_minus = Button(window, text="-", padx=7, pady=5, fg="white", highlightbackground="orange", font=myfont,
                      command=minus)
# insert row 3
button_reverse.grid(row=3, column=0, ipadx=19)
button_sqrt.grid(row=3, column=1, ipadx=22)
button_curt.grid(row=3, column=2, ipadx=13)
button_root.grid(row=3, column=3, ipadx=12)
button_ln.grid(row=3, column=4, ipadx=14)
button_log.grid(row=3, column=5, ipadx=11)
button_four.grid(row=3, column=6, ipadx=16)
button_five.grid(row=3, column=7, ipadx=17)
button_six.grid(row=3, column=8, ipadx=15)
button_minus.grid(row=3, column=9, ipadx=17)
# row4
button_fact = Button(window, text="x!", padx=4, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                     command=fact)
button_sin = Button(window, text="sin", padx=5, pady=4, fg="white", highlightbackground='#000000', font=myfont,
                    command=sinx)
button_cos = Button(window, text="cos", padx=5, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                    command=cosx)
button_tan = Button(window, text="tan", padx=5, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                    command=tanx)
button_e = Button(window, text="e", padx=8, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                  command=show_exp)
button_cot = Button(window, text="cot", padx=5, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                    command=cotx)
button_one = Button(window, text="1", padx=8, pady=5, fg="white", highlightbackground="grey", font=myfont,
                    command=lambda: show('1'))
button_two = Button(window, text="2", padx=8, pady=5, fg="white", highlightbackground="grey", font=myfont,
                    command=lambda: show('2'))
button_three = Button(window, text="3", padx=8, pady=5, fg="white", highlightbackground="grey", font=myfont,
                      command=lambda: show('3'))
button_plus = Button(window, text="+", padx=7, pady=5, fg="white", highlightbackground="orange", font=myfont,
                     command=add)
# insert row4
button_fact.grid(row=4, column=0, ipadx=24)
button_sin.grid(row=4, column=1, ipadx=18)
button_cos.grid(row=4, column=2, ipadx=12)
button_tan.grid(row=4, column=3, ipadx=12)
button_e.grid(row=4, column=4, ipadx=15)
button_cot.grid(row=4, column=5, ipadx=11)
button_one.grid(row=4, column=6, ipadx=15)
button_two.grid(row=4, column=7, ipadx=17)
button_three.grid(row=4, column=8, ipadx=15)
button_plus.grid(row=4, column=9, ipadx=17)
# row 5
button_rad = Button(window, text="rad", padx=5, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                    command=radian)
button_sinh = Button(window, text="sinh", padx=5, pady=6, fg="white", highlightbackground='#000000', font=myfont,
                     command=sinhx)
button_cosh = Button(window, text="cosh", padx=4, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                     command=coshx)
button_tanh = Button(window, text="tanh", padx=4, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                     command=tanhx)
button_pi = Button(window, text="π", padx=8, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                   command=show_pi)
button_rand = Button(window, text="rand", padx=4, pady=5, fg="white", highlightbackground='#000000', font=myfont,
                     command=rand)
button_zero = Button(window, text="0", padx=30, pady=5, fg="white", highlightbackground="grey", font=myfont,
                     command=lambda: show('0'))
button_dot = Button(window, text=".", padx=8, pady=5, fg="white", highlightbackground="grey", font=myfont,
                    command=lambda: show("."))
button_equal = Button(window, text="=", padx=8, pady=5, fg="white", highlightbackground="orange", font=myfont,
                      command=equal)
# insert row5
button_rad.grid(row=5, column=0, ipadx=17)
button_sinh.grid(row=5, column=1, ipadx=14)
button_cosh.grid(row=5, column=2, ipadx=8)
button_tanh.grid(row=5, column=3, ipadx=8)
button_pi.grid(row=5, column=4, ipadx=14)
button_rand.grid(row=5, column=5, ipadx=7)
button_zero.grid(row=5, column=6, ipadx=25, columnspan=2)
button_dot.grid(row=5, column=8, ipadx=18)
button_equal.grid(row=5, column=9, ipadx=15)

window.mainloop()
