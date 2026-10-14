
#1
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")


#2
word = "skyline"
for ch in word:
    if ch in "aeiou":
        break
    print(ch)


#3
n = 2
while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2


#4
limit = int(input("Enter limit: "))
for i in range(1, limit + 1):
    if i == 7:
        break
    print(i, end=" ")


#5
word = input("Enter word: ")
target = input("Enter target character: ")
for ch in word:
    print(ch, end=" ")
    if ch == target:
        break


#6
nums = input("Enter numbers separated by spaces: ").split()
for num in nums:
    num = int(num)
    if num < 0:
        break
    print(num, end=" ")


#7
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)


#8
sentence = input("Enter sentence: ")
target = input("Enter target word: ")
words = sentence.split()
for word in words:
    if word == target:
        print("Found")
        break
else:
    print("Not found")


#9
for i in range(1, 7):
    if i == 4:
        continue
    print(i)


#10
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")


#11
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)


#12
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")


#13
word = input("Enter word: ")
target = input("Enter character: ")
for ch in word:
    if ch == target:
        continue
    print(ch, end="")


#14
marks = input("Enter marks separated by spaces: ").split()
for mark in marks:
    mark = int(mark)
    if mark < 40:
        continue
    print(mark, end=" ")


#15
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)


#16
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)


#17
word = input("Enter word: ")
count = 0
for ch in word:
    if ch in "aeiou":
        continue
    count += 1
print(count)


#18
for i in range(1, 4):
    print(i)
else:
    print("Done")


#19
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")


#20
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")


#21
for item in []:
    print("Inside")
else:
    print("Else block")


#22
nums = input("Enter numbers separated by spaces: ").split()
target = int(input("Enter target: "))
for num in nums:
    num = int(num)
    if num == target:
        print("Found")
        break
else:
    print("Not found")


#23
word = input("Enter word: ")
target = input("Enter character: ")
for ch in word:
    if ch == target:
        print("Character exists")
        break
else:
    print("Character missing")


#24
n = int(input("Enter number: "))
for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")


#25
values = [2, 4, 6, 8]
for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")


#26
# Case A
for x in range(3):
    continue
else:
    print("A")

# Case B
for x in range(3):
    break
else:
    print("B")

# Case C
for x in range(0):
    print(x)
else:
    print("C")


#27
word = input("Enter word: ")
for ch in word:
    if word.count(ch) >= 2:
        print(ch)
        break
else:
    print("No repeated character")


#28
for i in range(1, 4):
    if i == 2:
        pass
    print(i)


#29
x = 10
if x > 5:
    pass
print("Finished")


#30
for letter in "cat":
    pass
print("Loop ended")


#31
for i in range(1, 6):
    if i % 2 == 0:
        pass
    print(i)


#32
choice = int(input("Enter choice: "))
if choice == 1:
    print("Option 1 selected")
elif choice == 2:
    pass
else:
    print("Unknown option")
print("Program closed")


#33
# Program A
for i in range(1, 5):
    if i == 3:
        pass
    print(i)

# Program B
for i in range(1, 5):
    if i == 3:
        continue
    print(i)


#34
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


#35
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")


#36
nums = input("Enter numbers separated by spaces: ").split()
target = int(input("Enter target: "))
for num in nums:
    num = int(num)
    if num < 0:
        continue
    if num == target:
        print("Target found")
        break
else:
    print("Target not found")


#37
nums = input("Enter numbers separated by spaces: ").split()
for num in nums:
    num = int(num)
    if num == 0:
        continue
    if num == -1:
        break
    print(num, end=" ")
else:
    print("All values processed")


#38
for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")


#39
nums = input("Enter numbers separated by spaces: ").split()
for num in nums:
    num = int(num)
    if num < 0:
        continue
    if num % 4 == 0 and num % 6 == 0:
        print("Found:", num)
        break
else:
    print("No matching number")


#40
print("1. break")
print("2. continue")
print("3. for-else")
print("4. pass")
print("5. continue")
print("6. break")
print("7. for-else")
print("8. pass")
