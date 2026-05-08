import tkinter as tk
from tkinter import ttk
from Password_check import check_password


def toggle_password():
    entry.config(show="" if show_var.get() else "*")


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

# a button that shows the password
show_var = tk.IntVar()
tk.Checkbutton(
    root, text="Show Password", variable=show_var, command=toggle_password
).pack()

# Progress bar
progress = ttk.Progressbar(
    root, length=300, maximum=5, style="bar.Horizontal.TProgressbar"
)
progress.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

score_label = tk.Label(root, text="", font=("Arial", 10))
score_label.pack()

# Feedback
feedback_text = tk.Text(root, height=10, width=48)
feedback_text.pack(pady=10)

root.mainloop()
