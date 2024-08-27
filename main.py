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
        self.root.geometry("1600x900+0+0")
        self.root.resizable(TRUE, TRUE)
        #self.root.state('zoomed')

        #configure the grid of the window
        self.root.grid_rowconfigure(0, weight=0) #Title
        self.root.grid_rowconfigure(1, weight=3) #Data Frame
        self.root.grid_rowconfigure(2, weight=1) #button Frame
        self.root.grid_rowconfigure(3, weight=2) #Detail Frame
        self.root.grid_columnconfigure(0, weight=1)

        labeltitle = Label(self.root,bd=20, relief= RIDGE, text= "Hospital Management System", fg="red", bg="white", font=("times new roman", 30, "bold"))
        labeltitle.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0,10))


        #====================DATA Frame=====================================
        DataFrame= Frame(self.root, bd =20, relief = RIDGE)
        DataFrame.grid(row =1, column=0, columnspan=4, sticky= "nsew", pady=(0,10))

        



        #------------------------------------Configure DataFrame grid rows and columns************************
        DataFrame.grid_rowconfigure(0, weight= 1)
        DataFrame.grid_columnconfigure(0, weight= 2)
        DataFrame.grid_columnconfigure(1, weight=1)


         #--------------------------------------------Making another frame inside the left side of the Data Frame***********************************************
        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx=20, relief = RIDGE,
                                                    font = ("arial", 10, "bold"), text = "Patient Information")
        DataFrameLeft.grid(row = 0, column=0, sticky = "nsew", padx=(0,10))


          
        #***********************************Configure DataFrameLeft grid*************************************
        for i in range(9):
            DataFrameLeft.grid_rowconfigure(i, weight=1)
        
        for i in range(4):
            DataFrameLeft.grid_columnconfigure(i, weight=1)

        
        
        '''DataFrameLeft.grid_columnconfigure(0, weight = 1)
        DataFrameLeft.grid_columnconfigure(1, weight = 1)
        DataFrameLeft.grid_columnconfigure(2, weight = 1)
        DataFrameLeft.grid_columnconfigure(3, weight = 1)'''




       
       
        #----------------------------------------------making another frame inside the Right side of the Data FRame**************************************************
        DataFrameRight = LabelFrame(DataFrame, bd=10, padx=20, relief = RIDGE,
                                                    font = ("times new roman", 10, "bold"), text = "Prescription")
        DataFrameRight.grid(row = 0, column=1, sticky="nsew", padx=(10,0))
        DataFrameRight.grid_rowconfigure(0, weight= 1)
        DataFrameRight.grid_columnconfigure(0, weight= 1)
        DataFrameRight.grid_columnconfigure(1, weight=0) #for scrollbar


        
        



        #==================================DataframeLeft==============================================================

        #-------------First Row---------------------
        lblNameTablet= Label(DataFrameLeft, text = "Names of Tablet", font = ("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0, sticky="w")

        comboNameTablet= ttk.Combobox(DataFrameLeft,font = ("times new roman",12,"bold"),
                                                                                           width= 23)
        comboNameTablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Aderall", "Amlodipine", "Ativan")
        comboNameTablet.grid(row=0, column=1, sticky="ew")

        lblInfo = Label(DataFrameLeft, text="Further Information", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblInfo.grid(row=0, column=2, sticky="w")

        entry_Info = ttk.Entry(DataFrameLeft, font =("arial",12), width =20)
        entry_Info.grid(row=0, column= 3, sticky="ew")

        #---------------Second Row--------------------------------------
        lblReference = Label(DataFrameLeft, text="Reference No", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblReference.grid(row=1, column=0, sticky="w")

        entry_Ref = ttk.Entry(DataFrameLeft, font =("arial",12), width =21)
        entry_Ref.grid(row=1, column= 1, sticky="ew")

        lblBlood = Label(DataFrameLeft, text="Blood Pressure", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblBlood.grid(row=1, column=2, sticky="w")

        entry_Blood = ttk.Entry(DataFrameLeft, font =("arial",12), width =20)
        entry_Blood.grid(row=1, column= 3, sticky="ew")

        
        #-----------------Thired Row---------------------------------------------
        lblDose = Label(DataFrameLeft, text="Dose", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDose.grid(row=2, column=0, sticky="w")

        entry_Dose = ttk.Entry(DataFrameLeft, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Dose.grid(row=2, column= 1, sticky="ew")

        lblStorage = Label(DataFrameLeft, text="Storage Advice", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblStorage.grid(row=2, column=2, sticky="w")

        entry_Storage = ttk.Entry(DataFrameLeft, font =("arial",12), width =20)
        entry_Storage.grid(row=2, column= 3, sticky="ew")

        
        #---------------Fourth Row--------------------------------------
        lblTabletsnum = Label(DataFrameLeft, text="No. of Tablets", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblTabletsnum.grid(row=3, column=0, sticky="w")

        entry_Tabletsnum = ttk.Entry(DataFrameLeft, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Tabletsnum.grid(row=3, column= 1, sticky="ew")

        lblMedication = Label(DataFrameLeft, text="Blood Pressure", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblMedication.grid(row=3, column=2, sticky="w")

        entry_Medication = ttk.Entry(DataFrameLeft, font =("arial",12), width =20)
        entry_Medication.grid(row=3, column= 3, sticky="ew")

         #---------------Fifth Row--------------------------------------
        lblLot = Label(DataFrameLeft, text="Lot", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblLot.grid(row=4, column=0, sticky="w")

        entry_Lot = ttk.Entry(DataFrameLeft, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Lot.grid(row=4, column= 1, sticky="ew")

        lblPatientId = Label(DataFrameLeft, text="Patient Id", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientId.grid(row=4, column=2, sticky="w")

        entry_PatientId = ttk.Entry(DataFrameLeft, font =("arial",12), width =20)
        entry_PatientId.grid(row=4, column= 3, sticky="ew")


         #---------------sixth Row--------------------------------------
        lblIssueDate = Label(DataFrameLeft, text="Issue Date", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblIssueDate.grid(row=5, column=0, sticky="w")

        entry_IssueDate = ttk.Entry(DataFrameLeft, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_IssueDate.grid(row=5, column= 1, sticky="ew")

        lblNhNum = Label(DataFrameLeft, text="NHS Number", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblNhNum.grid(row=5, column=2, sticky="w")

        entry_NhNum = ttk.Entry(DataFrameLeft, font =("arial",12), width =20)
        entry_NhNum.grid(row=5, column= 3, sticky="ew")

         #---------------Seventh Row--------------------------------------
        lblExpDate = Label(DataFrameLeft, text="Expairy Date", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblExpDate.grid(row=6, column=0, sticky="w")

        entry_ExpDate = ttk.Entry(DataFrameLeft, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_ExpDate.grid(row=6, column= 1, sticky="ew")

        lblPatientName = Label(DataFrameLeft, text="Patient Name", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientName.grid(row=6, column=2, sticky="w")

        entry_PatientName = ttk.Entry(DataFrameLeft, font =("arial",12), width =20)
        entry_PatientName.grid(row=6, column= 3, sticky="ew")

         #---------------Eigth Row--------------------------------------
        lblDailyDose = Label(DataFrameLeft, text="Daily Dose", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDailyDose.grid(row=7, column=0, sticky="w")

        entry_DailyDose = ttk.Entry(DataFrameLeft, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_DailyDose.grid(row=7, column= 1, sticky="ew")

        lblDOB = Label(DataFrameLeft, text="Date Of Birth", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDOB.grid(row=7, column=2, sticky="w")

        entry_DOB = ttk.Entry(DataFrameLeft, font =("arial",12), width =20, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_DOB.grid(row=7, column= 3, sticky="ew")

         #---------------Ninth Row--------------------------------------
        lblSideEffect = Label(DataFrameLeft, text="Side Effects", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblSideEffect.grid(row=8, column=0, sticky="w")

        entry_SideEffect = ttk.Entry(DataFrameLeft, font =("arial",12), width =21)
        entry_SideEffect.grid(row=8, column= 1, sticky="ew")

        lblPatientAddress = Label(DataFrameLeft, text="Patient Address", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientAddress.grid(row=8, column=2, sticky="w")

        entry_PatientAddress = ttk.Entry(DataFrameLeft, font =("arial",12), width =20)
        entry_PatientAddress.grid(row=8, column= 3, sticky="ew")

       



      
        # Adjust the layout of elements in DataFrameLeft
        elements = [
        (lblNameTablet, comboNameTablet, lblInfo, entry_Info),
        (lblReference, entry_Ref, lblBlood, entry_Blood),
        (lblDose, entry_Dose, lblStorage, entry_Storage),
        (lblTabletsnum, entry_Tabletsnum, lblMedication, entry_Medication),
        (lblLot, entry_Lot, lblPatientId, entry_PatientId),
        (lblIssueDate, entry_IssueDate, lblNhNum, entry_NhNum),
        (lblExpDate, entry_ExpDate, lblPatientName, entry_PatientName),
        (lblDailyDose, entry_DailyDose, lblDOB, entry_DOB),
        (lblSideEffect, entry_SideEffect, lblPatientAddress, entry_PatientAddress)
]

        for i, (lbl1, widget1, lbl2, widget2) in enumerate(elements):
            lbl1.grid(row=i, column=0, sticky="w", padx=2, pady=2)
            widget1.grid(row=i, column=1, sticky="ew", padx=2, pady=2)
            lbl2.grid(row=i, column=2, sticky="w", padx=2, pady=2)
            widget2.grid(row=i, column=3, sticky="ew", padx=2, pady=2)

        
        
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
        
        
        ButtonFrame= LabelFrame(self.root, bd=20,  relief = RIDGE, text = "Actions", font=("arial", 12, "bold"))
        ButtonFrame.grid(row = 2, column=0, columnspan=4, sticky="ew", padx=10, pady=(10,0))

        
        
        #                               Adding buttons with in the boarder label frame
        
        btnPrescription = Button(ButtonFrame, text = "Prescription", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnPrescription.grid(row =0, column=0, padx=5, pady=5, sticky="nsew")
        
        btnPrescriptionData = Button(ButtonFrame, text = "Prescription Data", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnPrescriptionData.grid(row =0, column=1, padx=5, pady=5,  sticky="nsew")

        btnUpdate = Button(ButtonFrame, text = "Update", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnUpdate.grid(row =0, column=2, padx=5, pady=5,  sticky="nsew")

        btnDelete = Button(ButtonFrame, text = "Delete", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnDelete.grid(row =0, column=3, padx=5, pady=5,  sticky="nsew")

        btnClear = Button(ButtonFrame, text = "Clear", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnClear.grid(row =0, column=4, padx=5, pady=5,  sticky="nsew")

        btnExit = Button(ButtonFrame, text = "Exit", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnExit.grid(row =0, column=5, padx=5, pady=5,  sticky="nsew")



        #====================================== Details frame ===============================================
        
        
        DetailsFrame= Frame(self.root, bd=20,  relief = RIDGE)
        DetailsFrame.grid(row = 3, column=0, columnspan=4, sticky="nsew", padx=10, pady=(10,0))
        DetailsFrame.grid_columnconfigure(0, weight=1)
        DetailsFrame.grid_rowconfigure(0, weight=1)

        details_Label = Label(DetailsFrame, text="Details will be shown here")
        details_Label.grid(row=0, column=0, sticky="nsew")

        #=======================================Table==================================
        #=======================Scrollbar===========================

        #             Creating Treeview Widget
        self.hospital_table= ttk.Treeview(DetailsFrame, column=("Name of Tablets", "Reference Number", "Dose", "No. of Tablets",
                                                                "Lot", "Issue Date", "Expairy Date", "Daily Dose", "Storage", "NHS Number",
                                                                   "Patient Name", "Address", "DOB"))
        
        # Creating Scroll Bars
        scrollInDetails_x = ttk.Scrollbar(DetailsFrame, orient = HORIZONTAL, command= self.hospital_table.xview)
        scrollInDetails_y = ttk.Scrollbar(DetailsFrame, orient = VERTICAL, command= self.hospital_table.yview)
        
        # Configuring the Treeview widget to use the scrollbars
        self.hospital_table.configure(xscrollcommand= scrollInDetails_x.set, yscrollcommand=scrollInDetails_y.set)


        #gird scroll bars in correct positions
        scrollInDetails_x.grid(row=1, column=0, sticky="ew")
        scrollInDetails_y.grid(row=0, column=1, sticky="ns")



        #configure the Treeview columns and headings
        self.hospital_table.heading("Name of Tablets", text="Name Of Tablets")
        self.hospital_table.heading("Reference Number", text="Reference Number")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("No. of Tablets", text= "NO. OF Tablets ")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("Daily Dose", text="Daily Dose")
        self.hospital_table.heading("Issue Date", text="Issue Date")
        self.hospital_table.heading("Expairy Date", text="Expairy Date")
        self.hospital_table.heading("Storage", text="Storage")
        self.hospital_table.heading("NHS Number", text= "NHS Number")
        self.hospital_table.heading("Patient Name", text="Patient Name")
        self.hospital_table.heading("Address", text= "Address")
        self.hospital_table.heading("DOB", text="DOB")

        self.hospital_table["show"] =  "headings"

        #Grid the Treeview widget
        self.hospital_table.grid(row=0, column=0, sticky="nsew")

        #set the width of each column
        columns=["Name of Tablets", "Reference Number", "Dose", "No. of Tablets",
                "Lot", "Issue Date", "Expairy Date", "Daily Dose", "Storage",
                 "NHS Number", "Patient Name", "Address", "DOB"]
        
        for column in columns:
            self.hospital_table.column(column, width=100)


        

        

        # Adjust the weight configuration to make sure DetailsFrame gets more space
        self.root.update_idletasks()  # Ensure layout updates are applied
        





root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
ob = Hospital(root)
root.mainloop()





