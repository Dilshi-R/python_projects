import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        messagebox.showinfo("BMI Result", f"Your BMI is {bmi:.2f} ({category})")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Labels and input fields
tk.Label(root, text="Weight (kg):", font=("Arial", 12)).pack(pady=5)
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack()

tk.Label(root, text="Height (cm):", font=("Arial", 12)).pack(pady=5)
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack()

# Calculate Button
calc_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12), command=calculate_bmi)
calc_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the Tkinter loop
root.mainloop()
