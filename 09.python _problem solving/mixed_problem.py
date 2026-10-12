# 2

ecount=0
gcount=0
pcount=0
fcount=0
for marks in range(10):
    marks=int(input("enter your marks :"))
    if marks>=75 and marks<=100:
        print("excellent")
        ecount+=1
    elif marks>=50 and marks<=74:
        print("good")
        gcount=+1
    elif marks>=35 and marks<=49:
        print("pass")
        pcount=+1
    else:
        print("fail")   
        fcount=+1 
print(f"the no of student got excellent is :{ecount}") 
print(f"the no of student got good is :{gcount}")  
print(f"the no of student got pass is :{pcount}")  
print(f"the no of student got fail is :{fcount}")     

#5

word=input("enter a word :")
if len(word)<=3:
    print("short")
elif len(word)>=4 or len(word)<=6:
    print("medium")
else:
    print("long")        
print(len(word))

#8

total=0
bcount=0
rcount=0
pcount=0
lcount=0
for price in range (8):
    price=float(input("enter your price :"))
    total+=price
    if price < 500:
        print("Budget")
        bcount=+1
    elif price>=500 and price<=1999:
        print("Regular")
        rcount=+1
    elif price>=2000 and price<=4999:
        print("Premium")
        pcount=+1
    else:
        print("Luxury")  
        lcount=+1   
print(f"The no of product in budget is {bcount}")
print(f"The no of product in regular is {rcount}")      
print(f"The no of product in premium is {pcount}")
print (f"The no of product in luxury is {lcount}")
print(f"The average of all product is {price/8}")

13

total=0
for bill in range(6):
    bill=float(input("Enter the electricity bill :"))
    total+=bill
    if bill>=0 or bill<=100:
        a=bill*5
        print(a)
    elif bill>=100 or bill<=200:
        b=(bill-100)*7+100*5
        print(b)  
    elif bill>=200 or bill <=400:
        c=(bill-200)*10+100*7+100*5
        print(c)     
    else:
        d=(bill-400)*15+c    
        print(d)
if total < 1000:
    print("low")    
elif total > 1000 or total <3000:
    print("medium")  
elif total >3000:
    print("high")  
print(f"total bill is {total}")      

