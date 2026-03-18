import tkinter as tk

def add_student_click():
    mark = mark_entry.get()
    name = name_entry.get()
    if not name:
        result_lbl.config(text="Please enter a name for the student.")
    else:
        try:
            intmark = int(mark)
            if intmark<0:
                result_lbl.config(text="Mark must be positive.")
            elif intmark>100:
                result_lbl.config(text="Mark is out of 100.")
            else:
                current_students = student_list.get(0, tk.END)
                index = len(current_students)
                student_list.insert(index+1, f"{name}: {mark}")
        except (ValueError, TypeError):
            result_lbl.config(text="Please enter mark as an integer.")


def delete_student_click():
    index = student_list.curselection()
    if not index:
        result_lbl.config(text= "Please select a student to delete.")
    else:
        student_list.delete(index)

def calculate_average_click():
    students = student_list.get(0, tk.END)
    total = 0
    for student in students:
        split_student = student.split(":")
        total = total + int(split_student[1]) #We have already checked the mark is an int, so this does not need to be in a try except.
    try:
        total = total / len(students)
        result_lbl.config(text=f"Average: {total}")
    except ZeroDivisionError:
        result_lbl.config(text="Average: N/A")

root = tk.Tk()
root.title("Student Tracker")

tk.Label(root, text="Student Name:", font=("Papyrus", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="e")

name_entry = tk.Entry(root, font=("Vani",10))
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

tk.Label(root, text="Mark:", font=("Papyrus", 10)).grid(row=1, column=0, padx=10, pady=10, sticky="e")

mark_entry = tk.Entry(root, font=("Vani",10))
mark_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

add_student_btn = tk.Button(root, text="Add Student", command=add_student_click, font=("Tunga", 10))
add_student_btn.grid(row=2, column=0, padx=10, pady=10, sticky="e")

delete_student_btn = tk.Button(root, text="Delete Student", command=delete_student_click, font=("Tunga", 10))
delete_student_btn.grid(row=2, column=1, padx=10, pady=10, sticky="e")

students = tk.Variable(value=[])
student_list = tk.Listbox(root, listvariable=students, width=40, selectmode=tk.SINGLE)
student_list.grid(row=3, columnspan=2, padx=10, pady=10, sticky="e")

calc_average_btn = tk.Button(root, width=32, text="Calculate Average", command=calculate_average_click, font=("Miriam", 10))
calc_average_btn.grid(row=4, columnspan=2, padx=10, pady=10, sticky="e")

result_lbl = tk.Label(root, width= 50, text="Average:      ", font=("Harrington", 12))
result_lbl.grid(row=5, columnspan=2, padx=10, pady=10, sticky="e")

root.mainloop()