import tkinter as tk
from tkinter import ttk
from Password_check import check_password


# Window
root = tk.Tk()
root.title("Password Strength Checker (Real-Time)")
root.geometry("420x450")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("default")
style.configure("bar.Horizontal.TProgressbar", thickness=20)

# Title
tk.Label(root, text="Password Strength Checker", font=("Arial", 14, "bold")).pack(
    pady=10
)

# Input
entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack(pady=5)


root.mainloop()
