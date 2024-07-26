from tkinter import*
from PIL import Image,ImageTk  #install Pillow in cmd by writing pip install Pillow
from Customer import Cust_win
from MovieBooking import Booking
from Detailssssss import Details
from report import Report


class MovieTicketBookingSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Movie Ticket Booking System")
        self.root.geometry("1550x800+0+0")



    #=============1st image=====================
        img1=Image.open(r"C:\Users\chinm\OneDrive\Desktop\DBMS_Mini_project\Moviehall.jpg")
        img1=img1.resize((1550,180),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=SOLID)
        lblimg.place(x=0,y=0,width=1550,height=180)


    #========================logo================
        img2=Image.open(r"C:\Users\chinm\OneDrive\Desktop\DBMS_Mini_project\logo.png")
        img2=img2.resize((230,180),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=SOLID)
        lblimg.place(x=0,y=0,width=230,height=180)
    #================title======================
        lbl_title=Label(self.root,text="MOVIE BOOKING SYSTEM",font=("times new roman",40,"bold"),bg="pink",fg="black")
        lbl_title.place(x=0,y=180,width=1550,height=50)
    #================main frame=================
        main_frame=Frame(self.root,bd=4,relief=SOLID)
        main_frame.place(x=0,y=225,width=1550,height=620)
    #=====================menu=================
        lbl_title=Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=230,height=40)   

    #===============button frame================
        btn_frame=Frame(main_frame,bd=2,relief=SOLID)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        movie_btn=Button(btn_frame,text="MOVIES",command=self.booking_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        movie_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",command=self.report,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        #logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        #logout_btn.grid(row=4,column=0,pady=1)

    #=============right side image===============
        img3=Image.open(r"C:\Users\chinm\OneDrive\Desktop\DBMS_Mini_project\tickets.jpg")
        img3=img3.resize((1310,610),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=SOLID)
        lblimg1.place(x=225,y=0,width=1310,height=610)

    #=============down image========================
        img4=Image.open(r"C:\Users\chinm\OneDrive\Desktop\DBMS_Mini_project\down.jpg")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=SOLID)
        lblimg2.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\Users\chinm\OneDrive\Desktop\DBMS_Mini_project\down2.jpg")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=SOLID)
        lblimg3.place(x=0,y=420,width=230,height=200)
    
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def booking_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Booking(self.new_window)

    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)

    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=Report(self.new_window)








if __name__ =="__main__":
    root=Tk()
    obj=MovieTicketBookingSystem(root)
    root.mainloop()