
from tkinter import *
from tkinter import messagebox
import mysql.connector
import sqlite3

f = ('Times', 14)

con = sqlite3.connect('bms_py.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS signup(
                    name text, 
                    fname text,
                    dob text, 
                    gender text,
                    email text,
                    marital text,
                    address text,
                    city text,
                    pincode text,
                    state text
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
    if register_name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1

    if register_fname.get() == "":
        warn = "Father's Name can't be empty"
    else:
        check_counter += 1

    if register_dob.get() == "":
       warn = "Date of Birth can't be empty"
    else:
        check_counter += 1

    if var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if register_email.get() == "":
        warn = "E-mail can't be empty"
    else:
        check_counter += 1
    
    if marital.get() == "":
        warn = "Select Marital Status"
    else:
        check_counter += 1

    if register_address.get() == "":
        warn = "Address can't be empty"
    else:
        check_counter += 1

    if register_city.get() == "":
        warn = "City didn't match!"
    else:
        check_counter += 1
    
    if register_pincode.get() == "":
        warn = "Pin can't be empty"
    else:
        check_counter += 1
    
    if register_state.get() == "":
        warn = "State can't be empty"
    else:
        check_counter += 1

    if check_counter == 10:
        try:
            con = sqlite3.connect('bms_py.db')
            cur = con.cursor()
            cur.execute("INSERT INTO signup VALUES (:name, :fname, :dob, :gender, :email, :marital, :address, :city, :pincode, :state)", {
                'name': register_name.get(),
                'fname':register_fname.get(),
                'dob':register_dob.get(),
                'gender': var.get(),
                'email': register_email.get(),
                'marital': marital.get(),
                'address': register_address.get(),
                'city': register_city.get(),
                'pincode': register_pincode.get(),
                'state': register_state.get()
            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')
            ws.destroy()
            
            import Signup2

        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)


var = StringVar()
var.set('male')

marital = StringVar()
marital.set('Unmarried')


right_frame = Frame(
    ws,
    #text="Personal Details",
    bd=3,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)
label1 = Label(ws, text="Personal Details", font=f)

label1.pack()
Label(
    right_frame,
    text="Enter Name",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Father's Name",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Date of Birth",
    bg='#CCCCCC',
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select Gender",
    bg='#CCCCCC',
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select E-mail",
    bg='#CCCCCC',
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Marital Status",
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Address",
    bg='#CCCCCC',
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter City",
    bg='#CCCCCC',
    font=f
).grid(row=7, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Pin Code",
    bg='#CCCCCC',
    font=f
).grid(row=8, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter State",
    bg='#CCCCCC',
    font=f
).grid(row=9, column=0, sticky=W, pady=10)



gender_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

marital_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

register_name = Entry(
    right_frame,
    font=f
)

register_fname = Entry(
    right_frame,
    font=f
)

register_dob = Entry(
    right_frame,
    font=f
)


male_rb = Radiobutton(
    gender_frame,
    text='Male',
    bg='#CCCCCC',
    variable=var,
    value='male',
    font=('Times', 10),

)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='#CCCCCC',
    variable=var,
    value='female',
    font=('Times', 10),

)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='#CCCCCC',
    variable=var,
    value='others',
    font=('Times', 10)

)


register_email = Entry(
    right_frame,
    font=f,
    
)
married_rb = Radiobutton(
    marital_frame,
    text='Married',
    bg='#CCCCCC',
    variable=marital,
    value='Married',
    font=('Times', 10),

)

unmarried_rb = Radiobutton(
    marital_frame,
    text='Unmarried',
    bg='#CCCCCC',
    variable=marital,
    value='Unmarried',
    font=('Times', 10),

)

register_address = Entry(
    right_frame,
    font=f,
)

register_city = Entry(
    right_frame,
    font=f,
)

register_pincode = Entry(
    right_frame,
    font=f,
)

register_state = Entry(
    right_frame,
    font=f,
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
register_name.grid(row=0, column=1, pady=10, padx=20)
register_fname.grid(row=1, column=1, pady=10, padx=20)
register_dob.grid(row=2, column=1, pady=10, padx=20)
register_email.grid(row=4, column=1, pady=10, padx=20)
register_address.grid(row=6, column=1, pady=10, padx=20)
register_city.grid(row=7, column=1, pady=10, padx=20)
register_pincode.grid(row=8, column=1, pady=10, padx=20)
register_state.grid(row=9, column=1, pady=10, padx=20)




next_btn.grid(row=10, column=1, pady=10, padx=20)
right_frame.place(x=450, y=50)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
marital_frame.grid(row=5, column=1, pady=10, padx=20)

male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)

married_rb.pack(expand=True, side=LEFT)
unmarried_rb.pack(expand=True, side=LEFT)


# infinite loop
ws.mainloop()
