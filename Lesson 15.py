import tkinter as tk

root = tk.Tk()
root.title("Number Sign Checker")
root.geometry("400x400")

def check():
    user_input = entry.get()

    try:
        num = float(user_input)

        if num > 0:
            answer_label.config(text=f"{num} is Positive")
        elif num < 0:
            answer_label.config(text=f"{num} is Negative")
        else:
            answer_label.config(text=f"{num} is Zero")
    except ValueError:
        answer_label.config(text="Put in a number.")

entry = tk.Entry(root, width=20)
entry.pack(pady=15)

btn = tk.Button(root, text="Check Number", command=check)
btn.pack(pady=15)

answer_label = tk.Label(root, text="", font=("Arial", 11))
answer_label.pack(pady=15)

root.mainloop()