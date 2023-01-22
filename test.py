import tkinter as tk
from tkinter import ttk
import array

def on_button_click():
    text = entry.get()
    if text=="":
        label.config(text="Enter only numbers with comma as seperator");

    else:
        numbers= text.split(",");

    numbers_arr=array.array("i",);
    for i in range(numbers.__len__()):
        numbers_arr[i]=str(numbers[i]);

    print(number_arr)

    # label.config(text=numbers)

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
button = tk.Button(root, text="Sort!", command=on_button_click, width=25)
button.grid(row=1, column=0, padx=20, pady=20)
# button.bind("a", on_button_click);

# Create a Label widget
label = tk.Label(root, text="")
label.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()