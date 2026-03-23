import tkinter as tk
from utils import check_password_strength, suggest_password

def check():
    password = entry.get()
    strength = check_password_strength(password)

    result_label.config(text=f"Strength: {strength}")

    suggestions_text.delete("1.0", tk.END)
    if strength == "Weak":
        suggestions = suggest_password(password)
        for s in suggestions:
            suggestions_text.insert(tk.END, f"- {s}\n")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

tk.Label(root, text="Enter Password:").pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

suggestions_text = tk.Text(root, height=10, width=40)
suggestions_text.pack(pady=10)

root.mainloop()