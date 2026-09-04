#1
name = input("Enter your name: ")
print(name)

#2
city = input("Enter your city: ")
print(f"Your city is {city}")

#3
name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)

#4
age = input("Enter age: ")

print(type(age))

#5
value = input("Enter something: ")

print(type(value))
#6
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(first_name, last_name)
#7
name = input("Enter your name: ")
city = input("Enter your city: ")
college = input("Enter your college: ")

print(name)
print(city)
print(college)

#8first_name, last_name = input("Enter first and last name: ").split()

print(first_name)
print(last_name)

#9
word1, word2 = input().split()

#10
word1, word2, word3 = input("Enter three words: ").split()

print(word1)
print(word2)
print(word3)

#11
number = int("25")

print(number)
print(type(number))

#12
number = float("25.5")

print(number)
print(type(number))




#13
number = 100

text = str(number)

print(text)
print(type(text))

#14
age = int(input("Enter your age: "))

print(age)
print(type(age))

#15
price = float(input("Enter price: "))

print(price)
print(type(price))


#16
a = input()
b = input()

print(a + b)

#17
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

#18
name = "Rahul"
age = 20

print(f"My name is {name} and I am {age} years old.")

#19
a = 10
b = 20

sum = a + b

print(f"The sum is {sum}")


#20
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")


#21
price = float(input("Enter price: "))

print(f"Price: {price:.2f}")

#22
price = 99.5678

print(f"{price:.2f}")

#23
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")

#24
print("A", "B", "C")

#25
print("2026", "08", "19", sep="-")

#26
print("Hello", end=" ")
print("World")

#27
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

total = first + second

print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Sum: {total}")

#28
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")

#29
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks:.2f}")

#30
name = input("Enter student name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
city = input("Enter city: ")

print("\nStudent Information")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f}")
print(f"City: {city}")