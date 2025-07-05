import tkinter as tk
from tkinter import messagebox
from todo_backend import ToDoList

class ToDoApp:
    def __init__(self, root):
        self.todo = ToDoList()
        self.root = root
        self.root.title("📝 TO-DO LIST")
        self.root.geometry("400x500")
        self.root.config(bg="#fefae0")

        self.task_var = tk.StringVar()

        tk.Label(root, text="My TO-DO List", font=("Arial", 18, "bold"), bg="#fefae0").pack(pady=10)

        input_frame = tk.Frame(root, bg="#fefae0")
        input_frame.pack(pady=10)
        tk.Entry(input_frame, textvariable=self.task_var, width=30, font=("Arial", 12)).grid(row=0, column=0, padx=10)
        tk.Button(input_frame, text="Add Task", command=self.add_task, bg="#90be6d").grid(row=0, column=1)

        self.listbox = tk.Listbox(root, width=45, height=15, font=("Arial", 12))
        self.listbox.pack(pady=20)

        btn_frame = tk.Frame(root, bg="#fefae0")
        btn_frame.pack()

        tk.Button(btn_frame, text="Delete Selected", command=self.delete_task, bg="#f94144").grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Clear All", command=self.clear_all, bg="#f3722c").grid(row=0, column=1, padx=10)

    def add_task(self):
        task = self.task_var.get()
        if self.todo.add_task(task):
            self.update_list()
            self.task_var.set("")
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.todo.remove_task(selected_index)
            self.update_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_all(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.todo.clear_all()
            self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo.get_tasks():
            self.listbox.insert(tk.END, task)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
