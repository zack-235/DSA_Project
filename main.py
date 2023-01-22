import tkinter as tk

def get_text():
    text = entry.get()
    label.config(textvariable=text);



root = tk.Tk()
root.minsize(width=600, height=400);

# Create a text input field
entry = tk.Entry(root)
entry.pack()

stringvar=tk.StringVar();
stringvar.set("");

button = tk.Button(root, text="Get Text", command=get_text)
button.pack()

label=tk.Label(root, text="result will show here!");
label.pack();



root.mainloop()

