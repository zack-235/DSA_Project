import tkinter as tk
from tkinter import ttk
from algo import selection_sort, insertion_sort, bubble_sort

def on_button_click(algo_type):
    text = entry.get()
    if text=="":
        label.config(text="Enter only numbers with comma as seperator");
    else:
        numbers= text.split(",");

    numbers_arr=[];
    for i in range(len(numbers)):
        numbers_arr.append(eval(numbers[i]));
    print(algo_type, numbers_arr)

    if algo_type == 'selection':
        sorted_numbers = selection_sort(numbers_arr)
    elif algo_type == 'insertion':
        sorted_numbers = insertion_sort(numbers_arr)
    elif algo_type == 'bubble':
        sorted_numbers = bubble_sort(numbers_arr)
    label.config(text=sorted_numbers)

root = tk.Tk()
root.minsize(height=400, width=600);
root.title("Sorting");
# root.config(bg="#820ecf")

# Create an Entry widget
entry = tk.Entry(root, highlightthickness=2, borderwidth=1)
entry.config(width=50);
entry.grid(row=0, column=0, padx=150, pady=100)
# entry.config(background="red")

# Create a Button widget
button1 = tk.Button(
    root,
    text="Selection Sort!",
    command=(lambda: on_button_click('selection')),
    width=25
)
button1.grid(row=2, column=0, padx=20, pady=20)

button2 = tk.Button(
    root,
    text="Insertion Sort!",
    command=(lambda: on_button_click('insertion')),
    width=25
)
button2.grid(row=3, column=0, padx=20, pady=20)

button3 = tk.Button(
    root,
    text="Bubble Sort!",
    command=(lambda: on_button_click('bubble')),
    width=25
)
button3.grid(row=4, column=0, padx=20, pady=20)
# button.bind("a", on_button_click);

# Create a Label widget
label = tk.Label(root, text="")
label.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()