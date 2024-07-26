from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Details:
    def __init__(self, root):
        self.root=root
        self.root.title("Movie Ticket Booking System")
        self.root.geometry("1200x495+230+260") 

        messagebox.showinfo("Details","1.Be on time\n2.Sit in your allocated seat\n3.Have awareness of personal space\n4.Phones on silent\n5.Keep the chatter for the end of the movie")


if __name__ =="main":
    root=Tk()
    obj=Details(root)
    root.mainloop()