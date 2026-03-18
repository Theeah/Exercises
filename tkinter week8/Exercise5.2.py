#This doesn't actually work!
import tkinter as tk

root = tk.Tk()
root.title("Grid Demo")

root.columnconfigure(1, weight=1)

# Row 0: Name
tk.Label(root, text="Full Name:", font=("Daytona", 11)).grid(row=0, column=0, padx=10, pady=8, sticky="e") #Widget sticks to east border.
tk.Entry(root, font=("Lao UI", 11)).grid(row=0, column=1, padx=10, pady=8, sticky="ew") #Sticks to both east and west

# Row 1: Email
tk.Label(root, text="Email:", font=("Rockwell", 11)).grid(row=1, column=0, padx=10, pady=8, sticky="e")
tk.Entry(root, font=("Wandohope", 11)).grid(row=1, column=1, padx=10, pady=8, sticky="ew")

# Row 2: Password
tk.Label(root, text="Password:", font=("Kalinga", 11)).grid(row=2, column=0, padx=10, pady=8, sticky="e")
tk.Entry(root, font=("Reem Kufi", 11), show="*").grid(row=2, column=1, padx=10, pady=8, sticky="ew") #show="*" is very cool!

# Row 3: Button spanning two columns
tk.Button(root, text="Register", bg="#5B2C8E", fg="white",font=("Arial", 11, "bold")).grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()