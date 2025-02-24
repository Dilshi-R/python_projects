import tkinter as tk

def on_click(button_text):
    entry.insert(tk.END, button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())  # Evaluates the expression entered
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and output
entry = tk.Entry(root, width=20, font=("Arial", 16), bd=5, relief=tk.SUNKEN, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create buttons
for r, row in enumerate(buttons, 1):
    for c, text in enumerate(row):
        if text == "=":
            btn = tk.Button(root, text=text, width=11, height=2, font=("Arial", 14), command=calculate)  # Wider "=" button
            btn.grid(row=r, column=c, columnspan=2, padx=5, pady=5)  # Span two columns
        elif text == "0":
            btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: on_click(t))
            btn.grid(row=r, column=c, padx=5, pady=5)
        else:
            btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: on_click(t))
            btn.grid(row=r, column=c, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=clear)
clear_btn.grid(row=4, column=0, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
