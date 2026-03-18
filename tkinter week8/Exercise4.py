import tkinter as tk

def calculate_bmi_click():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if height <= 0 or weight <= 0:
            raise ValueError
        bmi = weight / (height ** 2)
        result_var.set(f"Your BMI is: {bmi:.1f}")
        # Change colour based on BMI range
        if bmi < 18.5:
            result_label.config(fg="blue")
        elif bmi < 25:
            result_label.config(fg="green")
        elif bmi < 30:
            result_label.config(fg="orange")
        else:
            result_label.config(fg="red")
    except ValueError:
        result_var.set("Please enter valid numbers.")
        result_label.config(fg="red")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x250")
root.configure(bg="#d6f5ec")

# Weight input
tk.Label(root, text="Weight (kg):", font=("Stencil", 11),
bg="#b8f3cb").pack(pady=(15, 2))
weight_entry = tk.Entry(root, font=("Shruti", 12), width=20,
justify="center")
weight_entry.pack()
weight_entry.insert(0, "e.g. 70") #Inserts at the 0th character in

# Height input
tk.Label(root, text="Height (m):", font=("Onyx", 11),
bg="#becff3").pack(pady=(10, 2))
height_entry = tk.Entry(root, font=("Gabriola", 12), width=20,
justify="center")
height_entry.pack()
height_entry.insert(0, "e.g. 1.75")

def weight_clear(event):
    """Activates when weight_entry is clicked"""
    if weight_entry.get() == "e.g. 70":
        weight_entry.delete(0, tk.END)

def height_clear(event):
    """Activates when height_entry is clicked"""
    if height_entry.get() == "e.g. 1.75":
        height_entry.delete(0, tk.END)

#Binds the click event to the methods.
weight_entry.bind("<FocusIn>", weight_clear)
height_entry.bind("<FocusIn>", height_clear)

# Calculate button
tk.Button(
root,
text="Calculate BMI",
command=calculate_bmi_click,
bg="#5B2C8E",
fg="white",
font=("Walbaum Text", 11, "bold")
).pack(pady=15)
# Result
result_var = tk.StringVar()
result_label = tk.Label(
root,
textvariable=result_var,
font=("OCR A Extended", 13, "bold"),
bg="#bcabfa"
)
result_label.pack()

root.mainloop()