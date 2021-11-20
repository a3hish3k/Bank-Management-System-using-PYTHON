
from tkinter import *
from tkinter import messagebox
import mysql.connector
import sqlite3

f = ('Times', 14)
fsmall = ('Times', 8)

con = sqlite3.connect('bms_py.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS signup3(
                    atypr text, 
                    cardno text, 
                    pin number, 
                    facility text 
                    
                )
            ''')
con.commit()


ws = Tk()
ws.title('iBanking')
ws.geometry('950x700')
ws.config(bg='#0B5A81')


def insert_record():
    import random
    random_pin = StringVar()
    random_cardno = StringVar()
    var = StringVar()

    def random_cardno(N):
	    minimum = pow(16, N-1)
	    maximum = pow(16, N) - 1
	    return random.randint(minimum, maximum)

    print(random_cardno(13))
    
    def random_pin(N):
        minimum = pow(4, N-1)
	    maximum = pow(4, N) - 1
	    return random.randint(minimum, maximum)
        
    print(random_pin(3))

    check_counter = 0
    warn = ""
    if atype.get() == "":
       warn = "Select Account Type can't be empty"
    else:
        check_counter += 1

    if atmcb.get() == "":
        warn = " can't be empty"
    else:
        check_counter += 1

    if mobilecb.get() == "":
       warn = "Income can't be empty"
    else:
        check_counter += 1

    if chequecb.get() == "":
        warn = "Education can't be empty"
    else:
        check_counter += 1

    if internetbankingcb.get() == "":
        warn = "Occupation can't be empty"
    else:
        check_counter += 1

    if emailalertcb.get() == "":
        warn = "PAN Number can't be empty"
    else:
        check_counter += 1

    if estatementcb.get() == "":
        warn = "Aadhar Number can't be empty"
    else:
        check_counter += 1

    if check_counter == 9:
        try:
            con = sqlite3.connect('bms_py.db')
            cur = con.cursor()
            cur.execute("INSERT INTO signup3 VALUES (:atype, :cardno, :pin, :facility)", {
                'atype': atype.get(),
                'cardno': random_cardno.get(),
                'pin': random_pin.get(),
                'facility': var.get()
                
            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')
            
            ws.destroy()
            import Menu
        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)


def destroy():
    ws.destroy()

atype = StringVar()
atype.set('Saving Account')

cb = IntVar()
atmcb = IntVar()
mobilecb = IntVar()
chequecb = IntVar()
internetbankingcb = IntVar()
emailalertcb = IntVar()
estatementcb = IntVar()

right_frame = Frame(
    ws,
    #text="Personal Details",
    bd=3,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)
label1 = Label(ws, text="Accounts Details", font=f)

label1.pack()

Label(
    right_frame,
    text="Select Account Type",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

cb_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10,
    pady=30,
)

atype_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)


atype_sa_rb = Radiobutton(
    atype_frame,
    text='Saving Account',
    bg='#CCCCCC',
    variable=atype,
    value='Saving Account',
    font=('Times', 10),

)

atype_ca_rb = Radiobutton(
    atype_frame,
    text='Current Account',
    bg='#CCCCCC',
    variable=atype,
    value='Current Account',
    font=('Times', 10),

)

atype_fd_rb = Radiobutton(
    atype_frame,
    text='Fixed Deposit',
    bg='#CCCCCC',
    variable=atype,
    value='Fixed Deposit Account',
    font=('Times', 10),

)

Label(
    right_frame,
    text="Card Number",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="XXXX-XXXX-XXXX-XXXX",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=1, sticky=W, pady=10)

Label(
    right_frame,
    text="(Your 16-Digit Card Number)",
    bg='#CCCCCC',
    font=fsmall
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="It would appear on ATM Card, Cheque Book and Statement",
    bg='#CCCCCC',
    font=fsmall
).grid(row=2, column=1, sticky=W, pady=10)

Label(
    right_frame,
    text="Pin",
    bg='#CCCCCC',
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="XXXX",
    bg='#CCCCCC',
    font=f
).grid(row=3, column=1, sticky=W, pady=10)

Label(
    right_frame,
    text="(4-Digit PIN)",
    bg='#CCCCCC',
    font=fsmall
).grid(row=4, column=0, sticky=W, pady=5)

Label(
    right_frame,
    text="Services Required:",
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=5)


Checkbutton(
    cb_frame,
    text='ATM', 
    variable=atmcb,
    onvalue=1, 
    offvalue=0
).grid(row=6, column=0, sticky=W, pady=10)

Checkbutton(
    cb_frame,
    text='Mobile Banking',
    variable=mobilecb,
    onvalue=1,
    offvalue=0
).grid(row=6, column=1, sticky=W, pady=10)

Checkbutton(
    cb_frame,
    text='Cheque Book',
    variable=chequecb,
    onvalue=1,
    offvalue=0
).grid(row=7, column=0, sticky=W, pady=10)

Checkbutton(
    cb_frame,
    text='Internet Banking',
    variable=internetbankingcb,
    onvalue=1,
    offvalue=0
).grid(row=7, column=1, sticky=W, pady=10)

Checkbutton(
    cb_frame,
    text='E-mail Alert',
    variable=emailalertcb,
    onvalue=1,
    offvalue=0
).grid(row=8, column=0, sticky=W, pady=10)

Checkbutton(
    cb_frame,
    text='E-Statement',
    variable=estatementcb,
    onvalue=1,
    offvalue=0
).grid(row=8, column=1, sticky=W, pady=10)


Checkbutton(right_frame, text='Accept the terms & conditions', variable=cb,
            onvalue=1, offvalue=0).grid(row=9)

submit_btn = Button(
    right_frame,
    width=15,
    text='SUBMIT',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)

cancel_btn = Button(
    right_frame,
    width=15,
    text='CANCEL',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=destroy
)

# widgets placement

submit_btn.grid(row=10, column=0, pady=10, padx=20)
cancel_btn.grid(row=10, column=1, pady=10, padx=20)
right_frame.place(x=300, y=50)

atype_frame.grid(row=0, column=1, pady=10, padx=20)
cb_frame.grid(row=5, column=1, pady=10, padx=20)

atype_sa_rb.pack(expand=True, side=LEFT)
atype_ca_rb.pack(expand=True, side=LEFT)
atype_fd_rb.pack(expand=True, side=LEFT)



# infinite loop
ws.mainloop()
