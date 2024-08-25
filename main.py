import tkinter as tk
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
        self.root.state('zoomed')

        #configure the grid of the window
        self.root.grid_rowconfigure(0, weight=0) #Title
        self.root.grid_rowconfigure(1, weight=1) #Data Frame
        self.root.grid_rowconfigure(2, weight=1) #button Frame
        self.root.grid_rowconfigure(3, weight=4) #Detail Frame
        self.root.grid_columnconfigure(0, weight=1)

        labeltitle = Label(self.root,bd=20, relief= RIDGE, text= "Hospital Management System", fg="red", bg="white", font=("times new roman", 30, "bold"))
        labeltitle.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0,10))


        #====================DATA Frame=====================================
        DataFrame= Frame(self.root, bd =20, relief = RIDGE)
        DataFrame.grid(row =1, column=0, columnspan=4, sticky= "nsew", pady=(0,10))

        



        #------------------------------------Configure DataFrame grid rows and columns************************
        DataFrame.grid_rowconfigure(0, weight= 1)
        DataFrame.grid_columnconfigure(0, weight= 1)
        DataFrame.grid_columnconfigure(1, weight=1)


         #--------------------------------------------Making another frame inside the left side of the Data Frame***********************************************
        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx=20, relief = RIDGE,
                                                    font = ("arial", 10, "bold"), text = "Patient Information")
        DataFrameLeft.grid(row = 0, column=0, sticky = "nsew", padx=(0,10))


       
       
        #----------------------------------------------making another frame inside the Right side of the Data FRame**************************************************
        DataFrameRight = LabelFrame(DataFrame, bd=10, padx=20, relief = RIDGE,
                                                    font = ("times new roman", 10, "bold"), text = "Prescription")
        DataFrameRight.grid(row = 0, column=1, sticky="nsew", padx=(10,0))
        DataFrameRight.grid_rowconfigure(0, weight= 1)
        DataFrameRight.grid_columnconfigure(0, weight= 1)
        DataFrameRight.grid_columnconfigure(1, weight=0) #for scrollbar


        
        #---------------------------------------Configure DataFrameLeft grid*************************************
        for i in range(9):
            DataFrame.grid_rowconfigure(i, weight=1)
        
        for i in range(4):
            DataFrameLeft.grid_columnconfigure(i, weight=1)

        '''DataFrameLeft.grid_columnconfigure(0, weight = 1)
        DataFrameLeft.grid_columnconfigure(1, weight = 1)
        DataFrameLeft.grid_columnconfigure(2, weight = 1)
        DataFrameLeft.grid_columnconfigure(3, weight = 1)'''


        
        



        #==================================DataframeLeft==============================================================

        #-------------First Row---------------------
        lblNameTablet= Label(DataFrameLeft, text = "Names of Tablet", font = ("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0, sticky="w")

        comboNameTablet= ttk.Combobox(DataFrameLeft,font = ("times new roman",12,"bold"),
                                                                                           width= 33)
        comboNameTablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Aderall", "Amlodipine", "Ativan")
        comboNameTablet.grid(row=0, column=1, sticky="ew")

        lblInfo = Label(DataFrameLeft, text="Further Information", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblInfo.grid(row=0, column=2, sticky="w")

        entry_Info = ttk.Entry(DataFrameLeft, font =("arial",12), width =30)
        entry_Info.grid(row=0, column= 3, sticky="ew")

        #---------------Second Row--------------------------------------
        lblReference = Label(DataFrameLeft, text="Reference No", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblReference.grid(row=1, column=0, sticky="w")

        entry_Ref = ttk.Entry(DataFrameLeft, font =("arial",12), width =31)
        entry_Ref.grid(row=1, column= 1, sticky="ew")

        lblBlood = Label(DataFrameLeft, text="Blood Pressure", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblBlood.grid(row=1, column=2, sticky="w")

        entry_Blood = ttk.Entry(DataFrameLeft, font =("arial",12), width =30)
        entry_Blood.grid(row=1, column= 3, sticky="ew")

        
        #-----------------Thired Row---------------------------------------------
        lblDose = Label(DataFrameLeft, text="Dose", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDose.grid(row=2, column=0, sticky="w")

        entry_Dose = ttk.Entry(DataFrameLeft, font =("arial",12), width =31, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Dose.grid(row=2, column= 1, sticky="ew")

        lblStorage = Label(DataFrameLeft, text="Storage Advice", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblStorage.grid(row=2, column=2, sticky="w")

        entry_Storage = ttk.Entry(DataFrameLeft, font =("arial",12), width =30)
        entry_Storage.grid(row=2, column= 3, sticky="ew")

        
        #---------------Fourth Row--------------------------------------
        lblTabletsnum = Label(DataFrameLeft, text="No. of Tablets", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblTabletsnum.grid(row=3, column=0, sticky="w")

        entry_Tabletsnum = ttk.Entry(DataFrameLeft, font =("arial",12), width =31, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Tabletsnum.grid(row=3, column= 1, sticky="ew")

        lblMedication = Label(DataFrameLeft, text="Blood Pressure", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblMedication.grid(row=3, column=2, sticky="w")

        entry_Medication = ttk.Entry(DataFrameLeft, font =("arial",12), width =30)
        entry_Medication.grid(row=3, column= 3, sticky="ew")

         #---------------Fifth Row--------------------------------------
        lblLot = Label(DataFrameLeft, text="Lot", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblLot.grid(row=4, column=0, sticky="w")

        entry_Lot = ttk.Entry(DataFrameLeft, font =("arial",12), width =31, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Lot.grid(row=4, column= 1, sticky="ew")

        lblPatientId = Label(DataFrameLeft, text="Patient Id", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientId.grid(row=4, column=2, sticky="w")

        entry_PatientId = ttk.Entry(DataFrameLeft, font =("arial",12), width =30)
        entry_PatientId.grid(row=4, column= 3, sticky="ew")


         #---------------sixth Row--------------------------------------
        lblIssueDate = Label(DataFrameLeft, text="Issue Date", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblIssueDate.grid(row=5, column=0, sticky="w")

        entry_IssueDate = ttk.Entry(DataFrameLeft, font =("arial",12), width =31, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_IssueDate.grid(row=5, column= 1, sticky="ew")

        lblNhNum = Label(DataFrameLeft, text="NHS Number", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblNhNum.grid(row=5, column=2, sticky="w")

        entry_NhNum = ttk.Entry(DataFrameLeft, font =("arial",12), width =30)
        entry_NhNum.grid(row=5, column= 3, sticky="ew")

         #---------------Seventh Row--------------------------------------
        lblExpDate = Label(DataFrameLeft, text="Expairy Date", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblExpDate.grid(row=6, column=0, sticky="w")

        entry_ExpDate = ttk.Entry(DataFrameLeft, font =("arial",12), width =31, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_ExpDate.grid(row=6, column= 1, sticky="ew")

        lblPatientName = Label(DataFrameLeft, text="Patient Name", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientName.grid(row=6, column=2, sticky="w")

        entry_PatientName = ttk.Entry(DataFrameLeft, font =("arial",12), width =30)
        entry_PatientName.grid(row=6, column= 3, sticky="ew")

         #---------------Eigth Row--------------------------------------
        lblDailyDose = Label(DataFrameLeft, text="Daily Dose", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDailyDose.grid(row=7, column=0, sticky="w")

        entry_DailyDose = ttk.Entry(DataFrameLeft, font =("arial",12), width =31, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_DailyDose.grid(row=7, column= 1, sticky="ew")

        lblDOB = Label(DataFrameLeft, text="Date Of Birth", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDOB.grid(row=7, column=2, sticky="w")

        entry_DOB = ttk.Entry(DataFrameLeft, font =("arial",12), width =30, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_DOB.grid(row=7, column= 3, sticky="ew")

         #---------------Ninth Row--------------------------------------
        lblSideEffect = Label(DataFrameLeft, text="Side Effects", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblSideEffect.grid(row=8, column=0, sticky="w")

        entry_SideEffect = ttk.Entry(DataFrameLeft, font =("arial",12), width =31)
        entry_SideEffect.grid(row=8, column= 1, sticky="ew")

        lblPatientAddress = Label(DataFrameLeft, text="Patient Address", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientAddress.grid(row=8, column=2, sticky="w")

        entry_PatientAddress = ttk.Entry(DataFrameLeft, font =("arial",12), width =30)
        entry_PatientAddress.grid(row=8, column= 3, sticky="ew")

       
        
        
        #============================DataFrameRight============================================
        self.textPrescription = Text(DataFrameRight, font=("arial", 12,"bold"), width = 40, height= 0, padx=2, pady=6)
        self.textPrescription.grid(row=0, column=0, sticky= "nsew", padx=5, pady=5)
  
        
        #--------------------configure  DataFrameRight------------------------------------------
        DataFrameRight.grid_rowconfigure(0, weight =1)
        DataFrameRight.grid_columnconfigure(0, weight =1)



        #Adding scroll bar
        scrollbar_y= Scrollbar(DataFrameRight, orient= VERTICAL, command= self.textPrescription.yview)
        scrollbar_y.grid(row = 0, column =1, sticky= "ns")
        self.textPrescription.configure(yscrollcommand= scrollbar_y.set)






        #====================================== buttons frame ===============================================
        
        
        ButtonFrame= Frame(self.root, bd=20,  relief = RIDGE)
        ButtonFrame.grid(row = 2, column=0, columnspan=4, sticky="ew")

        #adding button
        Button(ButtonFrame, text = "Button 1").pack(side=LEFT, padx=5)
        Button(ButtonFrame, text = "Button 2").pack(side=LEFT, padx=5)



        #====================================== Details frame ===============================================
        
        
        DetailsFrame= Frame(self.root, bd=20,  relief = RIDGE)
        DetailsFrame.grid(row = 3, column=0, columnspan=4, sticky="nsew", padx=10, pady=(10,0))
        DetailsFrame.grid_columnconfigure(0, weight=1)
        DetailsFrame.grid_rowconfigure(0, weight=1)

        details_Label = Label(DetailsFrame, text="Details will be shown here")
        details_Label.grid(row=0, column=0, sticky="nsew")

        

        # Adjust the weight configuration to make sure DetailsFrame gets more space
        self.root.update_idletasks()  # Ensure layout updates are applied
        





root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
ob = Hospital(root)
root.mainloop()





