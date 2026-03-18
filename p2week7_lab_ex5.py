import tkinter as tk

def submit_form_click():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        result.config(text=f"Submitted: {name} ({email})", fg="green")

root = tk.Tk()
root.title = "Form"

tk.Label(root, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10,pady=10, sticky="e") #tk.Label().grid() layout

#Alternative way. Use when widget must be named
name_entry = tk.Entry(root, width=25, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:", font=("Arial", 12)).grid(row=1, column=0, padx=10,pady=10, sticky="e")

email_entry = tk.Entry(root, width=25, font=("Arial", 12))
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Submit", command=submit_form_click, font=("Arial", 12)).grid(row=2,column=0, columnspan=2, pady=15) #Fills row since columnspan=2

result = tk.Label(root, text="", font=("Arial", 12))
result.grid(row=3, column=0, columnspan=2)

root.mainloop()