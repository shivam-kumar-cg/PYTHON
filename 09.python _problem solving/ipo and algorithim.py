#question1
#IPO
#input = two number
#process = addition 
#output = print sum


#Algorithm
#1.start
#2.Read first number
#3.Read second number
#4.Add the two number 
#5.Store the result 
#6.Diaplay the result
#7.stop

#Test Case1
#input
number1=9
number2=2
#process
sum=9+2
#output
11

#TEatCase2
#input
number1=27
number2=29
#process
sum=27+29
#output
56


#python 
number1=int(input("Enter 1"))
number2=int(input("Enter"))
sum=number1+number2
print(sum)




#question2
#IPO 
#input = number
#process = check if number%2==0 even 
#output = print(even)

#Algorithm
#1.start
#2.read number
#3.Divide the number by 2 and check the remainder
#4.If the remainder is 0, print even
#5.esle odd number
#6.print(ontput)
#7.stop

#
#Test Case1
#input
number=9
#process
9%2=1
#output
# odd


#Test Case2
#input
number=26
#process
26%2==0
#output
# even

#Python 
number=int(input("enter a number :"))
if number%2==0:
    print("Even")
else:
    print("ODD")






#question3
#IPO
#input = three number
#process = if A>B and A>C A is greater
#output= which is greater

#Algorithm
#start
#read nthreee number
#if A>B and A>C A is greater
#output a
#stop
#Test Case1
#input
number1=9
number2=2
number3=8
#process
#9 is greater then 2and8
#output
#9
#Test Case2
#input
number1=1
number2=2
number3=3
#process
#3 greater then 1 and 2
#output

#python
number1=int(input("Enter first number: "))
number2=int(input("Enter second number :"))
number3=int(input("Enter third number : "))
if number3>number1 and number3>number2:
    print("number3 is greater ")
elif number2>number1 and number2>number3:
    print("number2 greater ")
else:
    print('number1 is greater')



#question4
#IPO
#input = person age
#process = if age>18 eligible
#output = print eligible

#Algorithm 
#start
#read person age 
#if age>=18 eligible
#else Not eligible to vote
#print eligible not eligible

#python
AGE=int(input("Enter your AGE"))
if AGE>=18:
    print("eligible")
else:
    print("not eligible")






#question5
#IPO
#input = price
#process = if price greater then equle to 2000 give 20% discount
#output = final pricee


#Algorithm
#start
#read price
#if Discount = price * 20 / 100

#Final price = price - discount
#print output


#Test Case1
#input
#price=1000
#process
#final  price=1000
#output
#1000

#Test Case2
#input
#price=2000
#process
#discount=(20/100)*2000 =400
#final=price-discount
#output
#160


#python
price=int(input("Enter item "))

if price>=2000:
    discount=price*20/100
    final=price-discount
    print(final)
else:
    print(price)






#question6
#IPO
#Input = Three subject marks
#Process = calculate average and check whether average ≥ 40
#Output = Average and Pass or Fail
#Algorathm
# Start.
#Take three subject marks as input.
#Add the three marks.
#Divide the total by 3 to calculate the average.
#If the average is greater than or equal to 40, print Pass.
#Otherwise, print Fail.
#Print the average.
#Stop.

#Test Case 1:
#Total = 50 + 60 + 70 = 180
#Average = 180 / 3 = 60
#60 ≥ 40 → Pass




#Test Case 1:
#Total = 50 + 60 + 70 = 180
#Average = 180 / 3 = 60
#60 ≥ 40 → Pass



mark1 = float(input("Enter first subject marks: "))
mark2 = float(input("Enter second subject marks: "))
mark3 = float(input("Enter third subject marks: "))

average = (mark1 + mark2 + mark3) / 3

print("Average:", average)

if average >= 40:
    print("Pass")
else:
    print("Fail")