from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox,filedialog
import pymysql
import time
import mysql.connector as connector
import os
import pandas


class student:
    def __init__(self,root):
         self.root =root
         self.root.geometry("1530x790+0+0")
         #root.iconbitmap('log')
         #root.tk.call('wm', 'iconphoto', root.w, tk.PhotoImage(file='logo.png')
         self.root.iconphoto(False, tk.PhotoImage(file='logo.png'))
         self.root.title("STUDENT MANAGEMENT SYSTEM")
#===========================

         self.txt_room_no_var=StringVar()
         self.txt_name_var=StringVar()
         self.txt_father_var=StringVar()
         self.txt_sur_name_var=StringVar()
         self.txt_fcn_var=StringVar()
         self.txt_email_var=StringVar()
         self.cmb_gen_var=StringVar()
         self.txt_contact_var=StringVar()
         self.txt_dob_var=StringVar()
         self.txt_city_var=StringVar()
         self.cmb_rpd_var=StringVar()
         self.txt_class_s_var=StringVar()
         self.txt_address_var=StringVar()
         self.txt_search_by_var = StringVar()
         self.txt_text_by_var = StringVar()
         #self.clock=StringVar()


         f1=Frame(self.root,bg="white", borderwidth=5,relief=GROOVE)
         f1.place(width=1530,height=60)

         l=Label(f1,text="HOSTEL MANAGEMENT SYSTEM",fg="green",font=("times new roman", 30,"bold"),bg="white").place(x=400,y=0)

         self.clock = Label(f1, bg="white", borderwidth=0, relief=GROOVE, font=("times new roman", 20, "bold"),fg='green')
         self.clock.place(x=11, y=7)
         self.tick()

         self.clock1 = Label(f1, bg="white", borderwidth=0, relief=GROOVE, font=("times new roman", 20, "bold"),fg='green')
         self.clock1.place(x=1300, y=7)
         self.tick1()

         #===========================
         f2 = Frame(self.root, bg="red", borderwidth=5, relief=GROOVE)
         f2.place(x=0,y=60,width=600, height=730)

         l1=Label(f2,text="STUDENT MANAGEMENT ",fg="white",font=("times new roman", 30,"bold"),bg="red").place(x=20,y=0)




         room_no = Label(f2, text="ROOM NO.", font=("times new roman", 15, "bold"), bg="red", fg="black").place(x=20,y=60)
         self.txt_room_no = Entry(f2, font=("times new roman", 15), bg="white",textvariable=self.txt_room_no_var)
         self.txt_room_no.place(x=20, y=90, width=250)

         f_name = Label(f2, text="NAME", font=("times new roman", 15, "bold"), bg="red", fg="black").place(x=330, y=60)
         self.txt_name = Entry(f2, font=("times new roman", 15), bg="white",textvariable=self.txt_name_var)
         self.txt_name.place(x=330, y=90, width=250)


         # ===========-------------row2------------
         father_name = Label(f2, text="Father Name", font=("times new roman", 15, "bold"), bg="red", fg="black").place(
             x=20, y=130)
         self.txt_father = Entry(f2, font=("times new roman", 15), bg="white",textvariable=self.txt_father_var)
         self.txt_father.place(x=20, y=170, width=250)

         sur_name = Label(f2, text="SURNAME", font=("times new roman", 15, "bold"), bg="red", fg="black").place(x=330,
                                                                                                                y=130)
         self.txt_sur_name = Entry(f2, font=("times new roman", 15), bg="white",textvariable=self.txt_sur_name_var)
         self.txt_sur_name.place(x=330, y=170, width=250)

         fcn = Label(f2, text="FATHER CONTACT_NO.", font=("times new roman", 15, "bold"), bg="red", fg="black").place(
             x=20,
             y=220)
         self.txt_fcn = Entry(f2, font=("times new roman", 15), bg="white",textvariable=self.txt_fcn_var)
         self.txt_fcn.place(x=20, y=250, width=250)

         email = Label(f2, text="Email", font=("times new roman", 15, "bold"), bg="red", fg="black").place(x=330,
                                                                                                             y=220)
         self.txt_email = Entry(f2, font=("times new roman", 15), bg="white",textvariable=self.txt_email_var)
         self.txt_email.place(x=330, y=250, width=250)

         # =====----------row3--------------
         gender = Label(f2, text="Gender", font=("times new roman", 15, "bold"), bg="red",
                          fg="black").place(x=20, y=300)
         self.cmb_gen = ttk.Combobox(f2, font=("times new roman", 13), state='readonly', justify=CENTER,textvariable=self.cmb_gen_var)
         self.cmb_gen['value'] = ("Select", "Male", "Female", "other",)
         self.cmb_gen.place(x=20, y=330, width=250)
         self.cmb_gen.current(0)

         contact = Label(f2, text="Mobile No.", font=("times new roman", 15, "bold"), bg="red", fg="black").place(x=330,
                                                                                                            y=300)
         self.txt_contact = Entry(f2, font=("times new roman", 15),  bg="white",textvariable=self.txt_contact_var)
         self.txt_contact.place(x=330, y=330, width=250)
         # ===========-------------row4------------
         dob = Label(f2, text="DOB", font=("times new roman", 15, "bold"), bg="red", fg="black").place(x=20,
                                                                                                                   y=380)
         self.txt_dob = Entry(f2, font=("times new roman", 15), bg="white",textvariable=self.txt_dob_var)
         self.txt_dob.place(x=20, y=410, width=250)

         city = Label(f2, text="VILLAGE/CITY", font=("times new roman", 15, "bold"), bg="red",
                          fg="black").place(x=330, y=380)
         self.txt_city = Entry(f2, font=("times new roman", 15),  bg="white",textvariable=self.txt_city_var)
         self.txt_city.place(x=330, y=410, width=250)

         room_payment_detail = Label(f2, text="ROOM PAYMENT STATUS", font=("times new roman", 15, "bold"), bg="red",
                        fg="black").place(x=20, y=460)
         self.cmb_rpd = ttk.Combobox(f2, font=("times new roman", 13), state='readonly', justify=CENTER,textvariable=self.cmb_rpd_var)
         self.cmb_rpd['value'] = ("Select", "complete payment", "due payment")
         self.cmb_rpd.place(x=20, y=500, width=250)
         self.cmb_rpd.current(0)

         class_s = Label(f2, text="CLASS", font=("times new roman", 15, "bold"), bg="red",
                          fg="black").place(x=330, y=460)
         self.txt_class_s = Entry(f2, font=("times new roman", 15),  bg="white",textvariable=self.txt_class_s_var)
         self.txt_class_s.place(x=330, y=500, width=250)


         address = Label(f2, text="PERMANENT ADDRESS.. ", font=("times new roman", 15, "bold"), bg="red",
                      fg="black").place(x=20, y=550)
         self.txt_address = Entry(f2, font=("times new roman", 15), bg="white",textvariable=self.txt_address_var)
         self.txt_address.place(x=20, y=580, width=560,height=60)

         add = Button(f2, text="Add",bd=5, bg="black", fg="white",relief=SUNKEN,cursor="hand2",font=("times new roman", 20,"bold"),command=self.student_manage).place(x=50, y=650)
         update = Button(f2,  text="Update",   cursor="hand2",font=("times new roman", 20,"bold"),command=self.update,bg="black",bd=5, fg="white",relief=SUNKEN).place(x=170, y=650)
         delete = Button(f2,  text="Delete",  cursor="hand2",font=("times new roman", 20,"bold"),command=self.delete,bg="black",bd=5, fg="white",relief=SUNKEN).place(x=320,y=650)
         clear= Button(f2,  text="Clear", cursor="hand2",font=("times new roman", 20,"bold"), bg="black",bd=5, fg="white",relief=SUNKEN,command= self.clear).place(x=460, y=650)


         # ====------------terms===---------------

         f3 = Frame(self.root, bg="red", borderwidth=5, relief=GROOVE)
         f3.place(x=600, y=60, width=928, height=730)

         l2= Label(f3, text="Search By ", fg="white", font=("times new roman", 25, "bold"), bg="red").place(
             x=10, y=20)
         self.cmb_ser= ttk.Combobox(f3, font=("times new roman", 13), state='readonly', justify=CENTER,textvariable=self.txt_search_by_var)
         self.cmb_ser['value'] = ("Select Option", "Room_no", "Name")
         self.cmb_ser.place(x=185, y=30, width=200)
         self.cmb_ser.current(0)

         self.txt_free = Entry(f3, font=("times new roman", 15), bg="white",textvariable=self.txt_text_by_var)
         self.txt_free.place(x=400, y=30, width=200)

         search = Button(f3, text="Search", cursor="hand2", font=("times new roman", 12, "bold"),command=self.search, bg="white", bd=0,
                         fg="black", relief=SUNKEN).place(x=630, y=30,width=120)
         show_all = Button(f3, text="Show All", cursor="hand2", font=("times new roman", 12, "bold"), bg="white", bd=0,
                       command=self.fetch_data, fg="black", relief=SUNKEN).place(x=780, y=5,width=120)
         save= Button(f3, text="Save All", cursor="hand2", font=("times new roman", 12, "bold"),command=self.save_as, bg="white", bd=0,
                            fg="black", relief=SUNKEN).place(x=780, y=45, width=120)

         Table_Frame = Frame(f3, borderwidth=5, relief=RIDGE,bg="crimson")
         Table_Frame.place(width=919, height=640,y=80)

         style=ttk.Style()

         style.configure('Treeview.Heading',font=("times new roman", 15,"bold"),foreground="blue")
         style.configure('Treeview',font=("times new roman", 13,"bold"),foreground="green",background="red")

         scroll_x=Scrollbar(Table_Frame,orient="horizontal")
         #self.txt = Text(Table_Frame, yscrollcommand=scroll_x.set)
         scroll_y = Scrollbar(Table_Frame, orient="vertical")
         #self.txt = Text(Table_Frame, yscrollcommand=scroll_y.set)
#===================only create column==========
         self.Student_table=ttk.Treeview(Table_Frame,column=("Room_no","Name","father_name","sur_name","Father contact_no.","Email","Gender",
                    "Contact_no","Dob","village/city","room payment status","Class","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)



         scroll_x.pack(side="bottom",fill=X)
         scroll_y.pack(side="right", fill=Y)
        # self.txt = Text(F3, yscrollcommand=scroll_y.set)
         scroll_x.config(command=self.Student_table.xview)
         scroll_y.config(command=self.Student_table.yview)
#==============show all name================
         self.Student_table.heading("Room_no", text="Room_no")
         self.Student_table.heading("Name", text="Name")
         self.Student_table.heading("father_name", text="Father_name")
         self.Student_table.heading("sur_name", text="Surname")
         self.Student_table.heading("Father contact_no.", text="Father contact_no.")
         self.Student_table.heading("Email", text="Email")
         self.Student_table.heading("Gender", text="Gender")
         self.Student_table.heading("Contact_no", text="Contact_no")
         self.Student_table.heading("Dob", text="D.O.B")
         self.Student_table.heading("village/city", text="village/city")
         self.Student_table.heading("room payment status", text="room payment status")
         self.Student_table.heading("Class", text="Class")
         self.Student_table.heading("Address", text="Address")
         self.Student_table["show"]="headings"
         self.Student_table.column("Room_no",width=100)
         self.Student_table.column("Gender", width=100)
         self.Student_table.column("room payment status", width=150)
         self.Student_table.column("Address", width=300)
         self.Student_table.pack(fill="both",expand=1)
         self.Student_table.bind("<ButtonRelease>",self.get_cursor)
         self.fetch_data()


    def tick(self):
        time_string= time.strftime("%H:%M:%S")

        self.clock.config(text="Time :"+time_string)
        self.clock.after(200, self.tick)

    def tick1(self):

        date_string = time.strftime("%d/%m/%Y")
        #print(time_string, date_string )

        self.clock1.config(text='Date :'+date_string )

    def student_manage(self):

     if self.txt_room_no_var.get()=="" or self.txt_name_var.get()=="" or self.txt_father_var.get()=="" or self.txt_sur_name_var.get()=="" or self.txt_fcn_var.get()=="" or self.txt_email_var.get()=="" or self.cmb_gen_var.get()=="" or self.txt_contact_var.get()=="" or self.txt_dob_var.get()=="" or self.txt_city_var.get()=="" or self.cmb_rpd_var.get()=="" or self.txt_class_s_var.get()=="" or self.txt_address_var.get()=="":
      messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
      try:
             con = connector.connect(host="localhost", user="root", port='3306', password="Sunil@123",database='student_management1')
             cur = con.cursor()
             cur.execute("select * from student1 where email= %s", (self.txt_email.get(),))
             row = cur.fetchone()
             ## print(row)
             if row != None:
                messagebox.showerror("Error", "User already exist ,please try with another email", parent=self.root)

             else:
              cur.execute(
                       "insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (
                           self.txt_room_no_var.get(),
                           self.txt_name_var.get(),
                           self.txt_father_var.get(),
                           self.txt_sur_name_var.get(),
                           self.txt_fcn_var.get(),
                           self.txt_email_var.get(),
                           self.cmb_gen_var.get(),
                           self.txt_contact_var.get(),
                           self.txt_dob_var.get(),
                           self.txt_city_var.get(),
                           self.cmb_rpd_var.get(),
                           self.txt_class_s_var.get(),
                           self.txt_address_var.get()
                       ))
             con.commit()
             self.fetch_data()
             self.clear()
             con.close()
      except Exception as es:
       messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


    def fetch_data(self):
                 con = connector.connect(host="localhost", user="root", port='3306', password="Sunil@123",database='student_management1')
                 cur = con.cursor()
                 cur.execute("select * from student1")
                 rows = cur.fetchall()
                 # print(row)
                 if len(rows)!= 0:
                     self.Student_table.delete(*self.Student_table.get_children())
                 for row in rows:
                     self.Student_table.insert("",END,values=row)
                 con.commit()
                 con.close()

    def clear(self):
        self.txt_room_no_var.set("")
        self.txt_name_var.set("")
        self.txt_father_var.set("")
        self.txt_sur_name_var.set("")
        self.txt_fcn_var.set("")
        self.txt_email_var.set("")
        self.cmb_gen_var.set("")
        self.txt_contact_var.set("")
        self.txt_dob_var.set("")
        self.txt_city_var.set("")
        self.cmb_rpd_var.set("")
        self.txt_class_s_var.set("")
        self.txt_address_var.set("")



    def get_cursor(self,ev):
        curosor_row= self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents["values"]
        #print(row)

        self.txt_room_no_var.set(row[0])
        self.txt_name_var.set(row[1])
        self.txt_father_var.set(row[2])
        self.txt_sur_name_var.set(row[3])
        self.txt_fcn_var.set(row[4])
        self.txt_email_var.set(row[5])
        self.cmb_gen_var.set(row[6])
        self.txt_contact_var.set(row[7])
        self.txt_dob_var.set(row[8])
        self.txt_city_var.set(row[9])
        self.cmb_rpd_var.set(row[10])
        self.txt_class_s_var.set(row[11])
        self.txt_address_var.set(row[12])

    def update(self):
        con = connector.connect(host="localhost", user="root", port='3306', password="Sunil@123",database='student_management1')
        cur = con.cursor()
        cur.execute( "update student1 set name=%s,father_name=%s,surname=%s,father_contact_no=%s,email=%s,gender=%s,contact=%s,dob=%s,city=%s,room_payment_status=%s,class_s=%s,address=%s where room_no=%s",
            (   self.txt_name_var.get(),
                self.txt_father_var.get(),
                self.txt_sur_name_var.get(),
                self.txt_fcn_var.get(),
                self.txt_email_var.get(),
                self.cmb_gen_var.get(),
                self.txt_contact_var.get(),
                self.txt_dob_var.get(),
                self.txt_city_var.get(),
                self.cmb_rpd_var.get(),
                self.txt_class_s_var.get(),
                self.txt_address_var.get(),
                self.txt_room_no_var.get()
            ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


#==========
    def delete(self):

        aa=messagebox.askyesno(" Notification", "Are you sure ,Student data is delete", parent=self.root)
        if(aa == 0) :
            self.clear()
        con = connector.connect(host="localhost", user="root", port='3306', password="Sunil@123",database='student_management1')
        cur = con.cursor()

        cur.execute( "delete from student1 where room_no=%s",(self.txt_room_no_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()



#=============
    def search(self):
        if self.txt_search_by_var.get() == "" or self.txt_text_by_var.get() == "":
            messagebox.showerror("Error", "Please select option and fill search data ", parent=self.root)
        else:
                 con = connector.connect(host="localhost", user="root", port='3306', password="Sunil@123",database='student_management1')
                 cur = con.cursor()
                 cur.execute("select * from student1 where "+str(self.txt_search_by_var.get())+" Like '%"+str(self.txt_text_by_var.get())+"%'")
                 rows = cur.fetchall()
                 # print(row)
                 if len(rows)!= 0:
                     self.Student_table.delete(*self.Student_table.get_children())
                 for row in rows:
                     self.Student_table.insert("",END,values=row)
                 con.commit()
                 con.close()

    def save_as(self):
        # =========save file ke liye

        #self.bill_data = self.Student_table.get('1.0', END)
        #ff = filedialog.asksaveasfilename()
        f1 = open("bills/" + str(self.txt_room_no_var.get()) + ".txt", "w")

        #f1.write(self.bill_data)
        f1.close()


# =
root = Tk()
obj = student(root)
root = mainloop()