import tkinter as tk

def convert_click():
    temp=temp_entry.get()
    try:
        temp = float(temp)
        celsius=(temp-32)*(5/9)
        result_lbl.config(text=f"Celsius: {celsius}", fg="green")
    except (ValueError, TypeError):
        result_lbl.config(text="Temperature must be a decimal number.", fg="red")
    
    

    
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")

tk.Label(root, text="Temperature Converter", font=("Calibri", 18, "bold")).pack(pady=20)

temp_entry = tk.Entry(root, width=6, font=("Candara", 12))
temp_entry.pack(pady=25)

convert_btn = tk.Button(root, width=10, text="Convert", command=convert_click, font=("David",15)).pack(pady=10)

result_lbl = tk.Label(root, text="Celsius:      ", font=("Biome", 15), fg="green")
result_lbl.pack(pady=12)

root.mainloop()