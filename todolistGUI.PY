import tkinter as tk
tasks = []
window=tk.Tk()
window.title('TO-DO LIST APPLICATION')
window.configure(bg='lightyellow')
label=tk.Label(window,text="TO-DO LIST",font=("ARIAL BOLD",50),fg=("green"),bg='lightyellow')
label.pack()
def add_tsk():
    task=entry.get()
    tasks.append(task)
    listbox.insert(tk.END,task)
    entry.delete(0,tk.END)
def delete_tsk():
    selected=listbox.curselection()
    if selected:
        index=selected[0] 
    listbox.delete(index)       
    tasks.pop(index)
entry=tk.Entry(window,width=25,font=("ARIAL",20))
entry.pack(pady=10)
listbox=tk.Listbox(window,width=50,font=("ARIAL",15))
listbox.pack(pady=10)
add_btn=tk.Button(window,text="ADD TASK",command=add_tsk)
add_btn.pack(pady=5)
delete_btn=tk.Button(window,text="DELETE TASK",command=delete_tsk)
delete_btn.pack(pady=5)
window.mainloop()