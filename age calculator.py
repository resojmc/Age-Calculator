import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Age Calculator")

def find_age():
    year = int(main_entry.get())
    month = int(second_entry.get())
    years_old = 2023 - year
    return years_old, month
    
def update_age():
    age = find_age()
    y = age[0]
    m = age[1]
    if y < 1 and m < 12:
        result_label.config(text=f"Aww, You're only {m} months old.")
    else:
        result_label.config(text=f"You're {y} years and {m} months old!")

main_label = tk.Label(root, text="Enter Birth Year")
main_label.pack()

main_entry = tk.Entry(root,)
main_entry.pack()

second_label = tk.Label(root, text="""Enter Birth Month Number
eg: Jan=1, Feb=2 etc..""")
second_label.pack()

second_entry = tk.Entry(root,)
second_entry.pack()

button = tk.Button(root, text="Go", command=update_age)
button.pack()

result_label = tk.Label(root, text="Results:")
result_label.pack()

root.mainloop()