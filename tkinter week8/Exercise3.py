from tkinter import *

def greet_click():
    name = name_entry.get()
    if not name:
        output_lbl.configure(text=f"Hi!")
    else:
        output_lbl.configure(text=f"Hi, {name}!")

def clear_click():
    name_entry.delete(0, END)

def exit_click():
    root.destroy()

root = Tk()
root.title("Woah Buttons")
root.geometry("400x250")

Label(root, text="Enter your name.", font=("Yu Gothic", 12)).pack(pady=(20, 10)) #pady=(x, y) where x is the padding above and y is the padding below
name_entry = Entry(root, font=("Arial Narrow", 12), width=25)
name_entry.pack(pady=5)

btn_frame = Frame(root)
btn_frame.pack(pady=10)

greet_btn = Button(btn_frame, text="Greet", command=greet_click, bg="#042AD4", fg="white", font=("Ebrima", 11, "bold"))
greet_btn.pack(side=LEFT, padx=5)

clear_btn = Button(btn_frame, text="Clear", command=clear_click, font=("Lucida Bright", 11), width=10)
clear_btn.pack(side=LEFT, padx=5)

exit_btn = Button(btn_frame, text="Exit", command=exit_click, fg="red", font=("Harrington", 11), width=10)
exit_btn.pack(side=LEFT, padx=5)

output_lbl = Label(root, text="", font=("Raavi", 14), fg="#ADF345")
output_lbl.pack(pady=20)

root.mainloop()