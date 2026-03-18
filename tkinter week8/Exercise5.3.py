import tkinter as tk

root = tk.Tk()
root.title("place() Demo")
root.geometry("400x300")

# Absolute positioning with x, y
tk.Label(root, text="Positioned at (50, 30)", bg="lightblue").place(x=50,y=30)
tk.Label(root, text="Positioned at (150, 100)", bg="lightgreen").place(x=150, y=100)

"""Relative to the centre from 0 to 1.
relx=0 is far left, relx=1 is far right, rely=0 is top, rely=1 is bottom
Does adjust when screen size changes."""
tk.Button(root, text="Centre").place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()