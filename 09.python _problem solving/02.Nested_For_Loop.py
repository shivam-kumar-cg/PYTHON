#1
number=int(input("enter a number :"))
for i in range(number):
    for j in range(number):
        print("*", end=" ")
    print()


#2
for i in range(3):
    for j in range(1, 4):
        print(j, end=" ")
    print()


3
number=int(input("enter a number :"))
for i in range(1, number):
    for j in range(number-1):
        print(i, end=" ")
    print()


#4
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


#5
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


#6
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#8
for i in range(11):
    for j in range(1,6):
        print(i*j,end="|")
    print()    

#9
for i in range(1,4):
    for j in range(1,6):
        print(i*j,end="|")
    print()    

#10
for i in range(1,6):
    for j in range(1,6):
        print(j*j,end="|")
    print()    

#11
for i in range(1,6):
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print() 

for i in range(1,6):
    for j in range(0,6-i):
        print("*",end="")
    print()    

for i in range(1,6):
    a=1
    for j in range(i):
        print(a,end=" ")
        a+=2
    print()

for i in range(1,4):
    for j in range(1,4):
        print((i,j),end="")
    print()

for i in range(5):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print()       

for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print()        

