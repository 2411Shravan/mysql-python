from tkinter import *
from tkinter import ttk

class PMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1330x750+0+0")


        labeltitle=Label(self.root,text="Pharmacy Management System",bd=12,font=('times new roman',25),relief=RIDGE,bg='white'
                        ,fg='black',padx=1,pady=2)

        labeltitle.pack(side=TOP,fill=X)

        DataFrame = Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1320,height=400)

        DataFrameLeft = LabelFrame(DataFrame,bd=6,relief=RIDGE,padx=20,text="Medicine Info"
                        ,fg="darkgreen",font=500)

        DataFrameLeft.place(x=0,y=5,width=780,height=350)

        DataFrameRight = LabelFrame(DataFrame,bd=6,relief=RIDGE,padx=20,text="Add Medicines"
                        ,fg="darkgreen",font=500)

        DataFrameRight.place(x=800,y=5,width=450,height=350)


        ButtonFrame=Frame(self.root,bd=13,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1320,height=95)


        btnAddData = Button(ButtonFrame,text="Add-Medicine",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=0)

        btnAddData = Button(ButtonFrame,text="Update",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData = Button(ButtonFrame,text="Delete",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=2)


        btnAddData = Button(ButtonFrame,text="Reset",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=3)

        btnAddData = Button(ButtonFrame,text="Exit",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=4)

        btnExitMed = Button(ButtonFrame, text="EXIT", font=("arial",13,"bold"),width=14, bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)

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
        lblrefno=Label(DataFrameLeft, font=("arial",12,"bold"),text="Reference no", padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)


        ref_combo=ttk.Combobox(DataFrameLeft, width=15, font=("arial",14,"bold"),state="readonly")
        ref_combo["values"]=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        #===============Add Medicine===============
        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblDosage.grid(row=1,column=0,sticky=W)
        txtDosage=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtDosage.grid(row=1,column=1)



        lblrefno=Label(DataFrameLeft, font=("arial",12,"bold"),text="Type Of Medicine:", padx=2)
        lblrefno.grid(row=2,column=0,sticky=W)


        ref_combo=ttk.Combobox(DataFrameLeft, width=15, font=("arial",14,"bold"),state="readonly")
        ref_combo["values"]=("Tablet","Liquid","Drops","Injection","Capsule","Inhales")
        ref_combo.grid(row=2,column=1)
        ref_combo.current(0)


        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",14,"bold"),width=15)
        comMedicineName['value']=("nice","novel")
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)


        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:",padx=1,pady=3)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=1,pady=3)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=1,pady=3)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=1,pady=2)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtUses.grid(row=7,column=1)

        lblSideEffects=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects:",padx=1,pady=3)
        lblSideEffects.grid(row=8,column=0,sticky=W)
        txtSideEffects=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtSideEffects.grid(row=8,column=1)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=15)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=15,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=15,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtProductQt.grid(row=3,column=3)



        #=================== Images ===============
        

        

        
       
        


        #================== dataframeRight =========================
        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No:",padx=15,pady=6)
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFrameRight,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtrefno.place(x=135,y=80)


        lblmedname=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",padx=15,pady=6)
        lblmedname.place(x=0,y=110)
        txtmedname=Entry(DataFrameRight,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtmedname.place(x=140,y=110)
        


                       

        

        

if __name__ == "__main__":
    root=Tk()
    obj=PMS(root)
    root.mainloop()
