from tkinter import *

def show_selection_click():
    selected = []
    if python_var.get():
        selected.append("Python")
    if java_var.get():
        selected.append("Java")
    if js_var.get():
        selected.append("Javascript")
    if csharp_var.get():
        selected.append("CSharp")
    if eng_var.get():
        selected.append("English")
    
    if selected:
        result_var.set("Selected: " + ",".join(selected))
    else:
        result_var.set("No languages selected.")

root = Tk()
root.title("Checkbuttons! Radiobuttons!")
root.geometry("400x400")

Label(root, text="Which languages do you know?", font=("Aparajita", 12, "bold")).pack(pady=(15, 5))

python_var = BooleanVar()
java_var = BooleanVar()
js_var = BooleanVar()
csharp_var = BooleanVar()
eng_var = BooleanVar()

Checkbutton(root, text="Python", variable=python_var, font=("DokChampa", 11)).pack(anchor="w", padx=40)
Checkbutton(root, text="Java", variable=java_var, font=("DokChampa", 11)).pack(anchor="w", padx=40)
Checkbutton(root, text="Javascript", variable=js_var, font=("DokChampa", 11)).pack(anchor="w", padx=40)
Checkbutton(root, text="CSharp", variable=csharp_var, font=("DokChampa", 11)).pack(anchor="w", padx=40)
Checkbutton(root, text="English", variable=eng_var, font=("DokChampa", 11)).pack(anchor="w", padx=40)

Button(root, text="Show Selection", command=show_selection_click,bg="#5B2C8E", fg="white").pack(pady=10)

result_var = StringVar()
Label(root, textvariable=result_var, font=("Alasassy Caps", 11), fg="#f73235", wraplength=350).pack(pady=5)

Label(root, text="\nPreferred Difficulty:", font=("Baguet Script", 12, "bold")).pack(pady=(10,5))
difficulty_var = StringVar(value="medium")

for text, value in [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]:
    Radiobutton(root, text=text, variable=difficulty_var, value=value, font=("Algerian", 11)).pack(anchor="w", padx=40)

root.mainloop()