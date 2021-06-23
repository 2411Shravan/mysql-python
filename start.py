from tkinter import *


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





if __name__ == "__main__":
    root=Tk()
    obj=PMS(root)
    root.mainloop()
