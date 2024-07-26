from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Booking:
    def __init__(self, root):
        self.root=root
        self.root.title("Movie Ticket Booking System")
        self.root.geometry("1200x495+230+260") 

    #===============variables=====================

        self.var_mobile=StringVar()
        self.var_Movie_Date=StringVar()
        self.var_Movie_Name=StringVar()
        self.var_Seats=StringVar()
        self.var_Time=StringVar()
        self.var_Payment=StringVar()

    #================title===================
        lbl_title=Label(self.root,text="MOVIE BOOKING DETAILS",font=("times new roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1200,height=50)   


    #========================logo================
        img2=Image.open(r"C:\Users\chinm\OneDrive\Desktop\DBMS_Mini_project\logo.png")
        img2=img2.resize((100,80),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=SOLID)
        lblimg.place(x=5,y=2,width=100,height=46)

    #===============label frame===============
        labelframeleft=LabelFrame(self.root,bd=2,relief=SOLID,text="Booking Details",padx=2,font=("arial",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

    #================labels and entrys==========
    #cust Mobile
        lbl_cust_mobile=Label(labelframeleft,text="Customer Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_mobile.grid(row=0,column=0,sticky=W)

        entry_mobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=20,font=("arial",12,"bold"))
        entry_mobile.grid(row=0,column=1,sticky=W)

    #Fetch Data
        btnfetch=Button(labelframeleft,command=self.fetch_mobile,text="Fetch",font=("arial",13,"bold"),bg="black",fg="gold",width=6)
        btnfetch.place(x=325,y=4)

    #Movie Date
        lbl_Date=Label(labelframeleft,text="Date",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Date.grid(row=1,column=0,sticky=W)

        entry_Date=ttk.Entry(labelframeleft,textvariable=self.var_Movie_Date,width=29,font=("arial",12,"bold"))
        entry_Date.grid(row=1,column=1)

    #Movie Name
        lbl_Mov_name=Label(labelframeleft,text="Movie Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Mov_name.grid(row=2,column=0,sticky=W)

        combo_mov_name=ttk.Combobox(labelframeleft,textvariable=self.var_Movie_Name,font=("arial",12,"bold"),width=27,state="readonly")
        combo_mov_name["value"]=("Yeh Jawaani Hai Deewani","Brahmastra","Deol Band","RRR")
        combo_mov_name.current(0)
        combo_mov_name.grid(row=2,column=1)

    #Available seats
        lbl_Seats=Label(labelframeleft,text="Seats:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Seats.grid(row=3,column=0,sticky=W)

        entry_Seats=ttk.Entry(labelframeleft,textvariable=self.var_Seats,width=29,font=("arial",12,"bold"))
        entry_Seats.grid(row=3,column=1)



    #Time
        lbl_Seats=Label(labelframeleft,text="Time:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Seats.grid(row=4,column=0,sticky=W)

        combo_mov_name=ttk.Combobox(labelframeleft,textvariable=self.var_Time,font=("arial",12,"bold"),width=27,state="readonly")
        combo_mov_name["value"]=("9AM TO 12AM","1PM TO 4PM","6PM TO 9PM","9PM TO 12PM")
        combo_mov_name.current(0)
        combo_mov_name.grid(row=4,column=1)

    #Payment
        lbl_Seats=Label(labelframeleft,text="Total Price:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Seats.grid(row=5,column=0,sticky=W)

        entry_Seats=ttk.Entry(labelframeleft,textvariable=self.var_Payment,width=29,font=("arial",12,"bold"),state="readonly")
        entry_Seats.grid(row=5,column=1)
    

    #=================Total Price==============

        btntotal=Button(labelframeleft,text="Total",command=self.total,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btntotal.grid(row=6,column=0,padx=1,sticky=W)

    #===============button frame================
        btn_frame=Frame(labelframeleft,bd=2,relief=SOLID)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)
    #================right side================
        img3=Image.open(r"C:\Users\chinm\OneDrive\Desktop\DBMS_Mini_project\MovieSeats.jpg")
        img3=img3.resize((520,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=440,height=200)




    #===============label frame===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=SOLID,text="View Details And Search System",padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=280,width=780,height=260)
 
        lbl_searchby=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Time","Movie Name")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        entry_search=ttk.Entry(Table_Frame,width=24,font=("arial",13,"bold"))
        entry_search.grid(row=0,column=2,padx=2)

        btnsearch=Button(Table_Frame,text="Search",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(Table_Frame,text="Show All",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)


    #===============show data table========================
        details_table=Frame(Table_Frame,bd=2,relief=SOLID)
        details_table.place(x=0,y=50,width=800,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Booking_Table=ttk.Treeview(details_table,column=("Mobile","Movie Date","Movie Name","Seats","Time",
                                                                   "Payment"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Booking_Table.xview)
        scroll_y.config(command=self.Booking_Table.yview)

        self.Booking_Table.heading("Mobile",text="Mobile")
        self.Booking_Table.heading("Movie Date",text="Movie Date")
        self.Booking_Table.heading("Movie Name",text="Movie Name")
        self.Booking_Table.heading("Seats",text="Seats")
        self.Booking_Table.heading("Time",text="Time")
        self.Booking_Table.heading("Payment",text="Payment")
        
        self.Booking_Table["show"]="headings"

        self.Booking_Table.column("Mobile",width=100)
        self.Booking_Table.column("Movie Date",width=100)
        self.Booking_Table.column("Movie Name",width=100)
        self.Booking_Table.column("Seats",width=100)
        self.Booking_Table.column("Time",width=100)
        self.Booking_Table.column("Payment",width=100)
        
        self.Booking_Table.pack(fill=BOTH,expand=1)

        self.Booking_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data1()



    def add_data(self):
        if self.var_mobile.get()=="" or self.var_Movie_Date.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Chinmay33@9",database="dbms_mini_project")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into movie_booking values(%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_mobile.get(),
                                                                            self.var_Movie_Date.get(),
                                                                            self.var_Movie_Name.get(),
                                                                            self.var_Seats.get(),
                                                                            self.var_Time.get(),
                                                                            self.var_Payment.get()
                                                                        ))
                conn.commit()
                self.fetch_data1()
                conn.close()
                messagebox.showinfo("Success","Your Seat has been Reserved!",parent=self.root)
            
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #======================fetch data====================
    def fetch_data1(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Chinmay33@9",database="dbms_mini_project")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from movie_booking")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Booking_Table.delete(*self.Booking_Table.get_children())
                for i in rows:
                    self.Booking_Table.insert("",END,values=i)
                conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Booking_Table.focus()
        content=self.Booking_Table.item(cursor_row)
        row=content["values"]

        self.var_mobile.set(row[0]),
        self.var_Movie_Date.set(row[1]),
        self.var_Movie_Name.set(row[2]),
        self.var_Seats.set(row[3]),
        self.var_Time.set(row[5]),
        self.var_Payment.set(row[6]),
        

    #======================all fetch data=====================

    def fetch_mobile(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter mobile number") 

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Chinmay33@9",database="dbms_mini_project")
            my_cursor=conn.cursor()
            query=("Select name from Customer where mobile=%s")
            value=(self.var_mobile.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=455,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",username="root",password="Chinmay33@9",database="dbms_mini_project")
                my_cursor=conn.cursor()
                query=("Select gender from Customer where mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
 
                lblGen=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGen.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                conn=mysql.connector.connect(host="localhost",username="root",password="Chinmay33@9",database="dbms_mini_project")
                my_cursor=conn.cursor()
                query=("Select ref from Customer where mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
 
                lblref=Label(showDataframe,text="Ticket No.:",font=("arial",12,"bold"))
                lblref.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)
    


    def total(self):
        if self.var_Seats.get()=="":
            messagebox.showinfo("Details","Please Enter no. of seats")

        else:
            q1=float(250)
            q2=float(self.var_Seats.get())
            price=float(q1*q2)
            self.var_Payment.set(price)

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter mobile number",parent=self.root)

        else:
            messagebox.showinfo("Update","Update is not Available!",parent=self.root)


    def delete(self):
        delete=messagebox.askyesno("Movie Ticket Booking System","Do you want to delete??",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Chinmay33@9",database="dbms_mini_project")
            my_cursor=conn.cursor()
            query="delete from movie_booking where mobile=%s"
            value=[(self.var_mobile.get())]
            my_cursor.execute(query,value)

        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data1()
        conn.close()


    def reset(self):
            reset=messagebox.askyesno("Movie Ticket Booking System","Do you want to reset??",parent=self.root)
            if reset>0:
                messagebox.showinfo("Reset","Reset is not Available",parent=self.root)
            else:
                messagebox.showinfo("Reset","You can Proceed!!!!",parent=self.root)












if __name__ =="__main__":
    root=Tk()
    obj=Booking(root)
    root.mainloop()