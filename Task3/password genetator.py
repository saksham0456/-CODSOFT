from tkinter import *
import tkinter as tk
import random
import string


def generate_password():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + password)


def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())


root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("600x450")
root.configure(bg='#2b8cc4')
root.resizable(False,False)

Image_icon=PhotoImage(file="E:\CODSOFT PYTHON INTENSHIP\Task3\pics\Daco_5610966.png")
root.iconphoto(False, Image_icon)

heading=Label(root,text=" STRONG PASSWORD GENERATOR",font="Frutiger 20 bold",fg="white",bg="#2b8cc4")
heading.place(x=50,y=20)


length_label = tk.Label(root, text="Password Length:",width=15,height=1, font=("arial",17,"bold"), bg="#2b8cc4").place(x=190,y=100)

length_entry = tk.Entry(root,font=("helvetica",25))
length_entry.pack(padx=150,pady=180)


generate_button = tk.Button(root, text="Generate Password", command=generate_password,width=18,height=1, font=("arial",17,"bold"), bg="#2b8cc4").place(x=170,y=250)



password_label = tk.Label(root, text="",height=1,font=("arial",17,"bold"),bg="#2b8cc4")
password_label.pack()
password_label.place(x=130,y=350) 

root.mainloop()
