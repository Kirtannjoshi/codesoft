import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create listbox to display tasks
listbox_tasks = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
listbox_tasks.pack(padx=10, pady=10)

# Create entry for new tasks
entry_task = tk.Entry(root, width=50, font=("Arial", 12))
entry_task.pack(padx=10, pady=(0, 10))

# Create buttons to add and delete tasks
frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=5, fill=tk.X)

button_add = tk.Button(frame_buttons, text="Add Task", width=10, command=add_task)
button_add.pack(side=tk.LEFT)

button_delete = tk.Button(frame_buttons, text="Delete Task", width=10, command=delete_task)
button_delete.pack(side=tk.LEFT)

# Run the application
root.mainloop()
