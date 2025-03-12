from tkinter import *

buttons_list = ['%', '√', "x²", "1/x",
                "CE", 'C', '←', '÷',
                '7', '8', '9', 'x',
                '4', '5', '6', '-',
                '1', '2', '3', '+',
                '±', '0', ',', '=']

# Creating the window
window = Tk()
window.title("Cumculator")
window_size = "348x395" # "350x400" # 55,8(3) and 87,5
window.geometry(window_size)
window.resizable(False, False)

# Functions
def main_calc(string):
    global memory
    if string == '÷':
        entry.delete(0, END)
        if float(memory[2]) == 0.0:
            entry.insert(END, "!Dividing by 0!")
        else:
            entry.insert(END, float(memory[0])/float(memory[2]))
            memory[0] = float(memory[0])/float(memory[2])
    if string == 'x':
        entry.delete(0, END)
        entry.insert(END, float(memory[0])*float(memory[2]))
        memory[0] = float(memory[0])*float(memory[2])
    if string == '-':
        entry.delete(0, END)
        entry.insert(END, float(memory[0])-float(memory[2]))
        memory[0] = float(memory[0])-float(memory[2])
    if string == '+':
        entry.delete(0, END)
        entry.insert(END, float(memory[0])+float(memory[2]))
        memory[0] = float(memory[0])+float(memory[2])
    if string == '√':
        entry.delete(0, END)
        entry.insert(END, round(float(memory[0])**0.5, 5))
    if string == "x²":
        entry.delete(0, END)
        entry.insert(END, round(float(memory[0])**2, 5))
    if string == "1/x":
        entry.delete(0, END)
        if float(memory[0]) == 0.0:
            entry.insert(END, "!Dividing by 0!")
        else: entry.insert(END, round(float(memory[0])**(-1), 5))
    if string == '±':
        if entry.get() != '0':
            entry.delete(0, END)
            entry.insert(END, float(memory[0])*(-1))

def char_reading(char):
    global memory
    if char in "0123456789":
        if char == '0' and entry.get()[0] == '0' and '.' not in entry.get():
            pass
        if entry.get() == '0':
            entry.delete(0, END)
            entry.insert(END, char)
        else: entry.insert(END, char)
    if char == ',' and '.' not in entry.get():
        entry.insert(END, '.')
    if char == '←':
        entry.delete(len(entry.get()) - 1)
        if len(entry.get()) == 0 or entry.get() == '-':
            entry.delete(len(entry.get()) - 1)
            entry.insert(END, 0)
    if char == "CE":
        entry.delete(0, END)
        entry.insert(END, 0)
    if char in "÷x-+" and len(entry.get()) != 0:
        memory = [entry.get(), char]
        entry.delete(0, END)
        entry.insert(END, 0)
    if char == 'C':
        entry.delete(0, END)
        entry.insert(END, 0)
        memory = []
    if char in '=':
        if len(entry.get()) != 0 and len(memory) != 0:
            memory.append(entry.get())
            main_calc(memory[1])
    if char == '%':
        if len(entry.get()) != 0 and len(memory) != 0:
            memory.append( (float(memory[0])/100) * float(entry.get()))
            main_calc(memory[1])
    if char in ['√', "x²", "1/x"]:
        memory = [entry.get(), char]
        main_calc(char)
    if char == '±':
        memory = [entry.get()]
        main_calc(char)

# Creating an entry
entry = Entry(font=('Arial', 40), justify='right')
entry.pack(anchor=N, fill=X)
entry.insert(END, 0)

# Creating buttons
list_counter = 0
for i in range(6):
    for j in range(4):
        btn = Button(text=buttons_list[list_counter], font=('Arial', 20), command=lambda char=buttons_list[list_counter]: char_reading(char))
        btn.place(x=87*j, y=65 + 55*i, width=87, height=55)
        list_counter += 1

window.mainloop()

# + первый ноль и запятая
# + ошибку деления на ноль
# + пустота в ноль
#   ввод с клавиатуры 
#   информация
