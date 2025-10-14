# Lab Assignment 1
# Name: Pratik Ranjan Mahala
# Regd No: 24E113A07
# Serial No: 15



#1
import math
def calc(a,b):
    print("OPERATIONS MENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Tan(x)")
    print("7. Sin(x)")
    print("8. Cos(x)")
    print("9. Factorial")
    print("10. Log(x)")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        return a / b
    elif choice == 5:
        return math.pow(x,y)
    elif choice == 6:
        return math.tan(math.radians(x))
    elif choice == 7:
        return math.sin(math.radians(x))
    elif choice == 8:
        return math.cos(math.radians(x))
    elif choice == 9:
        return math.factorial(x)
    elif choice == 10:
        return math.log(x)
    else:
        print("Invalid choice")
        return None
    

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(calc(x, y))
print(id(calc))

#2
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter the number of terms: "))
fibonacci(num)
print(id(fibonacci))

#3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if (a==b):
    print("Numbers are equal")
elif (a < b):
    print(" First number is less than second number ")
else:
    print(" First number is greater than second number ")

#4
for i in range(1, 11):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

#5
for i in range(1, 11):
    for j in range(1, 12-i):
        print(i, end=" ")
    print()

#6
cash = int(input("Enter the cash amount: "))    
if cash > 0:
    notes_of_100 = cash // 100
    cash = cash % 100
    notes_of_50 = cash // 50
    cash = cash % 50
    notes_of_10 = cash // 10
    cash = cash % 10
    print("Notes of 100:", notes_of_100)
    print("Notes of 50:", notes_of_50)
    print("Notes of 10:", notes_of_10)
    print("Remaining cash (less than 10):", cash)
elif cash == 0:
    print("Invalid cash amount. Go get a j*b!")
else:
    print("Just repay your loan you fool!")

#7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def GCD(x, y):
    while(y):
        x, y = y, x % y
    return x

print(GCD(a, b))

#8
no_of_employees = 10
overtime_rate = 12
overtime_pay = 0

for i in range(1, no_of_employees+1):
    hours_worked = int(input(f"Enter hours worked for employee {i}: "))
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay += overtime_hours * overtime_rate
    else:
        overtime_pay += 0

print(f"Overtime Pay: ${overtime_pay}")

#9
days_late = int(input("Enter number of days late: "))
fine = 0

if days_late <= 5:
    fine = days_late * 0.50
elif days_late>5 and days_late <= 10:
    fine = days_late * 1.00
elif days_late>10 and days_late <= 30:
    fine = days_late * 5.00
else:
    fine = days_late * 5.00
    print("Membership cancelled")

print(f"Fine: Rs. {fine}")

#10
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
elif month == 2:
    if (year%400==0) or (year%4==0 and year%100!=0):
        days = 29
    else:
        days = 28
else:
    days = 0
    print("Invalid month and year")

print(f"Number of days: {days}")
