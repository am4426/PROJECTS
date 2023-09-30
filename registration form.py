from tkinter import *
root = Tk()
root.geometry("500x500")
def getvals():
    print("Accepted")
Label(root, text="PYTHON REGISTRATION FORM", font="ar 15 bold").grid(row=0, column=3)
name = Label(root, text="NAME")
age = Label(root, text="AGE")
gender = Label(root, text="GENDER")
phone = Label(root, text="PHONE")
paymentmode = Label(root, text="PAYMENT MODE")
name.grid(row=2, column=2)
age.grid(row=3, column=2)
gender.grid(row=4, column=2)
phone.grid(row=5, column=2)
paymentmode.grid(row=6, column=2)
namevalue = StringVar
agevalue = StringVar
gendervalue = StringVar
phonevalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable = namevalue)
agentry = Entry(root, textvariable=agevalue)
genderentry = Entry(root, textvariable=gendervalue)
phonevalue = Entry(root,textvariable=phonevalue)
paymentmodevalue = Entry(root,textvariable=paymentmodevalue)
checkvalue=Entry(root, textvariable=checkvalue)

nameentry.grid(row=2,column=3)
agentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
phonevalue.grid(row=5,column=3)
paymentmodevalue.grid(row=6,column=3)

checkbtn = Checkbutton(text="REMEMBER ME", variable = checkvalue)
checkbtn.grid(row=7,column=3)

Button(text="SUBMIT", command=getvals).grid(row=9,column=3)


root.mainloop()