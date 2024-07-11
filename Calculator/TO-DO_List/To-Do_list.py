import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showerror("Error", "Please select a task to remove.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
tasks_listbox.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)

add_button.pack()
remove_button.pack()
clear_button.pack()

root.mainloop()
