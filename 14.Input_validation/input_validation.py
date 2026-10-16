
#1
marks = int(input("Enter marks: "))

while marks < 0 or marks > 100:
    print("Invalid marks")
    marks = int(input("Enter marks again: "))

print("Accepted marks:", marks)


#2
num = int(input("Enter a positive number: "))

while num <= 0:
    print("Invalid number")
    num = int(input("Enter again: "))

print("Accepted number:", num)


#3
age = int(input("Enter age: "))

while age < 0 or age > 120:
    print("Invalid age")
    age = int(input("Enter age again: "))

print("Accepted age:", age)


#4
print("1. View profile")
print("2. Edit profile")
print("3. Settings")
print("4. Exit")

choice = int(input("Enter your choice: "))

while choice < 1 or choice > 4:
    print("Invalid choice")
    choice = int(input("Enter choice again: "))

print("Selected option:", choice)


#5
password = input("Enter password: ").strip()

while len(password) < 8:
    print("Password must contain at least 8 characters")
    password = input("Enter password again: ").strip()

print("Password accepted")


#6
temp = float(input("Enter temperature: "))

while temp < -20 or temp > 45:
    print("Invalid temperature")
    temp = float(input("Enter temperature again: "))

print("Accepted temperature:", temp)


#7
balance = 5000
amount = int(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance:
    print("Invalid withdrawal amount")
    amount = int(input("Enter amount again: "))

balance = balance - amount
print("Remaining balance:", balance)


#8
username = input("Enter username: ").strip()

while len(username) < 5 or " " in username:
    print("Invalid username")
    username = input("Enter username again: ").strip()

print("Accepted username:", username)


#9
num = int(input("Enter a positive number divisible by 3 and 5: "))

while num <= 0 or num % 3 != 0 or num % 5 != 0:
    print("Invalid number")
    num = int(input("Enter number again: "))

print("Accepted number:", num)


#10
pin = 2468
attempt = 1

while attempt <= 3:
    entered_pin = int(input("Enter PIN: "))

    if entered_pin == pin:
        print("Access granted")
        break

    print("Incorrect PIN")
    attempt += 1

if attempt > 3:
    print("Access denied")


#11
num = int(input("Enter number between 10 and 50: "))

while num < 10 or num > 50:
    print("Invalid number")
    num = int(input("Enter number again: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#12
balance = 2000
amount = int(input("Enter deposit amount: "))

while amount <= 0:
    print("Invalid deposit amount")
    amount = int(input("Enter amount again: "))

balance = balance + amount
print("New balance:", balance)


#13
num = int(input("Enter number between 1 and 100: "))

while num < 1 or num > 100:
    print("Invalid number")
    num = int(input("Enter number again: "))

print("Accepted number:", num)


#14
marks = int(input("Enter marks: "))

while marks < 0 or marks > 100:
    print("Invalid marks")
    marks = int(input("Enter marks again: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


#15 

while True:
    name = input("Enter username: ").strip()
    pass1 = input("Enter password: ")

    if len(name) >= 5 and " " not in name and len(pass1.strip()) >= 8:
        print("Login successful")
        break
    else:
        print("Invalid input, try again")


#16

a = float(input("Enter first number: "))
op = input("Enter operator: ")

while op not in ["+", "-", "*", "/"]:
    print("Wrong operator")
    op = input("Enter operator: ")

b = float(input("Enter second number: "))

while op == "/" and b == 0:
    print("Cannot divide by zero")
    b = float(input("Enter second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
else:
    print(a / b)


#17

bal = 10000

while True:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Balance:", bal)

    elif ch == 2:
        amt = float(input("Enter amount: "))

        while amt <= 0:
            print("Invalid amount")
            amt = float(input("Enter amount: "))

        bal = bal + amt
        print("Balance:", bal)

    elif ch == 3:
        amt = float(input("Enter amount: "))

        while amt <= 0 or amt > bal:
            print("Invalid amount")
            amt = float(input("Enter amount: "))

        bal = bal - amt
        print("Balance:", bal)

    elif ch == 4:
        print("Thank you")
        break

    else:
        print("Wrong choice")


#18

while True:
    m = int(input("Enter month (1-12): "))
    d = int(input("Enter day (1-31): "))

    if m >= 1 and m <= 12 and d >= 1 and d <= 31:
        print("Valid input")
        break
    else:
        print("Invalid input, try again")


#19

qty = int(input("Enter quantity: "))

while qty <= 0:
    print("Enter positive quantity")
    qty = int(input("Enter quantity: "))

price = float(input("Enter price: "))

while price <= 0:
    print("Enter positive price")
    price = float(input("Enter price: "))

total = qty * price
print("Total price:", total)


#20

n = int(input("How many numbers (1-20): "))

while n < 1 or n > 20:
    print("Enter number between 1 and 20")
    n = int(input("How many numbers: "))

total = 0

for i in range(n):
    num = float(input("Enter number: "))
    total = total + num

avg = total / n
print("Average:", avg)


#21

while True:
    pass1 = input("Enter password: ")

    upper = False
    lower = False
    digit = False
    space = False

    for ch in pass1:
        if ch.isupper():
            upper = True
        if ch.islower():
            lower = True
        if ch.isdigit():
            digit = True
        if ch.isspace():
            space = True

    if len(pass1) >= 8 and upper and lower and digit and not space:
        print("Password accepted")
        break
    else:
        print("Password must have 8 characters, uppercase, lowercase,")
        print("one digit and no spaces")


#22

num = int(input("Enter number (1-10): "))

while num < 1 or num > 10:
    print("Invalid number")
    num = int(input("Enter number (1-10): "))

print("Accepted number:", num)


#23

a = int(input("Enter first score: "))

while a < 0 or a > 100:
    print("Invalid score")
    a = int(input("Enter first score: "))

b = int(input("Enter second score: "))

while b < 0 or b > 100:
    print("Invalid score")
    b = int(input("Enter second score: "))

c = int(input("Enter third score: "))

while c < 0 or c > 100:
    print("Invalid score")
    c = int(input("Enter third score: "))

total = a + b + c
avg = total / 3

print("Total:", total)
print("Average:", avg)


#24
bal = 10000

amt = int(input("Enter withdrawal amount: "))

while amt <= 0 or amt > bal or amt % 100 != 0:
    print("Invalid amount")
    amt = int(input("Enter withdrawal amount: "))

bal = bal - amt

print("Withdrawn amount:", amt)
print("Remaining balance:", bal)
