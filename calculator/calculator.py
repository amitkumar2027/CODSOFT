import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget for input and result
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
entry.pack(padx=10, pady=20, fill="both")

# Function to handle button clicks
def click(symbol):
    if symbol == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create buttons in grid
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 18), relief="groove",
                        command=lambda symbol=btn_text: click(symbol))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Run the application
root.mainloop()
