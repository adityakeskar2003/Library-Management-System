from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import *
import datetime
import pymysql

class library:

    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1358x750+0+0")
        self.root.configure(bg = 'cadetblue')

        MType = StringVar()
        Member = StringVar()
        Title = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Address2 = StringVar()
        PostCode = StringVar()
        MobileNo = StringVar()
        BookISBN = StringVar()
        BookTitle = StringVar()
        BookType = StringVar()
        Author = StringVar()
        DateBorrowed = StringVar()
        DateDue = StringVar()
        SellingPrice = StringVar()
        LateReturnFine = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()


        MainFrame = Frame(self.root,bd = 10,bg = 'cadetblue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,bd = 10, width = 1350,padx = 60, relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width =31, font = ('arial',40,'bold'),text = "Library Management System")
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame,bd = 10,width= 1350,height=50,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame,bd=10,width=1300,height=50,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFTCover = LabelFrame(DataFrame,bd=0,width = 800,height=300,relief=RIDGE,
                                        bg = 'cadetblue',font = ('arial',12,'bold'),text = "Library Membership Info:")
        DataFrameLEFTCover.pack(side=LEFT,padx = 10)

        DataFrameLEFT = Frame(DataFrameLEFTCover,bd=10,width=800,height=300,pady=2,padx = 13,relief=RIDGE)
        DataFrameLEFT.pack(side=TOP)

        DataFrameLEFTb = LabelFrame(DataFrameLEFTCover,bd = 10,width= 800,height=100,pady=4,padx = 10, relief=RIDGE,
                                    font = ('arial',12,'bold'),text = 'Library Membership Info:')
        DataFrameLEFTb.pack(side=TOP)


        DataFrameRIGHT = LabelFrame(DataFrame,bd=10,width=450,height=300,padx = 10,relief=RIDGE,bg ='cadetblue',
                                    font = ('arial',12,'bold'),text = "Book Details:")
        DataFrameRIGHT.pack(side=RIGHT)


        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return 

        def iReset():
            MType.set("")
            Member.set("")
            Title.set("")
            FirstName.set("")
            Surname.set("")
            Address.set("")
            Address2.set("")
            PostCode.set("")
            MobileNo.set("")
            BookISBN.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")

        def addData():
            if(Member.get() == "" or FirstName.get() == "" or Surname.get() == ""):
                tkinter.messagebox.showerror("Library Management System","Enter correct members details")
            else:
                sqlCon = pymysql.connect(host="localhost",user="root",password="manasi@71", database="library")
                cur = sqlCon.cursor()
                cur.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                    Member.get(),
                    FirstName.get(),
                    Surname.get(),
                    Address.get(),
                    DateBorrowed.get(),
                    DateDue.get(),
                    DateOverDue.get(),
                    Author.get(),
                    BookISBN.get(),
                    BookTitle.get() 
                ))
                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                DateDue.set(cal.get_date())
                DateOverDue.set("Yes")
                tkinter.messagebox.showinfo("Library Management System","Record Entered Successfully")

        def DisplayData():
            sqlCon = pymysql.connect(host="localhost",user="root",password="manasi@71", database="library")
            cur = sqlCon.cursor()
            cur.execute("select * from library")
            result = cur.fetchall()
            if len(result)!=0:
                self.library_records.delete(*self.library_records.get_children())
                for row in result:
                    self.library_records.insert('',END,values=row)
                sqlCon.commit()
                sqlCon.close()

        def DeleteDB():
            sqlCon = pymysql.connect(host="localhost",user="root",password="manasi@71", database="library")
            cur = sqlCon.cursor()
            cur.execute("delete from library where member=%s", (Member.get(),))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Library Management System","Record Deleted Successfully")

        def SearchDB():
            try:
                sqlCon = pymysql.connect(host="localhost",user="root",password="manasi@71", database="library")
                cur = sqlCon.cursor()
                cur.execute("select * from library where member=%s", (Member.get(),))

                row = cur.fetchone()

                Member.set(row[0]),
                FirstName.set(row[1]),
                Surname.set(row[2]),
                Address.set(row[3]),
                DateBorrowed.set(row[4]),
                DateDue.set(row[5]),
                DateOverDue.set(row[6]),
                Author.set(row[7]),
                BookISBN.set(row[8]),
                BookTitle.set(row[9]),
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Library Management System","No such Record Found")
                sqlCon.close()

        def SelectedBook(evt):
            values = str(booklist.get(booklist.curselection()))
            w = values

            if(w == 'Cindrella'):
                BookISBN.set("ISBN 867849378993")
                BookTitle.set("God is King")
                Author.set("Paul Parker")
                LateReturnFine.set("200")
                SellingPrice.set("700")
                DaysOnLoan.set("30")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

        def LibraryInfo(ev,row):
            Member.set(row[0]),
            FirstName.set(row[1]),
            Surname.set(row[2]),
            Address.set(row[3]),
            DateBorrowed.set(row[4]),
            DateDue.set(row[5]),
            DateOverDue.set(row[6]),
            Author.set(row[7]),
            BookISBN.set(row[8]),
            BookTitle.set(row[9]),

        self.lblMemberType = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Member Type",padx = 2,pady = 2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)


        self.cboMemberType = ttk.Combobox(DataFrameLEFT,textvariable = MType , state='readonly',
                                          font = ('arial',12,'bold'), width = 34)
        self.cboMemberType['value'] = ('','Student','Lecturer','Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column = 1)


        self.lblBookISBN = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Book ID:",padx = 2,pady = 2)
        self.lblBookISBN.grid(row=0, column = 2,sticky = W)
        self.txtBookISBN = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=BookISBN,width=31)
        self.txtBookISBN.grid(row=0,column=3)

        self.lblMemberRef = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Member Ref No:",padx = 2,pady = 2)
        self.lblMemberRef.grid(row=1, column = 0,sticky = W)
        self.txtMemberRef = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=Member,width=36)
        self.txtMemberRef.grid(row=1,column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Book Title:",padx = 2,pady = 2)
        self.lblBookTitle.grid(row=1, column = 2,sticky = W)
        self.txtBookTitle = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=BookTitle,width=31)
        self.txtBookTitle.grid(row=1,column=3)

        self.lblTitle = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Title",padx = 2,pady = 2)
        self.lblTitle.grid(row=2,column=0,sticky=W)


        self.cboTitle = ttk.Combobox(DataFrameLEFT,textvariable = Title , state='readonly',
                                          font = ('arial',12,'bold'), width = 34)
        self.cboTitle['value'] = ('','Mr.','Mrs.','Miss.','Dr.','Capt.','Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column = 1)

        self.lblAuthor = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Author:",padx = 2,pady = 2)
        self.lblAuthor.grid(row=2, column = 2,sticky = W)
        self.txtAuthor = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=Author,width=31)
        self.txtAuthor.grid(row=2,column=3)

        self.lblFirstName = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "FirstName:",padx = 2,pady = 2)
        self.lblFirstName.grid(row=3, column = 0,sticky = W)
        self.txtFirstName = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=FirstName,width=36)
        self.txtFirstName.grid(row=3,column=1)

        self.lblDateBorrowed = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Date Borrowed:",padx = 2,pady = 2)
        self.lblDateBorrowed.grid(row=3, column = 2,sticky = W)
        self.txtDateBorrowed = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=DateBorrowed,width=31)
        self.txtDateBorrowed.grid(row=3,column=3)

        self.lblSurname = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Surname:",padx = 2,pady = 2)
        self.lblSurname.grid(row=4, column = 0,sticky = W)
        self.txtSurname = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=Surname,width=36)
        self.txtSurname.grid(row=4,column=1)

        self.lblDueDate = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Due Date:",padx = 2,pady = 2)
        self.lblDueDate.grid(row=4, column = 2,sticky = W)
        self.txtDueDate = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=DateDue,width=31)
        self.txtDueDate.grid(row=4,column=3)

        self.lblAddress1 = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Address1:",padx = 2,pady = 2)
        self.lblAddress1.grid(row=5, column = 0,sticky = W)
        self.txtAddress1 = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=Address,width=36)
        self.txtAddress1.grid(row=5,column=1)

        self.lblDaysOnLoan = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Days On Loan:",padx = 2,pady = 2)
        self.lblDaysOnLoan.grid(row=5, column = 2,sticky = W)
        self.txtDaysOnLoan = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=DaysOnLoan,width=31)
        self.txtDaysOnLoan.grid(row=5,column=3)

        self.lblAddress2 = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Address2:",padx = 2,pady = 2)
        self.lblAddress2.grid(row=6, column = 0,sticky = W)
        self.txtAddress2 = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=Address2,width=36)
        self.txtAddress2.grid(row=6,column=1)

        self.lblLateReturnFile = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Late Return Fine:",padx = 2,pady = 2)
        self.lblLateReturnFile.grid(row=6, column = 2,sticky = W)
        self.txtLateReturnFile = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=LateReturnFine,width=31)
        self.txtLateReturnFile.grid(row=6,column=3)

        self.lblPostCode = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Post Code:",padx = 2,pady = 2)
        self.lblPostCode.grid(row=7, column = 0,sticky = W)
        self.txtPostCode = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=PostCode,width=36)
        self.txtPostCode.grid(row=7,column=1)

        self.lblDateOverDue = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Date Over Due:",padx = 2,pady = 2)
        self.lblDateOverDue.grid(row=7, column = 2,sticky = W)
        self.txtDateOverDue = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=DateOverDue,width=31)
        self.txtDateOverDue.grid(row=7,column=3)

        self.lblMobileNumber = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Mobile No:",padx = 2,pady = 2)
        self.lblMobileNumber.grid(row=8, column = 0,sticky = W)
        self.txtMobileNumber = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=MobileNo,width=36)
        self.txtMobileNumber.grid(row=8,column=1)

        self.lblSellingPrice = Label(DataFrameLEFT, font = ('arial',12,'bold'),text = "Selling Price:",padx = 2,pady = 2)
        self.lblSellingPrice.grid(row=8, column = 2,sticky = W)
        self.txtSellingPrice = Entry(DataFrameLEFT, font = ('arial',12,'bold'),textvariable=SellingPrice,width=31)
        self.txtSellingPrice.grid(row=8,column=3)


        cal = Calendar(DataFrameRIGHT,selectmode = "day",year = 2020, month = 10,day =16, date_pattern = 'yyyy-mm-dd',
                       font = ('arial',12,'bold'),padx = 10)
        cal.grid(row = 0,column = 0,pady = 10)



        scroll_x=Scrollbar(DataFrameLEFTb,orient=HORIZONTAL)
        scroll_y=Scrollbar(DataFrameLEFTb,orient=VERTICAL)
        self.library_records = ttk.Treeview(DataFrameLEFTb,height=5,columns=("member","firstname","surname","address","databorrowed","datedue",
                                                                             "dayoverdue","author","bookisbn","booktitle"),xscrollcommand=scroll_x.set,
                                                                             yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side= RIGHT,fill=Y)

        self.library_records.heading("member",text = "Member")
        self.library_records.heading("firstname",text = "Firstname")
        self.library_records.heading("surname",text = "Surname")
        self.library_records.heading("address",text = "Address")
        self.library_records.heading("databorrowed",text = "Data Borrowed")
        self.library_records.heading("datedue", text="Date Due")
        self.library_records.heading("dayoverdue",text = "Days Over Due")
        self.library_records.heading("author",text = "Author")
        self.library_records.heading("bookisbn",text = "Book ISBN")
        self.library_records.heading("booktitle",text = "Book Title")


        self.library_records['show']='headings'

        self.library_records.column("member",width = 70)
        self.library_records.column("firstname",width = 100)
        self.library_records.column("surname",width = 100)
        self.library_records.column("address",width = 100)
        self.library_records.column("databorrowed",width = 70)
        self.library_records.column("datedue",width = 70)
        self.library_records.column("dayoverdue",width = 100)
        self.library_records.column("author",width = 100)
        self.library_records.column("bookisbn",width = 70)
        self.library_records.column("booktitle",width = 70)

        self.library_records.pack(fill = BOTH,expand = 1)
        self.library_records.bind('<ButtonRelease-1>',LibraryInfo)
        DisplayData()
        scrollbar = Scrollbar(DataFrameRIGHT,orient=VERTICAL)
        scrollbar.grid(row = 1,column = 1,sticky='ns')
        ListOfBooks=['Cindrella','Game Design','Ancient Rome','Made in Africa','Sleeping Beauty','London','Nigeria','Snow White','Shreik 3','London Streets',
                     'I Love Lagos','Love Kenya','Hello India']
        
        booklist = Listbox(DataFrameRIGHT,width=40,height=12,font = ('times',11,'bold'),  yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=1,column=0,padx= 3)
        scrollbar.config(command=booklist.yview)

        for items in ListOfBooks:
            booklist.insert(END,items)


        self.btnDisplayData = Button(ButtonFrame,text = "Display Data",font = ('arial',19,'bold'),
                                     padx = 4,width = 16,bd = 4,bg = 'cadetblue',command=addData)
        self.btnDisplayData.grid(row = 0, column = 0,padx = 3)

        self.btnDelete = Button(ButtonFrame,text = "Delete",font = ('arial',19,'bold'),
                                     padx = 4,width = 16,bd = 4,bg = 'cadetblue', command=DeleteDB)
        self.btnDelete.grid(row = 0, column = 1,padx = 3)

        self.btnReset = Button(ButtonFrame,text = "Reset",font = ('arial',19,'bold'),
                                     padx = 4,width = 16,bd = 4,bg = 'cadetblue', command=iReset)
        self.btnReset.grid(row = 0, column = 2,padx = 3)

        self.btnSearch = Button(ButtonFrame,text = "Search",font = ('arial',19,'bold'),
                                     padx = 4,width = 16,bd = 4,bg = 'cadetblue',command=SearchDB)
        self.btnSearch.grid(row = 0, column = 3,padx = 3)

        self.btnExit = Button(ButtonFrame,text = "Exit",font = ('arial',19,'bold'),
                                     padx = 4,width = 16,bd = 4,bg = 'cadetblue', command=iExit)
        self.btnExit.grid(row = 0, column = 4,padx = 3)





if __name__=='__main__':
    root = Tk()
    application = library(root)
    root.mainloop()


