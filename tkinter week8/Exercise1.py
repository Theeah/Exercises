from tkinter import * #Different from import tkinter as tk because here we don't need to do tk. whenever using it.

root = Tk()
root.title("Sizeable")
root.geometry("400x300")
root.minsize(300,200) #Stops a user from shrinking the window smaller than the parameters.
root.maxsize(500,400) #Stops the user from increasing the window size above the parameters.
root.configure(bg="#f0f0f0")

root.mainloop()