import time
import datetime
from tkinter import*
from tkinter import messagebox
 

root= Tk()
root.title("Payroll Systems")
root.geometry('1350x650+0+0')
Tops= Frame(root, width= 1350, height= 50, bd=8, relief= "raise")
Tops.pack(side=TOP)
f1= Frame(root, width=600, height=600, bd=8, relief="raise")
f1.pack(side= LEFT)
f2= Frame(root, width=300, height= 700, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a= Frame(f1, width=600, height= 200,bd=20, relief= "raise")
f1a.pack(side=TOP)
f1b= Frame(f1,width=600, height= 600, bd=20, relief= "raise")
f1b.pack(side=TOP)
lblinfo= Label(Tops, font=('arial',30,'bold'), text=" PAYROLL MANAGEMENT SYSTEMS")
lblinfo.grid(row=0, column=0)
def iExit():
    qExit= messagebox.askyesno("PAYROLL SYSTEM","Do You Want To Exit The Systems")
    if qExit>0:
        root.destroy()
        return
def Reset():
    Name.set("")
    Address.set("")
    HoursWorked.set("")
    WagesHour.set("")
    Payable.set("")
    Taxable.set("")
    NetPayable.set("")
    GrossPayable.set("")
    OvertimeHours.set("")
    Employer.set("")
    NINumber.set("")
    txtPaySlip.delete("1.0",END)
def EnterInfo():
    txtPaySlip.insert(END, "\t\tPay Slip\n\n")
    txtPaySlip.insert(END, 'Name:\t\t'+Name.get()+"\n\n")
    txtPaySlip.insert(END, 'Address:\t\t'+Address.get()+"\n\n")
    txtPaySlip.insert(END, 'Employer:\t\t'+Employer.get()+"\n\n")
    txtPaySlip.insert(END, 'NIMumber:\t\t'+NINumber.get()+"\n\n")
    txtPaySlip.insert(END, 'HoursWorked:\t\t'+HoursWorked.get()+"\n\n")
    txtPaySlip.insert(END, 'NetPayable:\t\t'+NetPayable.get()+"\n\n")
    txtPaySlip.insert(END, 'Wages Per Hour:\t\t'+WagesHour.get()+"\n\n")
    txtPaySlip.insert(END,'Tax Paid:\t\t'+Taxable.get()+"\n\n")
    txtPaySlip.insert(END, 'Payable:\t\t'+ Payable.get()+"\n\n")
def WeeklyWages():
    HoursWorkedPerWeek= float(HoursWorked.get())
    WagesPerHour= float(WagesHour.get())

    Paydue= WagesPerHour*HoursWorkedPerWeek
    PaymentDue= "$",str('%.2f'%(Paydue))
    Payable.set(PaymentDue)

    tax= Paydue*0.2
    Taxables= "$",str('%.2f'%(tax))
    Taxable.set(Taxables)

    netpay= Paydue-tax
    NetPays="$",str('%.2f'%(netpay))
    NetPayable.set(NetPays)

    if HoursWorkedPerWeek>40:
       overTimeHours= (HoursWorkedPerWeek-40)+WagesPerHour*1.5
       Overtimehrs="Rs.",str('%.2f' %(overTimeHours))
       OvertimeHours.set(Overtimehrs)
    elif HoursWorkedPerWeek <=40:
        overTimePay=(HoursWorkedPerWeek- 40)+WagesPerHour*1.5
        Overtimehrs="RS.",str ('%.2f' %(overTimePay))
        OvertimeHours.set(Overtimehrs)
    return
#===============================================creating variables==========================================
Name= StringVar()
Address= StringVar()
HoursWorked= StringVar()
WagesHour= StringVar()
Payable= StringVar()
Taxable=StringVar()
NetPayable=StringVar()
GrossPayable= StringVar()
OvertimeHours=StringVar()
Employer=StringVar()
NINumber=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
DateOfOrder.set(time.strftime("%d/%m/%Y"))
#==================================================label widget===============================================
lblName= Label(f1a,text= "Name",font=('arial',16,'bold'),bd=20).grid(row=0,column=0)
lblAddress= Label(f1a,text= "Address",font=('arial',16,'bold'),bd=20).grid(row=0,column=2)
lblEmployer= Label(f1a,text= "Employer",font=('arial',16,'bold'),bd=20).grid(row=1,column=0)

lblNINumber= Label(f1a,text= "NI Number",font=('arial',16,'bold'),bd=20).grid(row=1,column=2)

lblHoursWorked= Label(f1a,text= "Hours Worked",font=('arial',16,'bold'),bd=20).grid(row=2,column=0)

lblHourlyRate= Label(f1a,text= "Hourly Rate",font=('arial',16,'bold'),bd=20).grid(row=2,column=2)

lblTax= Label(f1a,text= "Tax",font=('arial',16,'bold'),bd=20,anchor='w').grid(row=3,column=0)

lblOverTime= Label(f1a,text= "Over Time",font=('arial',16,'bold'),bd=20).grid(row=3,column=2)

lblGrossPay= Label(f1a,text= "Gross Pay",font=('arial',16,'bold'),bd=20).grid(row=4,column=0)

lblNetPay= Label(f1a,text= "Net Pay",font=('arial',16,'bold'),bd=20).grid(row=4,column=2)
#===========================================entry widget================================================
etxtName= Entry(f1a, textvariable= Name,font=('arial',8,'bold'),bd=16,width=22, justify='left')
etxtName.grid(row=0,column=1)
etxtAddress= Entry(f1a,textvariable= Address,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtAddress.grid(row=0,column=3)
etxtEmployer= Entry(f1a,textvariable= Employer,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtEmployer.grid(row=1,column=1)
etxtHoursWorked= Entry(f1a,textvariable= HoursWorked,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtHoursWorked.grid(row=2,column=1)
etxtWagesPerHours= Entry(f1a,textvariable= WagesHour,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtWagesPerHours.grid(row=2,column=3)
etxtninoW= Entry(f1a,textvariable= NINumber,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtninoW.grid(row=1,column=3)
etxtGrossPay= Entry(f1a,textvariable= Payable,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtGrossPay.grid(row=4,column=1)
etxtNetPay= Entry(f1a,textvariable= NetPayable,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtNetPay.grid(row=4,column=3)
etxtTax= Entry(f1a,textvariable= Taxable,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtTax.grid(row=3,column=1)
etxtOverTime= Entry(f1a,textvariable= OvertimeHours,font=('arial',8,'bold'),bd=16, width=22, justify='left')
etxtOverTime.grid(row=3,column=3)
#=========================================text widget=========================================================
lblPaySlip=Label(f2,font=('arial',20,'bold'),textvariable=DateOfOrder).grid(row=0,column=0)
txtPaySlip= Text(f2, height=22, width=34,bd=16,font=('arial',12,'bold'))
txtPaySlip.grid(row=1,column=0)
#===========================================buttons widget=====================================================
btnSalary=Button(f1b, text='Weekly Salary',padx=16,pady=16,bd=8,fg="black",
                 font=('arial',12,'bold'),width=14,height=1,command=WeeklyWages).grid(row=0,column=0)
btnReset=Button(f1b, text='Reset',padx=16,pady=16,bd=8,fg="black",
                 font=('arial',12,'bold'),width=14,height=1,command=Reset).grid(row=0,column=1)
btnPayslip=Button(f1b, text='View Payslip',padx=16,pady=16,bd=8,fg="black",
                 font=('arial',12,'bold'),width=14,height=1,command=EnterInfo).grid(row=0,column=2)
btnExit=Button(f1b, text='Exit System',padx=16,pady=16,bd=8,fg="black",
                 font=('arial',12,'bold'),width=14,height=1,command= iExit).grid(row=0,column=3)


root.mainloop()
