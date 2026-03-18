import tkinter as tk

def button_click():
    welcome.config(font="Arial")

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")

welcome = tk.Label(
    root,
    text="Welcome.",
    font=("Wingdings", 18, "bold"),
    fg="teal",
    bg="turquoise"
)
welcome.pack(pady=20)

b1 = tk.Button(
    root,
    text="Boringify",
    command=button_click,
    font=("Helvetica", 12, "italic")
)
b1.pack(pady=40)

inp = tk.Entry(
    root,
    width=30,
    font=("Gothic", 18)
)
inp.pack(pady=30)

root.mainloop()