
import tkinter

root = tkinter.Tk()
root.title("Calculator")

root.resizable(width = False, height = False)
expression = ""

#Create Functions
def add(value):
	global expression
	expression += value
	label_result.config(text=expression)

def clear():
	global expression
	expression = ""
	label_result.config(text=expression)

def calculate():
	global expression
	result = ""
	if expression != "":
		try:
			result = eval(expression)
		except:
			result = "error"
			expression = ""
	label_result.config(text=result)
#Create GUI
label_result = tkinter.Label(root, text="")
label_result.grid(row=0, column=0, columnspan=4)

Key_1 = tkinter.Button(root, text="1", width=6,command=lambda: add("1"))
Key_1.grid(row=1, column=0)

Key_2 = tkinter.Button(root, text="2", width=6,command=lambda: add("2"))
Key_2.grid(row=1, column=1)

Key_3 = tkinter.Button(root, text="3", width=6,command=lambda:add("3"))
Key_3.grid(row=1, column=2)

Key_divide = tkinter.Button(root, text="/", width=6,command=lambda: add("/"))
Key_divide.grid(row=1, column=3)

Key_4 = tkinter.Button(root, text="4", width=6,command=lambda: add("4"))
Key_4.grid(row=2, column=0)

Key_5 = tkinter.Button(root, text="5", width=6,command=lambda: add("5"))
Key_5.grid(row=2, column=1)

Key_6 = tkinter.Button(root, text="6", width=6,command=lambda: add("6"))
Key_6.grid(row=2, column=2)
Key_multiply = tkinter.Button(root, text="*", width=6,command=lambda: add("*"))
Key_multiply.grid(row=2, column=3)

Key_7 = tkinter.Button(root, text="7", width=6,command=lambda: add("7"))
Key_7.grid(row=3, column=0)

Key_8 = tkinter.Button(root, text="8", width=6,command=lambda: add("8"))
Key_8.grid(row=3, column=1)

Key_9 = tkinter.Button(root, text="9", width=6,command=lambda: add("9"))
Key_9.grid(row=3, column=2)

Key_subtract = tkinter.Button(root, text="-", width=6,command=lambda: add("-"))
Key_subtract.grid(row=3, column=3)

Key_clear = tkinter.Button(root, text="C", width=6,command=lambda:clear())
Key_clear.grid(row=4, column=0)

Key_0 = tkinter.Button(root, text="0", width=6, command=lambda: add("0") )
Key_0.grid(row=4, column=1)

Key_dot = tkinter.Button(root, text=".", width=6, command=lambda: add("."))
Key_dot.grid(row=4, column=2)

Key_add = tkinter.Button(root, text="+", width=6, command=lambda: add("+"))
Key_add.grid(row=4, column=3)

Key_equals = tkinter.Button(root, text="=", width=33, command=lambda: calculate())
Key_equals.grid(row=5, column=0, columnspan=4)



root.mainloop()