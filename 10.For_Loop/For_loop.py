#1
for i in range(1,6):
    print("Hello")

#2
for i in range(0,10):
    print(i , end=(" "))   

#3
for i in range(1,11):
    print(i,end=(" ")) 

#4
for i in range(10,0,-1):
    print(i,end=(" ")) 

#5
for i in range(1,11):
    print(5*i)

#6
for i in range(2,21):
    if i%2==0:
        print(f"{i} is even")

#7
for i in range(1,20):
    if i%2!=0:
        print(f"{i} is odd")

#8
for i in range(1,7):
    print(3*i)

#9
for i in range(20,1,-2):
    print(i)

#10
number=int(input("enter a no.limit :"))
for i in range(1,number+1):
    print(i)

#11
number=int(input("enter a no. limit :"))
for i in range(1,number+1):
    if i%2==0:
        print(i)

#12
number=int(input("enter a no. limit :"))
for i in range(1,number+1):
    if i%2==1:
        print(i)

#13
number=int(input("enter a no. limit :"))
for i in range(1,number+1):
    if i%3==0:
        print(i)

#14
number=int(input("enter a no. limit :"))
for i in range(1,number+1):
    if i%2==0 and i%3==0:
        print(i)

#15
number=int(input("enter a no. limit :"))
count=0
for i in range(1,number+1):
    if i%2==0:
        count+=1
print(count)