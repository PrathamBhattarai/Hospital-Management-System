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

        
        self.Nameoftablets = StringVar()
        self.Reference = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()
        
        
        
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

        comboNameTablet= ttk.Combobox(DataFrameLeft,textvariable =self.Nameoftablets ,font = ("times new roman",12,"bold"), state= "readonltextvariable =self.,y",
                                                                                           width= 23)
        comboNameTablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Aderall", "Amlodipine", "Ativan")
        comboNameTablet.current(0)
        comboNameTablet.grid(row=0, column=1, sticky="ew")

        lblInfo = Label(DataFrameLeft, text="Further Information", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblInfo.grid(row=0, column=2, sticky="w")

        entry_Info = ttk.Entry(DataFrameLeft,textvariable =self.FurtherInformation , font =("arial",12), width =20)
        entry_Info.grid(row=0, column= 3, sticky="ew")

        #---------------Second Row--------------------------------------
        lblReference = Label(DataFrameLeft, text="Reference No", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblReference.grid(row=1, column=0, sticky="w")

        entry_Ref = ttk.Entry(DataFrameLeft,textvariable =self.Reference, font =("arial",12), width =21)
        entry_Ref.grid(row=1, column= 1, sticky="ew")

        lblDrivingMachine = Label(DataFrameLeft, text="Blood Pressure", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDrivingMachine.grid(row=1, column=2, sticky="w")

        entry_DrivingMachine = ttk.Entry(DataFrameLeft,textvariable =self.DrivingUsingMachine, font =("arial",12), width =20)
        entry_DrivingMachine.grid(row=1, column= 3, sticky="ew")

        
        #-----------------Thired Row---------------------------------------------
        lblDose = Label(DataFrameLeft, text="Dose", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDose.grid(row=2, column=0, sticky="w")

        entry_Dose = ttk.Entry(DataFrameLeft,textvariable =self.Dose, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Dose.grid(row=2, column= 1, sticky="ew")

        lblStorage = Label(DataFrameLeft, text="Storage Advice", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblStorage.grid(row=2, column=2, sticky="w")

        entry_Storage = ttk.Entry(DataFrameLeft,textvariable =self.StorageAdvice, font =("arial",12), width =20)
        entry_Storage.grid(row=2, column= 3, sticky="ew")

        
        #---------------Fourth Row--------------------------------------
        lblTabletsnum = Label(DataFrameLeft, text="No. of Tablets", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblTabletsnum.grid(row=3, column=0, sticky="w")

        entry_Tabletsnum = ttk.Entry(DataFrameLeft,textvariable =self.NumberofTablets, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Tabletsnum.grid(row=3, column= 1, sticky="ew")

        lblMedication = Label(DataFrameLeft, text="Medication", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblMedication.grid(row=3, column=2, sticky="w")

        entry_Medication = ttk.Entry(DataFrameLeft,textvariable =self.HowToUseMedication, font =("arial",12), width =20)
        entry_Medication.grid(row=3, column= 3, sticky="ew")

         #---------------Fifth Row--------------------------------------
        lblLot = Label(DataFrameLeft, text="Lot", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblLot.grid(row=4, column=0, sticky="w")

        entry_Lot = ttk.Entry(DataFrameLeft,textvariable =self.Lot, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_Lot.grid(row=4, column= 1, sticky="ew")

        lblPatientId = Label(DataFrameLeft, text="Patient Id", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientId.grid(row=4, column=2, sticky="w")

        entry_PatientId = ttk.Entry(DataFrameLeft,textvariable =self.PatientId, font =("arial",12), width =20)
        entry_PatientId.grid(row=4, column= 3, sticky="ew")


         #---------------sixth Row--------------------------------------
        lblIssueDate = Label(DataFrameLeft, text="Issue Date", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblIssueDate.grid(row=5, column=0, sticky="w")

        entry_IssueDate = ttk.Entry(DataFrameLeft,textvariable =self.IssueDate, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_IssueDate.grid(row=5, column= 1, sticky="ew")

        lblNhNum = Label(DataFrameLeft, text="NHS Number", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblNhNum.grid(row=5, column=2, sticky="w")

        entry_NhNum = ttk.Entry(DataFrameLeft,textvariable =self.nhsNumber, font =("arial",12), width =20)
        entry_NhNum.grid(row=5, column= 3, sticky="ew")

         #---------------Seventh Row--------------------------------------
        lblExpDate = Label(DataFrameLeft, text="Expairy Date", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblExpDate.grid(row=6, column=0, sticky="w")

        entry_ExpDate = ttk.Entry(DataFrameLeft,textvariable =self.ExpDate, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_ExpDate.grid(row=6, column= 1, sticky="ew")

        lblPatientName = Label(DataFrameLeft, text="Patient Name", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientName.grid(row=6, column=2, sticky="w")

        entry_PatientName = ttk.Entry(DataFrameLeft,textvariable =self.PatientName, font =("arial",12), width =20)
        entry_PatientName.grid(row=6, column= 3, sticky="ew")

         #---------------Eigth Row--------------------------------------
        lblDailyDose = Label(DataFrameLeft, text="Daily Dose", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDailyDose.grid(row=7, column=0, sticky="w")

        entry_DailyDose = ttk.Entry(DataFrameLeft,textvariable =self.DailyDose, font =("arial",12), width =21, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_DailyDose.grid(row=7, column= 1, sticky="ew")

        lblDOB = Label(DataFrameLeft, text="Date Of Birth", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblDOB.grid(row=7, column=2, sticky="w")

        entry_DOB = ttk.Entry(DataFrameLeft,textvariable =self.DateOfBirth, font =("arial",12), width =20, validate="key", validatecommand=(DataFrameLeft.register(lambda P: P.isdigit()or P ==""), '%P'))
        entry_DOB.grid(row=7, column= 3, sticky="ew")

         #---------------Ninth Row--------------------------------------
        lblSideEffect = Label(DataFrameLeft, text="Side Effects", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblSideEffect.grid(row=8, column=0, sticky="w")

        entry_SideEffect = ttk.Entry(DataFrameLeft,textvariable =self.SideEffect, font =("arial",12), width =21)
        entry_SideEffect.grid(row=8, column= 1, sticky="ew")

        lblPatientAddress = Label(DataFrameLeft, text="Patient Address", font=("times new roman", 12, "bold"), padx=2 , pady= 6)
        lblPatientAddress.grid(row=8, column=2, sticky="w")

        entry_PatientAddress = ttk.Entry(DataFrameLeft,textvariable =self.PatientAddress, font =("arial",12), width =20)
        entry_PatientAddress.grid(row=8, column= 3, sticky="ew")

       



      
        # Adjust the layout of elements in DataFrameLeft
        elements = [
        (lblNameTablet, comboNameTablet, lblInfo, entry_Info),
        (lblReference, entry_Ref, lblDrivingMachine, entry_DrivingMachine),
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
        btnPrescription.grid(row =0, column=0, padx=5, pady=1, sticky="nsew")
        
        btnPrescriptionData = Button(ButtonFrame,command=self.iPrescriptionData , text = "Prescription Data", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnPrescriptionData.grid(row =0, column=1, padx=5, pady=1,  sticky="nsew")

        btnUpdate = Button(ButtonFrame, text = "Update", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnUpdate.grid(row =0, column=2, padx=5, pady=1,  sticky="nsew")

        btnDelete = Button(ButtonFrame, text = "Delete", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnDelete.grid(row =0, column=3, padx=5, pady=1,  sticky="nsew")

        btnClear = Button(ButtonFrame, text = "Clear", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnClear.grid(row =0, column=4, padx=5, pady=1,  sticky="nsew")

        btnExit = Button(ButtonFrame, text = "Exit", bg = 'green', fg='white', font=("arial", 12,"bold"), width = 20, height= 0, padx=2, pady=6)
        btnExit.grid(row =0, column=5, padx=5, pady=1,  sticky="nsew")



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
                                                                "Lot", "Issue Date", "Expairy Date", "Daily Dose","Side Effect",
                                                                "Further Information", "Storage Advice", "Driving Using Machine",
                                                                "Medication","Patient Id","NHS Number", "Patient Name", 
                                                                "Date Of Birth", "Patient Address"))
        
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
        self.hospital_table.heading("Issue Date", text="Issue Date")
        self.hospital_table.heading("Expairy Date", text="Expairy Date")
        self.hospital_table.heading("Daily Dose", text="Daily Dose")
        self.hospital_table.heading("Side Effect", text="Side Effect")
        self.hospital_table.heading("Further Information", text="Further Information")
        self.hospital_table.heading("Storage Advice", text="Storage Advice")
        self.hospital_table.heading("Driving Using Machine", text="Driving Using Machine")
        self.hospital_table.heading("Medication", text="Medication")
        self.hospital_table.heading("Patient Id", text="Patient Id")
        self.hospital_table.heading("NHS Number", text= "NHS Number")
        self.hospital_table.heading("Patient Name", text="Patient Name")
        self.hospital_table.heading("Date Of Birth", text= "Date Of Birth")
        self.hospital_table.heading("Patient Address", text="Patient Address")

        self.hospital_table["show"] =  "headings"

        #Grid the Treeview widget
        self.hospital_table.grid(row=0, column=0, sticky="nsew")
        self.fatch_data()
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        #set the width of each column
        columns=["Name of Tablets", "Reference Number", "Dose", "No. of Tablets",
                "Lot", "Issue Date", "Expairy Date", "Daily Dose","Side Effect",
                "Further Information", "Storage Advice", "Driving Using Machine",
                "Medication","Patient Id","NHS Number", "Patient Name", 
                "Date Of Birth", "Patient Address"]
        
        for column in columns:
            self.hospital_table.column(column, width=100)



    #======================Functionality Declaration====================================
    def iPrescriptionData(self):
    # Check if required fields are empty before inserting into the database
        if self.Nameoftablets.get() == "" or self.Reference.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return  # Stop further execution if validation fails

        try:
        # Establish connection with MySQL
            conn = mysql.connector.connect(
                host="127.0.0.1",  # Make sure this matches your server setup
                user="root",       # Default MySQL username
                password="@Pp9842030782",       # Use your actual MySQL password if set
                database="mydata"  # Ensure this database exists
            )
            print("Connected to database successfully")  # Confirmation message

            my_cursor = conn.cursor()

        # Insert data into the hospital table
            my_cursor.execute(
                "INSERT INTO hospital (NameOfTablets, Reference, Dose, NumberOfTablets, Lot, IssueDate, ExpDate, DailyDose, SideEffect, FurtherInformation, StorageAdvice, DrivingUsingMachine, HowToUseMedication, PatientId, nhsNumber, PatientName, DateOfBirth, PatientAddress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.Nameoftablets.get(),
                    self.Reference.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.SideEffect.get(),
                    self.FurtherInformation.get(),
                    self.StorageAdvice.get(),
                    self.DrivingUsingMachine.get(),
                    self.HowToUseMedication.get(),
                    self.PatientId.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                )   
        )

        # Commit the changes and show a success message
            conn.commit()
            self.fatch_data()
            messagebox.showinfo("Success", "Data has been inserted successfully.")
        
        except mysql.connector.Error as e:
            # Show the error message if something goes wrong
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            print(f"Error: {e}")

        finally:
        # Ensure the connection is closed properly
            if conn.is_connected():
                conn.close()
                print("Database connection closed")
        



    def fatch_data(self):
            conn = mysql.connector.connect(host="127.0.0.1", user="root", password="@Pp9842030782", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from hospital")
            rows = my_cursor.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("", END, values = i)
                conn.commit()
            conn.close()

             
            

        
    def get_cursor(self,event = "" ):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0]),
        self.Dose.set(row[1]),
        self.Reference.set(row[2]),
        self.NumberofTablets.set(row[3]),
        self.Lot.set(row[4]),
        self.IssueDate.set(row[5]),
        self.ExpDate.set(row[6]),
        self.DailyDose.set(row[7]),
        #self.SideEffect.set(row[8]),
        #self.FurtherInformation.set(row[9]),
        self.StorageAdvice.set(row[8]),
        #self.DrivingUsingMachine.set(row[11]),
       # self.HowToUseMedication.set(row[12]),
        #self.PatientId.set(row[]),
        self.nhsNumber.set(row[14]),
        self.PatientName.set(row[15]),
        self.DateOfBirth.set(row[16]),
        self.PatientAddress.set(row[17])

        
        
        
        
        
        # Adjust the weight configuration to make sure DetailsFrame gets more space
        self.root.update_idletasks()  # Ensure layout updates are applied
        





root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
ob = Hospital(root)
root.mainloop()





