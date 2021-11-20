from tkinter import *
from tkinter import messagebox
import mysql.connector
import sqlite3
import Signup2

f = ('Times', 14)

con = sqlite3.connect('bms_py.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS signup2(
                    religion text,
                    category text,
                    income text,
                    education text,
                    occupation text,
                    pan text,
                    aadhar text,
                    scitizen text,
                    eaccount text 
                )
            ''')
con.commit()


ws = Tk()
ws.title('iBanking')
ws.geometry('950x700')
ws.config(bg='#0B5A81')


def insert_record():
    check_counter = 0
    warn = ""
    if register_religion.get() == "":
       warn = "Religion can't be empty"
    else:
        check_counter += 1

    if register_category.get() == "":
        warn = "Category can't be empty"
    else:
        check_counter += 1

    if register_income.get() == "":
       warn = "Income can't be empty"
    else:
        check_counter += 1

    if register_education.get() == "":
        warn = "Education can't be empty"
    else:
        check_counter += 1

    if register_occupation.get() == "":
        warn = "Occupation can't be empty"
    else:
        check_counter += 1

    if register_pan.get() == "":
        warn = "PAN Number can't be empty"
    else:
        check_counter += 1

    if register_aadhar.get() == "":
        warn = "Aadhar Number can't be empty"
    else:
        check_counter += 1

    if scitizen.get() == "":
        warn = "Select Senior Citizen"
    else:
        check_counter += 1

    if eaccount.get() == "":
        warn = "Select Existing Account"
    else:
        check_counter += 1


    if check_counter == 9:
        try:
            con = sqlite3.connect('bms_py.db')
            cur = con.cursor()
            cur.execute("INSERT INTO signup2 VALUES (:religion, :category, :income, :education, :occupation, :pan, :aadhar, :scitizen, :eaccount)", {
                'religion': register_religion.get(),
                'category': register_category.get(),
                'income': register_income.get(),
                'education': register_education.get(),
                'occupation': register_occupation.get(),
                'pan': register_pan.get(),
                'aadhar': register_aadhar.get(),
                'scitizen': scitizen.get(),
                'eaccount': eaccount.get()

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')
            ws.destroy()
            import Signup3
            

        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)


scitizen = StringVar()
scitizen.set('No')

eaccount = StringVar()
eaccount.set('No')


right_frame = Frame(
    ws,
    #text="Personal Details",
    bd=3,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)
label1 = Label(ws, text="Additionals Details", font=f)

label1.pack()


Label(
    right_frame,
    text="Enter Religion",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Category",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Income",
    bg='#CCCCCC',
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Education Qualifications",
    bg='#CCCCCC',
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Occupation",
    bg='#CCCCCC',
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter PAN Number",
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Aadhar Number",
    bg='#CCCCCC',
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select Senior Citizen",
    bg='#CCCCCC',
    font=f
).grid(row=7, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select Existing Account",
    bg='#CCCCCC',
    font=f
).grid(row=8, column=0, sticky=W, pady=10)


scitizen_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

eaccount_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

register_religion = Entry(
    right_frame,
    font=f
)

register_category = Entry(
    right_frame,
    font=f
)

register_income = Entry(
    right_frame,
    font=f
)


register_education = Entry(
    right_frame,
    font=f,
)

register_occupation = Entry(
    right_frame,
    font=f,
)

register_pan = Entry(
    right_frame,
    font=f,
)

register_aadhar = Entry(
    right_frame,
    font=f,
)


scitizen_yes_rb = Radiobutton(
    scitizen_frame,
    text='Yes',
    bg='#CCCCCC',
    variable=scitizen,
    value='Yes',
    font=('Times', 10),

)

scitizen_no_rb = Radiobutton(
    scitizen_frame,
    text='No',
    bg='#CCCCCC',
    variable=scitizen,
    value='No',
    font=('Times', 10),

)

eaccount_yes_rb = Radiobutton(
    eaccount_frame,
    text='Yes',
    bg='#CCCCCC',
    variable=eaccount,
    value='Yes',
    font=('Times', 10),

)

eaccount_no_rb = Radiobutton(
    eaccount_frame,
    text='No',
    bg='#CCCCCC',
    variable=eaccount,
    value='No',
    font=('Times', 10),

)


next_btn = Button(
    right_frame,
    width=15,
    text='NEXT',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)


# widgets placement
register_religion.grid(row=0, column=1, pady=10, padx=20)
register_category.grid(row=1, column=1, pady=10, padx=20)
register_income.grid(row=2, column=1, pady=10, padx=20)
register_education.grid(row=3, column=1, pady=10, padx=20)
register_occupation.grid(row=4, column=1, pady=10, padx=20)
register_pan.grid(row=5, column=1, pady=10, padx=20)
register_aadhar.grid(row=6, column=1, pady=10, padx=20)


next_btn.grid(row=10, column=1, pady=10, padx=20)
right_frame.place(x=450, y=50)

scitizen_frame.grid(row=7, column=1, pady=10, padx=20)
eaccount_frame.grid(row=8, column=1, pady=10, padx=20)

scitizen_yes_rb.pack(expand=True, side=LEFT)
scitizen_no_rb.pack(expand=True, side=LEFT)


eaccount_yes_rb.pack(expand=True, side=LEFT)
eaccount_no_rb.pack(expand=True, side=LEFT)


# infinite loop
ws.mainloop()
