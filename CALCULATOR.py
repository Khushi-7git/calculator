import tkinter as tk
import math
from PIL import Image,ImageTk

# Define button click behavior
def button_click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "x²":
        try:
            # Ensure input is a number before squaring
            number = float(current)
            result = number ** 2
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

# Create the window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")
img=Image.open('calculator.png')
img=img.resize((40,40))
photo=ImageTk.PhotoImage(img)
root.iconphoto(True,photo)
# Create an entry widget to display input and output
entry = tk.Entry(root, width=25, font=("Arial", 14), borderwidth=3, relief="raised", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=26, padx=8)

# Define button layout
buttons = [
    ('.', 1, 0), ('C', 1, 1), ('x²', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('0', 5, 2), ('=', 5, 3),
     
]

# Define button style
button_style = {
    'font': ("Arial", 18),
    'width': 5,
    'height': 2,
    'bg': "#00FFFF",  # Background color
    'fg': "white",
    'bd': 2,
    'relief': "groove",  # Button relief
    'activebackground': "00FFFF",
    'activeforeground': "black"
}

#crete a button and palace it
for(text,row,col)in buttons:
    if text=="=":
      button=tk.Button(root,text=text,width=5,height=2,
                    font=("Arial",14),
                    command=lambda t=text:button_click(t),
                    fg=("white"),
                    bg=("#0504b7"),
                    relief='ridge',
                    activebackground=("#2c2bfa"),
                    activeforeground="black")   


                    
    else:
     button=tk.Button(root,text=text,width=5,height=2,font=("Arial",14),command=lambda t=text:button_click(t) **button_style)
    button.grid(row=row,column=col,padx=5,pady=5)
#create a clear button    
clear_button=tk.Button(root,text="C",width=5,height=2,font=("Arial",14),command=lambda: button_click("C"))
clear_button.grid(row=1,column=1)
#
#start event loop
root.mainloop()


