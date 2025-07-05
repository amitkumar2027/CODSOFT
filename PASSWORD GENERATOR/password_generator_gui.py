import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        
        # character sets
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_chars) for _ in range(length))
        
        # Show password
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x250")
root.config(bg="#e0f7fa")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#e0f7fa").pack(pady=10)

# Length Input
frame = tk.Frame(root, bg="#e0f7fa")
frame.pack(pady=10)
tk.Label(frame, text="Enter Password Length:", font=("Arial", 12), bg="#e0f7fa").grid(row=0, column=0, padx=5)
length_entry = tk.Entry(frame, width=10, font=("Arial", 12))
length_entry.grid(row=0, column=1)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="#00796b", fg="white", font=("Arial", 12)).pack(pady=10)

# Password Display
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=35, font=("Arial", 12), justify="center").pack(pady=10)

# Main loop
root.mainloop()
