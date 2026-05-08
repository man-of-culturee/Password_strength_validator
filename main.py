import tkinter as tk
from tkinter import ttk
from Password_check import check_password


def real_time_validation(event=None):
    password = entry.get()
    score, feedback = check_password(password)

    # Update progress bar
    progress["value"] = score

    # Reset UI
    feedback_text.delete("1.0", tk.END)

    # Strength display
    if score <= 2:
        style.configure("bar.Horizontal.TProgressbar", background="red")
        result_label.config(text="Weak password", fg="red")
    elif score <= 4:
        style.configure("bar.Horizontal.TProgressbar", background="orange")
        result_label.config(text="Moderate password", fg="orange")
    else:
        style.configure("bar.Horizontal.TProgressbar", background="green")
        result_label.config(text="Strong password", fg="green")

    score_label.config(text=f"Score: {score}/5")

    # Feedback
    if feedback:
        for issue in feedback:
            feedback_text.insert(tk.END, f"- {issue}\n")
    else:
        feedback_text.insert(tk.END, "No issues found")


def toggle_password():
    entry.config(show="" if show_var.get() else "*")


def clear():
    entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)
    result_label.config(text="")
    score_label.config(text="")
    progress["value"] = 0


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

# Real-time binding the function real_time_validation with every key release
entry.bind("<KeyRelease>", real_time_validation)

# Clearing Button
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Clear", width=12, command=clear).grid(row=0, column=0)


root.mainloop()
