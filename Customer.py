from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_win:
    def __init__(self, root):
        self.root=root
        self.root.title("Movie Ticket Booking System")
        self.root.geometry("1200x495+230+260") 

    #===============variables================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_postcode=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()
    



    #================title===================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1200,height=50)   


    #========================logo================
        img2=Image.open(r"C:\Users\chinm\OneDrive\Desktop\DBMS_Mini_project\logo.png")
        img2=img2.resize((100,80),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=SOLID)
        lblimg.place(x=5,y=2,width=100,height=46)

    #===============label frame===============
        labelframeleft=LabelFrame(self.root,bd=2,relief=SOLID,text="Customer Details",padx=2,font=("arial",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)
    #================labels and entrys==========
    #cust reference
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",12,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

    #cust name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",12,"bold"))
        txtcname.grid(row=1,column=1)

    #gender
        lbl_gen=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gen.grid(row=3,column=0,sticky=W)

        combo_gen=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gen["value"]=("Male","Female","Other")
        combo_gen.current(0)
        combo_gen.grid(row=3,column=1)

    #post code
        lbl_post=Label(labelframeleft,text="Post Code:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_post.grid(row=4,column=0,sticky=W)
        entry_post=ttk.Entry(labelframeleft,textvariable=self.var_postcode,width=29,font=("arial",13,"bold"))
        entry_post.grid(row=4,column=1)

    
    #Mobile Number
        lbl_mob=Label(labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_mob.grid(row=5,column=0,sticky=W)
        entry_mob=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        entry_mob.grid(row=5,column=1)

    #Email ID
        lbl_mob=Label(labelframeleft,text="Email ID:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_mob.grid(row=6,column=0,sticky=W)
        entry_mob=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
        entry_mob.grid(row=6,column=1)


    #ID Proof
        lbl_proof=Label(labelframeleft,text="Proof:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_proof.grid(row=8,column=0,sticky=W)
        
        combo_proof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_proof["value"]=("Aadhar Card","Driving License","Pan Card","Passport")
        combo_proof.current(0)
        combo_proof.grid(row=8,column=1)

    #ID Number
        lbl_mob=Label(labelframeleft,text="ID Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_mob.grid(row=9,column=0,sticky=W)
        entry_mob=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=29,font=("arial",13,"bold"))
        entry_mob.grid(row=9,column=1)

    #Address Number
        lbl_add=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_add.grid(row=10,column=0,sticky=W)
        entry_add=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        entry_add.grid(row=10,column=1)

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
    #===============label frame===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=SOLID,text="View Details And Search System",padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=490)
 
        lbl_searchby=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile Number","Reference Number")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        entry_search=ttk.Entry(Table_Frame,width=24,font=("arial",13,"bold"))
        entry_search.grid(row=0,column=2,padx=2)

        btnsearch=Button(Table_Frame,text="Search",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(Table_Frame,text="Show All",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)

    #===============show data table============
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","gender","postcode","mobile",
                                                                   "email","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("postcode",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile No")
        self.Cust_Details_Table.heading("email",text="Email ID")
        self.Cust_Details_Table.heading("idproof",text="ID Proof")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")
        
        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("postcode",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_mobile.get()=="" or self.var_postcode.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Chinmay33@9",database="dbms_mini_project")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_postcode.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_idproof.get(),
                                                                                    self.var_idnumber.get(),
                                                                                    self.var_address.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been Added!",parent=self.root)
                
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Chinmay33@9",database="dbms_mini_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
        for i in rows:
            self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_postcode.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_idproof.set(row[6]),
        self.var_idnumber.set(row[7]),
        self.var_address.set(row[8])

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
            query="delete from customer where ref=%s"
            value=[(self.var_ref.get())]
            my_cursor.execute(query,value)

        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
            reset=messagebox.askyesno("Movie Ticket Booking System","Do you want to reset??",parent=self.root)
            if reset>0:
                messagebox.showinfo("Reset","Reset is not Available",parent=self.root)
            else:
                messagebox.showinfo("Reset","You can Proceed!!!!",parent=self.root)



    
                
        

if __name__ =="__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()