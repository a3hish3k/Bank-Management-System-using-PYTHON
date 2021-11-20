from tkinter import *
global root
root = Tk()
root.title = ("Welcome to iBanking")
root.geometry("950x650")
root.config(bg='#0B5A81')
f = ('Times', 14)
f1 = ('Times', 20)

def Signup():
    import Signup

def Deposit_response():
    root.destroy()
    import Deposit


def Pin_change_response():
    from transaction import Pin_change


'''def Fast_cash_response():
    from transaction import Fast_cash'''


def Withdrawl_response():
    root.destroy()
    import Withdrawl
    

def Mini_statement_response():
    from transaction import Mini_statement


def Balance_enquiry_response():
    from transaction import Balance_enquiry


def Exit_response():
    root.destroy()


Label(
    root,
    bd=2,
    font=f1,
    text="Welcome to iBanking",
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
).place(x=350, y=25)

#Widget
left_frame = Frame(
    root,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=100,
    pady=100
)

Label(
    root,
    bd=2,
    font=f,
    text="Welcome, Abhishek",
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
).place(x=350, y=110)


create_account_btn = Button(
    left_frame,
    width=15,
    text='Create Account',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=Signup
)

Deposit_btn = Button(
    left_frame,
    width=15,
    text='Deposit',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=Deposit_response
)
Pin_change_btn = Button(
    left_frame,
    width=15,
    text='Pin Change',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=Pin_change_response
)

'''Fast_cash_btn = Button(
    left_frame,
    width=15,
    text='Fast Cash',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=Fast_cash_response
)'''

Withdrawl_btn = Button(
    left_frame,
    width=15,
    text='Withdrawl',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=Withdrawl_response
)
Mini_statement_btn = Button(
    left_frame,
    width=15,
    text='Mini Statement',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=Mini_statement_response
)
Balance_enquiry_btn = Button(
    left_frame,
    width=15,
    text='Balance Enquiry',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=Balance_enquiry_response
)
exit_btn = Button(

    left_frame,
    width=15,
    text='Exit',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=Exit_response
)

Deposit_btn.grid(row=0, column=0, pady=5, padx=10)
Pin_change_btn.grid(row=0, column=1, pady=10, padx=20)
'''Fast_cash_btn.grid(row=0, column=2, pady=5, padx=10)'''
Withdrawl_btn.grid(row=1, column=0, pady=10, padx=20)
Mini_statement_btn.grid(row=1, column=1, pady=10, padx=20)
Balance_enquiry_btn.grid(row=1, column=2, pady=10, padx=20)
create_account_btn.grid(row=2, column=0, pady=5, padx=10)
exit_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=80, y=100)
root.mainloop()
