from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        labeltitle = Label(self.root,bd=20, relief= RIDGE, text= "Hospital Management System", fg="red", bg="white", font=("times new roman", 30, "bold"))
        labeltitle.pack(side=TOP,  fill=X)

        #====================DATA Frame=====================================
        DataFrame= Frame(self.root, bd =20, relief = RIDGE)
        DataFrame.place(x=0, y=100, width=1530, height =300)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx=20, relief = RIDGE,
                                                    font = ("arial", 10, "bold"), text = "Patient Information")
        DataFrameLeft.place(x=0,y=5,width=880,height=250)

        DataFrameRight = LabelFrame(DataFrame, bd=10, padx=20, relief = RIDGE,
                                                    font = ("times new roman", 10, "bold"), text = "Prescription")
        DataFrameRight.place(x=990,y=5,width=360,height=250)

        
        
        
        #====================================== buttons frame ===============================================
        
        
        ButtonFrame= Frame(self.root, bd=20,  relief = RIDGE)
        ButtonFrame.place(x=0, y=400,width=1530,height= 70)



 #====================================== Details frame ===============================================
        
        
        DetailsFrame= Frame(self.root, bd=20,  relief = RIDGE)
        DetailsFrame.place(x=0, y=470,width=1530,height= 200)


#==================================DataframeLeft==============================================================

        lblNameTablet= Label(DataFrameLeft, text = "Names of Tablet", font = ("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comboNameTablet= ttk.Combobox(DataFrameLeft,font = ("times new roman",12,"bold"),
                                                                                           width= 33)
        comboNameTablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Aderall", "Amlodipine", "Ativan")
        comboNameTablet.grid(row=0, column=1)


        



        




root = Tk()
ob = Hospital(root)
root.mainloop()





