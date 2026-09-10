# #1
# number=int(input("enter a number :"))
# if number>0:
#     print("positive")
# elif number==0:
#     print("zero")
# elif number<0:
#     print("negative")
# else:
#     print("enter valid number")            

# #2
# number=int(input("enter a number :"))
# if number==0:
#     print("zero")
# elif (number%2)==0 and (number/2)>0:
#     print("Positive even")
# elif (number%2)==0 and (number/2)<0:
#     print("negative even")
# elif (number%2)==1 and (number/2)>0:
#     print("positive odd")
# elif (number%2)==1 and (number/2)<0:
#     print("negative odd")
# else:
#     print("enter valid no.")    

# #3
# a=int(input("enter a number :"))
# b=int(input("enter another number :"))
# if a==b:
#     print("both are equal")
# elif a>b:
#     print(a)
# elif a<b:
#     print(b)        

# #4
# a=int(input("enter first number :"))
# b=int(input("enter second number :"))
# c=int(input("enter third number :"))
# if a<b and a<c:
#     print(a)
# elif a>b and b<c:
#     print(b)
# elif a>c and b>c:
#     print (c)   
# elif a==b==c:
#     print("all are equal")
# else:
#     print("enter valid data") 

# #5
# a=int(input("enter first number :"))
# b=int(input("enter second number :"))
# c=int(input("enter third number :"))   
# if a>b and a>c:
#     print(f"{a} is the greatest")
# elif a<b and b>c:
#     print(f"{b} is the greatest")
# elif a<c and b<c:
#      print(f"{c} is the greatest")        
# elif a==b==c:
#     print ("all are equal")     

# #6
# number=int(input("enter a number :"))
# if (number%5)==0 and (number%11)==0:
#     print("divisible by 5 and 11")
# elif (number%5)==0 and (number%11)!=0:
#     print("divisible by 5")
# elif (number%5)!=0 and (number%11)==0:
#     print("divisible by 11")
# elif (number%5)!=0 and (number%11)!=0: 
#     print("divisible by neither 5 nor 11")    

# #7
# number=int(input("enter a number :")) 
# if (number%3)==0 and (number%7)==0:
#     print("divisible by 3 and 7")
# elif (number%3)==0 and (number%7)!=0:
#     print("divisible by 3")
# elif (number%3)!=0 and (number%7)==0:
#     print("divisible by 7")
# elif (number%3)!=0 and (number%7)!=0: 
#     print("divisible by neither 3 nor 7")      

# #8
# marks=int(input("enter your marks :"))
# if marks<0 or marks>100:
#     print("invalid marks")
# elif marks>=40:
#     print("pass")
# elif marks<40:
#     print("fail")               

# #9
# marks=int(input("enter your marks :"))  
# if marks>=90 and marks<=100:
#     print("A")
# elif marks>=80 and marks<=89:
#     print("B")
# elif marks>=79 and marks<=70:
#     print("C")
# elif marks>=60 and marks<=69:
#     print("D")
# elif marks>=59 and marks<=40:
#     print("F")        
# elif marks<0 or marks>100:
#     print("invalid marks")                

# #10
# age=int(input("enter your age :"))
# if age<0 or age>120:
#     print("invalid age")       
# elif age<18:
#     print("cannot vote")
# elif age>=18:
#     print("can vote") 

# #11
# year=int(input("enter a year :"))
# if(year%400)==0 or(year%4)==0 and (year%100)!=0:
#     print(f"{year} is a leap year") 
# else:
#     print(f"{year} is not a leap year")


# #14
# selling_price=int(input("enter the selling price :"))
# cost_price=int(input("enter the cost price :"))
# if selling_price>cost_price:
#     print("profit")
# elif cost_price>selling_price:
#     print("loss")    
# elif cost_price==selling_price:
#     print("neither loss nor profit")

# #15
# selling_price=int(input("enter the selling price :"))
# cost_price=int(input("enter the cost price :"))   
# if selling_price>cost_price:
#     print((selling_price-cost_price)*100/cost_price)
# elif selling_price<cost_price:
#     print((cost_price-selling_price)*100/cost_price)

# #16     
# unit=int(input("enter the bill input :"))
# if unit<=100:
#     print(unit*5)
# elif unit>100 and unit<=200:
#     print((unit-100)*7+(100*5))       
# elif unit>200:
#     print((unit-200)*10+(100*7)+(100*5))

# #17
# first = float(input("enter a number :"))
# second = float(input("enter a number :"))
# operator = input("plz enter the operation"
# "such as:"
# "+"
# "-"
# "*"
# "/")

# if operator == '+':
#     print(first + second)
# elif operator == '-':
#     print(first - second)
# elif operator == '*':
#     print(first * second)
# elif operator == '/':
#     if second == 0:
#         print("Division by zero is not allowed")
#     else:
#         print(first / second)

# #18
# temperature = float(input("enter the tempreature :"))

# if temperature < 0:
#     print("Freezing")
# elif temperature <= 15:
#     print("Very Cold")
# elif temperature <= 25:
#     print("Cold")
# elif temperature <= 35:
#     print("Normal")
# else:
#     print("Hot")

# #19
# number = int(input("enter a number :"))

# if number < 0:
#     print("Negative")
# elif number <= 10:
#     print("between 0 and 10")
# elif number <= 50:
#     print("between 11 and 50")
# elif number <= 100:
#     print("between 51 and 100")
# else:
#     print("Above 100")

# #20
# a = int(input("enter a length of triangle :"))
# b = int(input("enter another length of triangle :"))
# c = int(input("enter last length of triangle :"))

# if (a + b) > c and (a + c) > b and (b + c) > a:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")

# #21
# a = int(input("enter a length of triangle :"))
# b = int(input("enter another length of triangle :"))
# c = int(input("enter last length of triangle :"))

# if a + b > c and a + c > b and b + c > a:
#     if a == b and b == c:
#         print("Equilateral")
#     elif a == b or b == c or a == c:
#         print("Isosceles")
#     else:
#         print("Scalene")
# else:
#     print("Invalid triangle")



      