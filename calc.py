import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)

# Global expression variable
expression = ""

# Function to update display
def press(value):
    global expression
    expression += str(value)
    input_text.set(expression)

# Function to clear display
def clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Display screen
input_text = tk.StringVar()
input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(
    input_frame,
    textvariable=input_text,
    font=("Arial", 20),
    width=18,
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
]

for (text, row, col) in buttons:
    if text == "C":
        action = clear
    else:
        action = lambda x=text: press(x)

    tk.Button(
        button_frame,
        text=text,
        width=6,
        height=2,
        font=("Arial", 14),
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

# Equal button (separate for full width feel)
tk.Button(
    root,
    text="=",
    width=28,
    height=2,
    font=("Arial", 14),
    bg="lightblue",
    command=equal
).pack(pady=10)

root.mainloop()