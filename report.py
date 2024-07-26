from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Report:
    def __init__(self, root):
        self.root=root
        self.root.title("Movie Ticket Booking System")
        self.root.geometry("1200x495+230+260") 

        messagebox.showinfo("Report","You Need Permission!!!\nPlease Contact to Office")


if __name__ =="main":
    root=Tk()
    obj=Report(root)
    root.mainloop()