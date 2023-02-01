import tkinter as tk
from tkinter import ttk
from algo import selection_sort, insertion_sort, bubble_sort, quick_sort, binary_search, linear_search, reset
import time


def render_list(frame, list1, delay=0):
    for i, num in enumerate(list1):
        box = ttk.Entry(frame, width=2, justify='center')
        box.insert(0, num)
        box.config(state='disabled')
        box.grid(row=0, column=i, padx=5)
    root.update_idletasks()
    if (delay > 0): time.sleep(delay)
    return

def visualizale(algo_type, numbers_arr, search_key):
    visualization_window = tk.Toplevel(root)
    visualization_window.title('Visualization')
    frame = ttk.Frame(visualization_window)
    frame.grid(row=0, column=0, padx=20, pady=20)

    render_list(frame, numbers_arr)
    if algo_type == 'selection':
        result = selection_sort(numbers_arr, (lambda rl: render_list(frame, rl, 1)))
        result = f'Sorted Array: {str(result)}'
    elif algo_type == 'insertion':
        result = insertion_sort(numbers_arr, (lambda rl: render_list(frame, rl, 1)))
        result = f'Sorted Array: {str(result)}'
    elif algo_type == 'bubble':
        result = bubble_sort(numbers_arr, (lambda rl: render_list(frame, rl, 1)))
        result = f'Sorted Array: {str(result)}'
    elif algo_type == 'quick':
        result = quick_sort(numbers_arr, (lambda rl: render_list(frame, rl, 1)))
        result = f'Sorted Array: {str(result)}'
    elif algo_type == 'linear_s':
        result = linear_search(eval(search_key), numbers_arr)
        result = f'Found Index: {str(result)}'
    elif algo_type == 'binary_s':
        result = binary_search(eval(search_key), numbers_arr)
        result = f'Found Index: {str(result)}'
    label.config(text=result)

def on_button_click(algo_type):
    search_key=key.get()
    text = entry.get()
    if text=="":
        label.config(text="Enter only numbers with comma as seperator");
        return
    elif search_key=="" and (algo_type == 'linear_s' or algo_type == 'binary_s'):
        label.config(text="You must enter a value to search");
        return
    else:
        numbers=text.split(",");

    numbers_arr=[];
    for i in range(len(numbers)):
        numbers_arr.append(eval(numbers[i]));

    if algo_type == 'reset':
        reset(numbers_arr)
        result = 'Result will appear here...'
        label.config(text=result)
        entry.config(text="")
        key.config(text="")
    else:
        visualizale(algo_type, numbers_arr, search_key)


#################################
#### GUI SETUP               ####
#################################

# main window settings
root = tk.Tk()
root.title("Sorting")
# root.(height=720, width=1280)

# styling
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

frame = ttk.Frame(root)
frame.pack(fill="both", expand=True)

# Create an Entry widget
label_for_array = ttk.Label(frame, width=50, text="Enter array: (comma seperated)")
label_for_array.grid(row=0, column=0, padx=10, pady=20)
entry = ttk.Entry(frame, width=50)
entry.grid(row=1, column=0, padx=10)

label_for_key = ttk.Label(frame, width=30, text="Enter value to find:")
label_for_key.grid(row=0, column=1, padx=10, pady=20)
key=ttk.Entry(frame,width=30)
key.grid(row=1, column=1, padx=10)

# Create a Button widget
button1 = ttk.Button(
    frame,
    text="Selection Sort!",
    command=(lambda: on_button_click('selection')),
    width=25
)
button1.grid(row=3, column=0, padx=20, pady=20)

button2 = ttk.Button(
    frame,
    text="Insertion Sort!",
    command=(lambda: on_button_click('insertion')),
    width=25
)
button2.grid(row=4, column=0, padx=20, pady=20)

button3 = ttk.Button(
    frame,
    text="Bubble Sort!",
    command=(lambda: on_button_click('bubble')),
    width=25
)
button3.grid(row=5, column=0, padx=20, pady=20)

button4 = ttk.Button(
    frame,
    text="Quick Sort!",
    command=(lambda: on_button_click('quick')),
    width=25
)
button4.grid(row=6, column=0, padx=20, pady=20)

button5=ttk.Button(
    frame,
    text="Linear Search!",
    command=(lambda: on_button_click('linear_s')),
    width=25
)
button5.grid(row=4, column=1, padx=5, pady=20)

button6=ttk.Button(
    frame,
    text="Binary Search!",
    command=(lambda: on_button_click('binary_s')),
    width=25
)
button6.grid(row=5, column=1, padx=5, pady=20)

reset_button=ttk.Button(
    frame,
    text="Reset",
    command=(lambda: on_button_click('reset')),
    width=25
)
reset_button.grid(row=6, column=1, padx=5, pady=20)

# Label to show result
label = ttk.Label(frame, text="Result will appear here...")
label.grid(row=2, column=0, columnspan=2, padx=20, pady=30)

footer_frame = ttk.Frame(root)
footer_frame.pack(fill="both", expand=True)
footer_label = ttk.Label(
    footer_frame,
    text="Made with ❤️ by Abdul Rehman Daniyal, Abdul Moiz Siddiqui & Muhammad Hamza Pervez.",
    anchor='center'
)
footer_label.grid(row=0, column=0, padx=50, pady=10)

root.mainloop()