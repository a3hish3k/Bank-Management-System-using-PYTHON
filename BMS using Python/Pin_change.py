from subprocess import pwd
import sqlite3
from tkinter import messagebox
from tkinter import *
global ws
ws = Tk()
ws.title = ("Welcome to iBanking")
ws.geometry("950x650")
ws.config(bg='#0B5A81')
f = ('Times', 14)
f1 = ('Times', 20)

con = sqlite3.connect('bms_py.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS tranctions(
                    withdrawl text, 
                    deposit text, 
                    fast_cash number, 
                    balance text 
                    
                )
            ''')
con.commit()

def withdrawl_response():
    curBal, acctNo, cursor, stringTheDeets, actDtlsTxt, tfr = StringVar()
    wdrAmt = float(wdrAmt.GetValue())
    if (wdrAmt <= curBal):
        newBal = curBal - wdrAmt
        updateQuery = "UPDATE ibankingdb.account SET balance = " + \
            str(newBal) + " WHERE account_no = " + acctNo.GetValue()
        cursor.execute(updateQuery)
        rowLockQuery = "SELECT * FROM ibankingdb.account WHERE account_no = " + \
            acctNo.GetValue()
        cursor.execute(rowLockQuery)
        row = cursor.fetchone()
        if row is not None:
            lblTxt = stringTheDeets(row)
            if tfr == 1:
                actDtlsTxt.SetLabelText("Source: "+lblTxt)
            else:
                actDtlsTxt.SetLabelText(lblTxt)
        else:
            actDtlsTxt.SetLabelText("Invalid query result.")
            return -1
    else:
        actDtlsTxt.SetLabelText(
            "Balance is insufficient for withdrawal in account.")
        return -1

def home_response():
    ws.destroy()
    import Menu

def exit_response():
    ws.destroy()
    
Label(
    ws,
    text="iBanking",
    bg='#CCCCCC',
    font=f1).place(x=400, y=10)

# widgets
left_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    left_frame,
    text="Enter the amount to make a Withdrawl:",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

wdrAmt_tf = Entry(
    left_frame,
    font=f
)

withdrawl_btn = Button(
    left_frame,
    width=15,
    text='Withdrawl',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=withdrawl_response
)

home_btn = Button(
    left_frame,
    width=15,
    text='Home',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=home_response
)

exit_btn = Button(
    left_frame,
    width=15,
    text='Exit',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=exit_response
)
# widgets placement
wdrAmt_tf.grid(row=0, column=1, pady=10, padx=20)
home_btn.grid(row=2, column=0, pady=10, padx=20)
exit_btn.grid(row=2, column=2, pady=10, padx=20)
withdrawl_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=100)
ws.mainloop()
