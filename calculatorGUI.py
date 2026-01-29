import tkinter as tk
window=tk.Tk()
window.title('MY CALCULATOR')
window.configure(bg='lightblue')
def click(value):
    entry.insert(tk.END,value) 
    
def calculate():
    result=eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(0,result)
    
def clear():
    entry.delete(0,tk.END)
    
label=tk.Label(window,text="CALCULATOR",font=("ARIAL BOLD",50),fg=("orange"))
label.grid(row=0, column=0, columnspan=4, pady=10)
entry=tk.Entry(window,width=20,font=("ARIAL",20))
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('/', 5, 1)
]
for text, row, col in buttons:
    tk.Button(window, text=text, width=5, height=2,
              command=lambda t=text: click(t)
              ).grid(row=row, column=col,padx=3,pady=5)

tk.Button(window,text="=", width=5, height=2,command=calculate).grid(row=5, column=2)
tk.Button(window,text="CLEAR", width=5, height=2,command=clear).grid(row=5, column=3)
window.mainloop()
