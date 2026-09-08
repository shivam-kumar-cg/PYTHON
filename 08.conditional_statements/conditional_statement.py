#1
number=int(input("enter a number :"))
if number>10:
    print("Greater than 10")

#2
age=int(input("enter your age :"))
if age>=18:
    print("adult")

#3
number=int(input("enter a number :"))
if number>=0:
    print("positive")

#4
marks=int(input("enter your marks :"))
if marks>=40:
    print("pass")


#5
number=int(input("enter a number :"))
if number==0:
    print("Zero")


#6
number=int(input("enter a number :"))
if number>0:
    print("positive")
else:
    print("not positive")    
    
#7
age=int(input("enter your age :"))
if age>=18:
    print("Adult")
else:
    print("minor")

#8
number=int(input("enter a number :"))
if number%2==0:
    print("even")
else:
    print("odd")

#9
marks=int(input("enter your marks :"))
if marks>=40:
    print("pass")
else:
    print("fail")        

#10
number1=int(input("enter a number :"))
number2=int(input("enter another number :"))
if number1>number2:
    print("happy")
else:
    print("sad")                           

#11
marks=int(input("enter your marks :"))
if marks>=90 and marks <= 100:
    print("A")
elif marks>=75 and marks<=89:
    print("B")
elif marks>=40 and marks<=59:
    print("C")
elif marks<40:
    print("F")

#12
number=int(input("enter a number :"))
if number==0:
    print("zero")
elif number>0:
    print("positive")
else:
    print("negative")   


#13

number=int(input("Enter a number from 1 to 5 :"))
if number==1:
    print("Monday")
elif number==2:
    print("Tuesday")
elif number==3:
    print("Wednesday")
elif number==4:
    print("Thrusday")
elif number==5:
    print("Friday")  
else:
    print("Enter a valid no.")                  

     
#14
marks=int(input("Enter your Marks :"))
if marks>=90 and marks<=100:
    print("Excellent")
elif marks>=80 and marks<=89:
    print("good")
elif marks>=70 and marks<=79:
    print("pass")
elif marks<=69 and marks>=0:
    print("fail")
else:
    print("enter a valid input")                

#15
number=int(input("enter a number between 1 to 3 :"))
if number==1:
    print(1)
elif number==2:
    print(2)
elif number==3:
    print(3)        
else:
    print("other")

#16
Age=int(input("Enter your age :"))
if Age>=18:
    if Age<=60:
        print("between 18 and 60")

#17
Marks=int(input("enter your marks :"))
if Marks>=40:
    if Marks>=75:
        print("Good")
    else:
        print("pass")    

#18
number=int(input("Enter a number :"))
if number>0:
    if number>100:
        print("greater than 100")
    else:
        print("less than 100 or equal to 100")    

#19
Age=int(input("Enter your Age :"))
if Age>=18:
    if Age<=60:
        print("you are selected")
    else:
        print(" you are not selected")        

#20
number=int(input("enter a number :"))
if number!=0:
    if number>0:
        print("positive")
    else:
        print("negative")

#21
age=int(input("enter your age :"))
marks=int(input("enter your marks :"))
if age>=18 and marks>=40:
    print("eligible")
else:
    print("not eligible")
    
#22
number=int(input("enter a number :"))
if number<10 or number>100:
    print("Special number")
else:
    print("try again")    

#23
age=int(input("enter your age :"))
has_id=bool(input("enter True if you have id or False if not :"))
if age>=18 and has_id==True:
    print("allowed")

#24
a=int(input("enter a number :"))
b=int(input("enter another number :"))
if a>10 and b>10:
    print("both no.greater than 10")

#25
number=int(input("enter a number :"))
if number<0 or number>100:
    print("valid number")
else:
    print("invalid no.")    

#26
is_closed = False

if not is_closed:
    print("Open")

#27
number=int(input("enter a number :"))
if number>10 and number<50:
    print("valid number")
else:
    print("try again")    

#28
number=int(input("enter a number :"))
if number>10 or number<50:
    print("valid number")
else:
    print("invalid number")    

#29
is_student=bool(input("if student type true else type false :"))
has_id=bool(input("if you have id type true else type false :"))
has_ticket=bool(input("if you have ticket type true else type false :"))
if is_student==bool(True) and has_id==bool(True) and has_ticket==bool(True):
    print("allowed")
else:
    print("false")    

#30
age=int(input("enter your age :"))
marks=int(input("enter your marks :"))
has_id=bool(input("if you have id type true else type false :"))
if age>=18 and marks>=40 and has_id==bool(True):
    print("allowed")
else:
    print("not allowed")
