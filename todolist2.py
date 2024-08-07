import tkinter as tk
from tkinter import PhotoImage, Label, Frame, Entry, Button, Listbox, Scrollbar, END, BOTH, LEFT, RIGHT, BOTTOM

root = tk.Tk()
root.title("To-Do-lo-list")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("Tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END, task)

def deleteTask():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)

        task_list.remove(selected_task)
        with open("Tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(f"{task}\n")

        listbox.delete(selected_task_index)
    except IndexError:
        pass

def openTaskFile():
    try:
        global task_list
        with open("Tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task.strip())
                listbox.insert(END, task.strip())

    except FileNotFoundError:
        with open('Tasklist.txt', 'w') as file:
            pass

# icon
Image_icon = PhotoImage(file="task.png")
root.iconphoto(False, Image_icon)

# top bar
TopImage = PhotoImage(file="topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#324056")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# delete button
Delete_icon = PhotoImage(file="delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()
