from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1330x750+0+0")

        self.addmed_var = StringVar()
        self.refmed_var=StringVar()


        self.refno_var=StringVar() 
        self.compname_var=StringVar()
        self.medicinetype_var=StringVar()
        self.medicinename_var=StringVar()
        self.lotno_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideeffects_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.tabletprice_var=StringVar()
        self.product_var=StringVar()


        labeltitle=Label(self.root,text="Pharmacy Management System",bd=12,font=('times new roman',25),relief=RIDGE,bg='white'
                        ,fg='black',padx=1,pady=2)

        labeltitle.pack(side=TOP,fill=X)

        DataFramer = Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFramer.place(x=0,y=120,width=1350,height=400)

        DataFramerLeft = LabelFrame(DataFramer,bd=6,relief=RIDGE,padx=20,text="Medicine Info"
                        ,fg="darkgreen",font=500)

        DataFramerLeft.place(x=0,y=5,width=780,height=350)

        DataFramerRight = LabelFrame(DataFramer,bd=6,relief=RIDGE,padx=20,text="Add Medicines"
                        ,fg="darkgreen",font=500)

        DataFramerRight.place(x=800,y=5,width=450,height=350)


        ButtonFrame=Frame(self.root,bd=13,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1350,height=95)


        

        

        # ===========Search By========
        lblSearch=Label(ButtonFrame, font=("arial",17,"bold"),text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame, width=12, font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        txtSearch=Entry(ButtonFrame, bd=3,relief=RIDGE, width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)


        searchButton=Button(ButtonFrame,text="SEARCH",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        searchButton.grid(row=0,column=8)

        showAll = Button(ButtonFrame, text="SHOW ALL", font=("arial",13,"bold"),width=13, bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)

        # =====================Label And Entry========================
        lblref_no=Label(DataFramerLeft, font=("arial",12,"bold"),text="Reference no", padx=2)
        lblref_no.grid(row=0,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="shravan123",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from pharma")
        reqRef = my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFramerLeft,textvariable=self.refno_var, width=15, font=("arial",14,"bold"),state="readonly")
        ref_combo["values"]=reqRef
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        #===============Add Medicine===============


        lblCompName=Label(DataFramerLeft,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblCompName.grid(row=1,column=0,sticky=W)
        txtCompName=Entry(DataFramerLeft,textvariable=self.compname_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtCompName.grid(row=1,column=1)



        lblrefeno=Label(DataFramerLeft, font=("arial",12,"bold"),text="Type Of Medicine:", padx=2)
        lblrefeno.grid(row=2,column=0,sticky=W)


        refno_combo=ttk.Combobox(DataFramerLeft,textvariable=self.medicinetype_var, width=15, font=("arial",14,"bold"),state="readonly")
        refno_combo["values"]=("Tablet","Liquid","Drops","Injection","Capsule","Inhales")
        refno_combo.grid(row=2,column=1)
        refno_combo.current(0)

        conn=mysql.connector.connect(host="localhost",username="root",password="shravan123",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select medname from pharma")
        reqMedName=my_cursor.fetchall()

        lblMedicineName=Label(DataFramerLeft,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFramerLeft,textvariable=self.medicinename_var,state="readonly",font=("arial",14,"bold"),width=15)
        comMedicineName['values']=reqMedName
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)


        lblLotNo=Label(DataFramerLeft,font=("arial",12,"bold"),text="Lot No:",padx=1,pady=3)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFramerLeft,textvariable=self.lotno_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFramerLeft,font=("arial",12,"bold"),text="Issue Date:",padx=1,pady=3)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFramerLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFramerLeft,font=("arial",12,"bold"),text="Exp Date:",padx=1,pady=3)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFramerLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFramerLeft,font=("arial",12,"bold"),text="Uses:",padx=1,pady=2)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFramerLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtUses.grid(row=7,column=1)

        lblSideEffects=Label(DataFramerLeft,font=("arial",12,"bold"),text="Side Effects:",padx=1,pady=3)
        lblSideEffects.grid(row=8,column=0,sticky=W)
        txtSideEffects=Entry(DataFramerLeft,textvariable=self.sideeffects_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtSideEffects.grid(row=8,column=1)

        lblPrecWarning=Label(DataFramerLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=15)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFramerLeft,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFramerLeft,font=("arial",12,"bold"),text="Dosage:",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFramerLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFramerLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=15,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFramerLeft,textvariable=self.tabletprice_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFramerLeft,font=("arial",12,"bold"),text="Product QT:",padx=15,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFramerLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtProductQt.grid(row=3,column=3)



        #=================== ADD-BUTTONS ===============
        

        
        btnAddData = Button(ButtonFrame,command=self.Add_Data,text="Add-Medicine",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=0)

        btnAddData = Button(ButtonFrame,command=self.Update,text="Update",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData = Button(ButtonFrame,text="Delete",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=2)


        btnAddData = Button(ButtonFrame,text="Reset",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=3)

        btnAddData = Button(ButtonFrame,text="Exit",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=4)
        
       
        


        #================== DataFramerRight =========================
        lblrefno=Label(DataFramerRight,font=("arial",12,"bold"),text="Reference No:",padx=15,pady=6)
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFramerRight,textvariable=self.refmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtrefno.place(x=135,y=80)


        lblmedname=Label(DataFramerRight,font=("arial",12,"bold"),text="Medicine Name:",padx=15,pady=6)
        lblmedname.place(x=0,y=110)
        txtmedname=Entry(DataFramerRight,textvariable=self.addmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtmedname.place(x=140,y=110)
        

        side_frame = Frame(DataFramerRight,bd = 4,relief = RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=250,height = 160)
        
        sc_x = ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y = ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table = ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)
        #====================== Medicine Add  Buttons=========================
        down_frame = Frame(DataFramerRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=260,y=150,height=160)

        btnAddmed = Button(down_frame,command=self.AddMed,text="ADD",font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed = Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)


        btnDeletemed = Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)


        btnClearmed = Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)


        #========================= Frame Details =================================
        Framedeatils=Frame(self.root,bd=15,relief=RIDGE)
        Framedeatils.place(x=0,y=580,width=1350,height=180)


        Table_frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame.place(x=0,y=580,width=1350,height=130)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)



        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        self.pharmacy_table["show"]="headings"
        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Medicine Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Proc&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="ProductQts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="shravan123",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(ref,medname) values(%s,%s)",(self.refmed_var.get(),self.addmed_var.get()))

        conn.commit()
        
        self.fetch_dataMed()
        #self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine added")

    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="shravan123",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for row in rows:
                self.medicine_table.insert("",END,values=row)

            conn.commit()            
        conn.close()
        

    def Medget_cursor(self,event=""):

        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])    

    def UpdateMed(self):

        if self.refmed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="shravan123",database="dbms_project")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set medname=%s where ref=%s",(
                                                                            self.addmed_var.get(),
                                                                            self.refmed_var.get(),
                                                                        ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success","Data has been updated successfully")



    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="shravan123",database="dbms_project")
        my_cursor=conn.cursor()  

        sql="delete from pharma where ref=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit() 
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success","Medicine Deleted!")


    def ClearMed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")


    def Add_Data(self):

        if self.refno_var=="" or self.lotno_var=="":
            messagebox.showerror("Error","Fields are compulsory")

        else:

            conn=mysql.connector.connect(host="localhost",username="root",password="shravan123",database="dbms_project")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into medicine_detail(ref_no,cmp_name,med_type,med_name,lot_no,date_of_issue,date_of_exp,uses,side_effect,warning,dosage,price,product) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                        self.refno_var.get(),
                                                                        self.compname_var.get(),
                                                                        self.medicinetype_var.get(),
                                                                        self.medicinename_var.get(),
                                                                        self.lotno_var.get(),
                                                                        self.issuedate_var.get(),
                                                                        self.expdate_var.get(),
                                                                        self.uses_var.get(),
                                                                        self.sideeffects_var.get(),
                                                                        self.warning_var.get(),
                                                                        self.dosage_var.get(),
                                                                        self.tabletprice_var.get(),
                                                                        self.product_var.get(),
                                                                                         ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Data inserted successfully")

    def fatch_data(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="shravan123",database="dbms_project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from medicine_detail")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    def get_cursor(self,ev=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row=content["values"]


        self.refno_var.set(row[0]),
        self.compname_var.set(row[1]),
        self.medicinetype_var.set(row[2]),
        self.medicinename_var.set(row[3]),
        self.lotno_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideeffects_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.tabletprice_var.set(row[11]),
        self.product_var.set(row[12]),
 

    def Update(self):

        if self.refno_var.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='shravan123',database='dbms_project')
            my_cursor=conn.cursor()
            my_cursor.execute("update medicine_detail set cmp_name=%s,med_type=%s,med_name=%s,lot_no=%s,date_of_issue=%s,date_of_exp=%s,uses=%s,side_effect=%s,warning=%s,dosage=%s,price=%s,product=%s where ref_no=%s",(

                                                                        
                                                                        self.compname_var.get(),
                                                                        self.medicinetype_var.get(),
                                                                        self.medicinename_var.get(),
                                                                        self.lotno_var.get(),
                                                                        self.issuedate_var.get(),
                                                                        self.expdate_var.get(),
                                                                        self.uses_var.get(),
                                                                        self.sideeffects_var.get(),
                                                                        self.warning_var.get(),
                                                                        self.dosage_var.get(),
                                                                        self.tabletprice_var.get(),
                                                                        self.product_var.get(),
                                                                        self.refno_var.get()
            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("UPDATE","Record has been Updated Succussefully")



if __name__ == "__main__":
    root=Tk()
    obj=PMS(root)
    root.mainloop()
