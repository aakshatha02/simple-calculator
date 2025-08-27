import tkinter as tk

def calculator(op):
    try:
        first = float(first_num.get())
        second = float(second_num.get())

        match op:
            case "+":
                result = first + second
            case "-":
                result = first - second
            case "*":
                result = first * second
            case "/":
                if second != 0:
                    result = first / second
                else:
                    result_label.config(text="❌ Division by zero", fg="#ff4c4c")
                    return
            case _:
                result_label.config(text="❌ Invalid operation", fg="#ff4c4c")
                return

        result_label.config(text=f"✅ Result: {result}", fg="#2ecc71")  # green
    except ValueError:
        result_label.config(text="❌ Enter valid numbers", fg="#ff4c4c")

def clear_fields():
    first_num.delete(0, tk.END)
    second_num.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("420x380")
root.resizable(False, False)
root.configure(bg="#2c3e50")  # dark background

# --- Styling ---
entry_style = {"font": ("Helvetica", 16), "width": 12, "justify": "center", "bd": 3, "relief": "ridge", "fg": "#2c3e50"}
btn_style = {"font": ("Helvetica", 14, "bold"), "width": 6, "height": 2, "bd": 0, "relief": "flat"}

# --- Entries ---
first_num = tk.Entry(root, **entry_style)
first_num.pack(pady=10)
first_num.insert(0, "0")

second_num = tk.Entry(root, **entry_style)
second_num.pack(pady=10)
second_num.insert(0, "0")

# --- Buttons Frame ---
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=15)

# Operation buttons with modern colors
tk.Button(btn_frame, text="+", command=lambda: calculator("+"), fg="black", **btn_style).grid(row=0, column=0, padx=6, pady=6)
tk.Button(btn_frame, text="-", command=lambda: calculator("-"), fg="black", **btn_style).grid(row=0, column=1, padx=6, pady=6)
tk.Button(btn_frame, text="×", command=lambda: calculator("*"), fg="black", **btn_style).grid(row=0, column=2, padx=6, pady=6)
tk.Button(btn_frame, text="÷", command=lambda: calculator("/"), fg="black", **btn_style).grid(row=0, column=3, padx=6, pady=6)

# --- Result Label ---
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white")
result_label.pack(pady=20)

# --- Clear Button ---
clear_btn = tk.Button(
    root, text="Clear", command=clear_fields,
    font=("Helvetica", 14, "bold"),
    fg="black",
    width=12, height=2, relief="flat", bd=0
)
clear_btn.pack(pady=10)

root.mainloop()
