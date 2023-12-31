from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.configure(background='white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = self.current ** 2
        self.display(self.current)

    def sqrt(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.sqrt(self.current)
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.sin(math.radians(self.current))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.cos(math.radians(self.current))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.tan(math.radians(self.current))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.log(self.current)
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.exp(self.current)
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.sinh(self.current)
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.cosh(self.current)
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.tanh(self.current)
        self.display(self.current)

    def asin(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.asin(self.current)
        self.display(self.current)

    def acos(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.acos(self.current)
        self.display(self.current)

    def atan(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.atan(self.current)
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.log2(self.current)
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = float(txtDisplay.get())
        self.current = math.log10(self.current)
        self.display(self.current)

added_value = Calc()
txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg='white', bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1

btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='white',
                  command=added_value.clear_entry).grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='white',
                     command=added_value.all_clear_entry).grid(row=1, column=1, pady=1)

btnSqrt = Button(calc, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='white',
                 command=added_value.sqrt).grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg