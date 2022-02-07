

# Python program to calculate monthly EMI (Equated Monthly Installment)

# EMI Formula = p * r * (1+r)^n/((1+r)^n-1)

# If the interest rate per annum is R% then 
# interest rate per month is calculated using: 

# Monthly Interest Rate (r) = R/(12*100)

# Varaible name details:
# p = Principal or Loan Amount
# r = Interest Rate Per Month
# n = Number of monthly installments

# Reading inputs from user
import math

p = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate: "))
n = int(input("Enter number of months: " ))

# Calculating interest rate per month
r = R/(12*100)

# Calculating Equated Monthly Installment (EMI)
emi = p * r * ((1+r)**n)/((1+r)**n - 1)
emi = math.ceil(emi)
print("Monthly EMI = ", emi)
 