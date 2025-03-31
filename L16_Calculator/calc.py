from tkinter import *

# Functions
def main_calc(op):
    global memory
    entry.delete(0, END)
    x = float(memory[0])
    y = float(memory[2]) if len(memory) > 2 else 0
    operations = {'+': x + y, '-': x - y, 'x': x * y, '÷': "!Dividing by 0!" if y == 0 else x / y,
           '√': "!√ of negative!" if x < 0 else round(x ** 0.5, 5), "x²": round(x ** 2, 5), "1/x": "!Dividing by 0!" if x == 0 else round(1 / x, 5),
           '±': -x if x != 0 else 0}
    entry.insert(END, operations.get(op, 0))
    if op in "+-x÷": memory[0] = operations[op]

def char_reading(char):
    global memory
    if char in "0123456789" or (char == '0' and text != '0'):
        if entry.get() == '0':
            entry.delete(0, END)
        entry.insert(END, char)
    if char == ',' and '.' not in entry.get():
        entry.insert(END, '.')
    if char == '←':
        entry.delete(len(entry.get()) - 1)
        if len(entry.get()) == 0 or entry.get() == '-':
            entry.delete(len(entry.get()) - 1)
            entry.insert(END, 0)
    if char in "÷x-+" and len(entry.get()) != 0:
        memory = [entry.get(), char]
        entry.delete(0, END)
        entry.insert(END, 0)
    if char in "CE C":
        entry.delete(0, END)
        entry.insert(END, 0)
        if char == 'C': memory = []
    if char == '=' and len(entry.get()) != 0 and len(memory) != 0:
        memory.append(entry.get())
        main_calc(memory[1])
    if char == '%' and len(entry.get()) != 0 and len(memory) != 0:
        memory.append( (float(memory[0]) / 100) * float(entry.get()))
        main_calc(memory[1])
    if char in ['√', "x²", "1/x"]:
        memory = [entry.get(), char]
        entry.delete(0, END)
        main_calc(char)
    if char == '±':
        memory = [entry.get()]
        main_calc(char)

def key_pressed(event):
    key_map = {'Return': '=', 'BackSpace': '←', 'Escape': 'C', 'plus': '+', 'minus': '-', 'asterisk': 'x', 'slash': '÷', 'comma': ','}
    char = key_map.get(event.keysym, event.char)
    if char in buttons_list:
        char_reading(char)

buttons_list = ['%', '√', "x²", "1/x",
                "CE", 'C', '←', '÷',
                '7', '8', '9', 'x',
                '4', '5', '6', '-',
                '1', '2', '3', '+',
                '±', '0', ',', '=']

# Creating the window
window = Tk()
window.title("Calculator")
window_size = "348x445" # "348x395"
window.geometry(window_size)
window.resizable(False, False)

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

window.bind("<Key>", key_pressed)
author_info = Label(text="Гильмия Арслановна и Азат Азатович, спасибо за всё!!!\nCopyright (c) 2025 A.A.Kireev\nAll rights are reserved")
author_info.place(x=174-155, y=445-50)

window.mainloop()

# + первый ноль и запятая
# + ошибку деления на ноль
# + пустота в ноль
# + ввод с клавиатуры 
# + информация”
