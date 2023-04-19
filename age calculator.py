import tkinter as tk

root = tk.Tk()
root.geometry("300x600")
root.title("Age Calculator")

def find_age():
    year = int(main_entry.get())
    age = 2023 - year
    return age

def update_age():
    age = find_age()
    if age >= 20 and age < 30:
        result_label.config(text=f"You're {age} years old! Not a teenager anymore!")
    elif age >= 30 and age < 40:
        result_label.config(text=f"You're {age} years old! How's Life?")
    elif age >= 40 and age < 60:
        result_label.config(text=f"You're {age} years young! Stay in shape!")
    elif age > 60:
        result_label.config(text=f"You're {age} years old! Wow!")
    else:
        result_label.config(text="")

main_label = tk.Label(root, text="Enter Birth Year")
main_label.pack()

main_entry = tk.Entry(root,)
main_entry.pack()

button = tk.Button(root, text="Go", command=update_age)
button.pack()

result_label = tk.Label(root, text="Results:")
result_label.pack()

root.mainloop()