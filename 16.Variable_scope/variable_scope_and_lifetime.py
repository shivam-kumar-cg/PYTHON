#1

def fun():
    city="patna"
    print(city)
fun()   

#2

school="THE DIKSHA SCHOOL"
def name():
    print(school)
name() 

#3

if True:
    name="SHIVAM"
print(name) 

#4

for i in range(10):
    pass
print(i)

#5

"""scope means till where we can acces our variable for example :- local scope ,global scope ,nonlocal scope.

lifetime means how long a variable can be accesed across a module."""

#6

value = 100
def test():
    value = 200
    print(value)
test()
print(value)
    
#7

clicks = 0
def click():
    global clicks
    clicks += 1
    print(clicks)
click()

#8

"""name = "Asha"
def show():
    print(name)
    name = "Ravi"
show()

it will show local unbounded error beacause inside the function it knows that there is a variable name but it cannot be accesed."""

#9

def outer_fun():
    a=20
    def inner_fun():
        print(a)
    inner_fun()   
outer_fun()   

#10

def list_fun():
    z=[10,20,30,40,50]
    return z
print(list_fun())

#11

def outer_fun():
    a=0
    def inner_fun():
        nonlocal a
        a+=1
        print(a)
    inner_fun()
    inner_fun()
    inner_fun()
outer_fun()   

#12

x=1
def outer():
    x=2
    def inner():
        x=3
        print(x)
    inner()
    print(x)
outer()
print(x)  

#13

"""A normal for loop has no separate scope, so its variable remains accessible after the loop.Whereas a list comprehension has its own scope, so its variable does not overwrite an outer variable."""

#!4

def outer():
    x = 10
    def inner():
        return x

    return inner

result = outer()
print(result()) 


#15
"""Names like list, str, and sum should be avoided because they are built-in Python functions."""