# Import module
from tkinter import *

# Create object
root = Tk()
root.title('Retirement Calculator')
root.geometry( "400x500" )

solLabel = Label(root, text="", font=16)
solinLabel = Label(root, text="", font=16)

# Taking user input and calculating their retirement value: introduction of the function
def retirementValue():
    global solLabel
    global solinLabel
    solLabel.config(text="")
    solinLabel.config(text="")

    ancon = int(user_c.get())
    uage = int(user_age.get())
    urage = int(user_ra.get())  
    uir = float(user_ir.get())
    upv = float(user_pv.get()) 
    ui = float(user_i.get())
    wr = urage-uage # working years created by retirement age - current age
    uia = uir - ui # adjusted interested rate with inflation
    
    fv = upv * (1 + uir)
    fvi = upv * (1 + uia)
    i=1
    while i < wr:
        fv = round((fv + ancon) * (1+uir), 2)
        fvi = round((fvi + ancon) * (1+uia), 2)
        i=i+1

    #fv =round(( * (((1 + uir)**(wr)-1)/uir)), 2) #future value with annual deposits made at end of each year

    rValue = "$" + str("{:,}".format(fv))
    riValue = "$" + str("{:,}".format(fvi))

    if uage > 0 and urage > 0 and 0 < uir < 1 and upv >= 0 and urage > uage:    # check if user inputs are valid numbers greater than 0
       
        solLabel.config(text=rValue)
        solinLabel.config(text=riValue)

    else:
       
       solLabel.config(text=f'Check your inputs')
    
    solLabel.grid(row=8, column=2, padx=20, pady=20) 
    solinLabel.grid(row=9, column=2, padx=20, pady =20)  


# User input for current age
labelAge = StringVar()
labelAge.set("What is your current age?")
labelDir = Label(root, textvariable=labelAge, padx=10, pady=10)
labelDir.grid(row=1, column=1)

user_age = Entry(root)
user_age.grid(row=1, column=2)


# User input for retirement age
labelRa = StringVar()
labelRa.set("At what age do you want to retire?")
labelDir = Label(root, textvariable=labelRa, padx=10, pady=10)
labelDir.grid(row=2, column=1)

user_ra = Entry(root)
user_ra.grid(row=2, column=2)


# User input for expected investment return
labelIr = StringVar()
labelIr.set("What is your expected annual return?")
labelDir = Label(root, textvariable=labelIr, padx=10, pady=10)
labelDir.grid(row=3, column=1)

user_ir = Entry(root)
user_ir.grid(row=3, column=2)


# User input current portfolio value
labelPv = StringVar()
labelPv.set("What is your current portfolio value?")
labelDir = Label(root, textvariable=labelPv, padx=10, pady=10)
labelDir.grid(row=4, column=1)

user_pv = Entry(root)
user_pv.grid(row=4, column=2)

# User input additional contributions
labelC = StringVar()
labelC.set("What will you contribute annually?")
labelDir = Label(root, textvariable=labelC, padx=10, pady=10)
labelDir.grid(row=5, column=1)

user_c = Entry(root)
user_c.grid(row=5, column=2)

# User input inflation estimation
labelI = StringVar()
labelI.set("Estimated inflation per year?")
labelDir = Label(root, textvariable=labelI, padx=10, pady=10)
labelDir.grid(row=6, column=1)

user_i = Entry(root)
user_i.grid(row=6, column=2)

labelRv = StringVar()
labelRv.set("You will have:")
labelDir = Label(root, textvariable=labelRv, padx=10, pady=30)
labelDir.grid(row=8, column=1)

labelArv = StringVar()
labelArv.set("In today's dollars:")
labelDir = Label(root, textvariable=labelArv, padx=10, pady=30)
labelDir.grid(row=9, column=1)


myButton = Button(root, text="Calculate", padx=10, pady=10, command=retirementValue)
myButton.grid(row=10, column=1)

# Execute tkinter
root.mainloop()