from tkinter import *
from tkinter import messagebox
from PIL import ImageTk # for using jpeg image

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be Empty !')
    elif usernameEntry.get()=='Saurav Mathur' and passwordEntry.get()=='Saurav123@':
        messagebox.showinfo('Success','Welcome !')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error',"Please Enter correct Details !")

window=Tk()

window.geometry('1280x700+0+0') # +0,+0 is distance from x axis and y axis
window.title("Login System of Student")
window.resizable(False,False) #Disable maximize button

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(window,image=backgroundImage)
bglabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='student.png')

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10,padx=10)

usernameImage=PhotoImage(file='user.png')

usernameLabel=Label(loginFrame,image=usernameImage,text='username:',compound=LEFT
                    ,font=('comic sans',20,'bold'),bg='white' )
#Flat icon website for free logo
usernameLabel.grid(row=1,column=0,pady=10,padx=10)

usernameEntry=Entry(loginFrame, font=('new times roman',20),bd=3,fg='royalblue')
usernameEntry.grid(row=1,column=1)

### Password line

passwordImage=PhotoImage(file='password.png')

passwordLabel=Label(loginFrame,image=passwordImage,text='password:',compound=LEFT
                    ,font=('comic sans',20,'bold'),bg='white' )
#Flat icon website for free logo
passwordLabel.grid(row=2,column=0,pady=10,padx=10)

passwordEntry=Entry(loginFrame, font=('new times roman',20),bd=3,fg='royalblue')
passwordEntry.grid(row=2,column=1)

loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=10
                   ,fg='white',bg='cornflowerblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=8)

window.mainloop()

