import os
from tkinter import *

# Widgety = GUI elementy - buttons, textboxes, labels, ...

# Obrazovka:

window = Tk()
window.geometry("1270x720")
window.title("Tutorial")
icon = PhotoImage(file=os.path.join("images", "icon.png"))

# label

app_label = Label(window, text="Ahoj svjete", font=("Arial", 40, "bold"))
app_label.pack()
app_label.place(x=0, y=0)

# button

count = 0
def click_function():
    global count
    count += 1

app_button = Button(window, text="Klikni")
app_button.config(command=click_function, font=("Arial", 40))
app_button.pack()

# User Input
#   entry widget = textbox, který přijímá jeden řádek uživatelského vstupu

entry_widget = Entry()
entry_widget.insert(0, "Text")  # Vloží text na zadaný index
# entry_widget.config(show="*")   # Password
act_input = entry_widget.get()  # Získání aktuálního vstupu
entry_widget.delete(0, END)     # Odstraní obsah entry textBoxu od first_index do last_index
entry_widget.pack()

# CheckBox
#

var1 = IntVar() # IntVar slouží ke správě celých čísel a jejich propojení s GUI prvky
var2 = IntVar()

def command():
    var1_value = var1.get()
    var2_value = var2.get()
    if var1_value == 1 and var2_value == 1:
        print("Oba jsou zaškrtnuté.")
    elif var1_value == 1 and var2_value == 0:
        print("PRVNÍ je zaškrtnutý")
    elif var1_value == 0 and var2_value == 1:
        print("DRUHÝ je zaškrtnutý")
    else: print("ŽÁDNÝ není zaškrtnutý")
   

checkbox1 = Checkbutton(window, text="moznost 1", variable=var1, onvalue=1, offvalue=0, command=command)
checkbox1.config(anchor="w") # w = West
checkbox1.pack()
checkbox2 = Checkbutton(window, text="moznost 2", variable=var2, onvalue=1, offvalue=0, command=command)
checkbox2.config(anchor="w") # w = West
checkbox2.pack()

window.iconphoto(True, icon)
window.mainloop()