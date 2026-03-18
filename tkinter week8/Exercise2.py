from tkinter import *

root = Tk()
root.title("Woah Labels")
root.geometry("450x350")

unwoah_lbl = Label(root, text="Wow... a label... so impressive....")
unwoah_lbl.pack(pady=5)

woah_lbl = Label(root, text="Woah, a label", font="Grotesque", fg="#80fff4", bg="#35f348", padx=5, pady=5)
woah_lbl.pack(pady=15)

long_lbl = Label(root, text="This label is super long. It was going to be named superlong_lbl but super was a command word so I decided not to include it. Just like how I don't like to include not in variable names as well. I also prefer to avoid int but that's not really feasible super often.", wraplength=180, justify="right", font=("Perpetua", 12)) #Woah wraplength, justify is just alignment.
long_lbl.pack(pady=10)

status_txt = StringVar()
status_txt.set("Status: Ready")
status_lbl = Label(root, textvariable=status_txt, font=("Courier", 12), fg="black", relief="sunken", width=30)
status_lbl.pack(pady=10)

status_txt.set("Status: Not Ready") #This is pretty cool actually!

root.mainloop()