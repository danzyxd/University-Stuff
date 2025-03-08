from tkinter import *

buttons_list = ['%', '√', 'x2', '1/x',
                'CE', 'C', '←', '÷',
                '7', '8', '9', 'X',
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
def char_reading(char):
    if char in "0123456789":
        entry.insert(END, char)
    if char == '←':
        entry.delete(len(entry.get()) - 1)

# Creating an entry
entry = Entry(font=('Arial', 40), justify='right')
entry.pack(anchor=N, fill=X)

# Creating buttons
list_counter = 0
for i in range(6):
    for j in range(4):
        btn = Button(text=buttons_list[list_counter], command=lambda char=buttons_list[list_counter]: char_reading(char))
        btn.place(x=87*j, y=65 + 55*i, width=87, height=55)
        list_counter += 1

window.mainloop()
