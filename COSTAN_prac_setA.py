
print(f"\n\n{'STANDARD PAYROLL':=^40}")
print("\t SET A")

tanname = input("Employee Name: ")
tanjobPosition = input("Input letter for respective job position:"
                       "\n|A| Janitor"
                       "\n|B| Clerk"
                       "\n|C| Cashier"
                       "\n|D| Manager"
                       "\n")
tanhrsWorked = int(input("Actual Hours Worked: "))

match tanjobPosition.strip().capitalize():
    case 'A':
        jobCateg = 'Janitor'
        tanmonthlySalary = 18000

    case 'B':
        jobCateg = 'Clerk'
        tanmonthlySalary = 22000

    case 'C':
        jobCateg = 'Cashier'
        tanmonthlySalary = 24000

    case 'D':
        jobCateg = 'Manager'
        tanmonthlySalary = 40000

CostanBHMS = tanmonthlySalary/ 2
CostanHR = CostanBHMS / 88

costanAB = 0
costanAD = 0
costanOTH = 0
costanOTR = 0
costanOTP = 0

if tanhrsWorked < 88:
    costanAB = 88 - tanhrsWorked
    costanAD = costanAB * CostanHR
elif tanhrsWorked > 88:
    costanOTH = tanhrsWorked - 88
    costanOTR = CostanHR * 1.25
    costanOTP = costanOTH * costanOTR
else:
    pass
netSalary = CostanBHMS-costanAD+costanOTP

print(f"\n\n{'YOOUR PAYROLL':=^40}")
print(f"\nEMPLOYEE POSITION: {tanname.title()}"
      f"\nJOB POSITION: {jobCateg}"
      f"\nACTUAL HOURS WORKED: {tanhrsWorked}"
      f"\nMONTHLY SALARY: PHP {tanmonthlySalary:,}"
      f"\nHALF-MONTH SALARY: PHP {CostanBHMS:,}"
      f"\nHOURLY RATE: {CostanHR:,.2f}"
      f"\n\nABSENT HOURS: {costanAB} HOURS"
      f"\nEXPECTED ABSENT DEDUCTION: PHP {costanAD:,.2f}"
      f"\nOVERTIME HOURS: {costanOTH:,.2f}"
      f"\nEXPECTED OVERTIME PAY: PHP {costanOTP:,.2f}"
      f"\n\nEXPECTED NET SALARY: PHP {netSalary:,.2f}")

