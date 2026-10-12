#1

i = 1
while i <= 5:
    print("Hello")
    i += 1


#2

i = 0
while i <= 9:
    print(i)
    i += 1

#3

i = 1
while i <= 10:
    print(i)
    i += 1

#4

i = 10
while i >= 1:
    print(i)
    i -= 1

#5

i = 5
while i <= 50:
    print(i)
    i += 5


#6

i = 2
while i <= 20:
    print(i)
    i += 2


#7

i = 1
while i <= 19:
    print(i)
    i += 2


#8

i = 3
while i <= 18:
    print(i)
    i += 3


#9

i = 20
while i >= 2:
    print(i)
    i -= 2


#10

n = int(input("Enter a number : "))
i = 1
while i <= n:
    print(i)
    i += 1

#11

n = int(input("Enter a number : "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

#12

n = int(input("Enter a number : "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1

#13

n = int(input("Enter a number : "))
i = 1
while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1

#14

n = int(input("Enter a number : "))
i = 1
while i <= n:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    i += 1

#15

n = int(input("Enter a number : "))
i = 1
count = 0

while i <= n:
    if i % 2 == 0:
        count += 1
    i += 1

print("Count =", count)