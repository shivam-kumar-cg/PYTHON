#1

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")
    case 4:
        print("You selected Sandwich")
    case _:
        print("Invalid Menu Choice")


#2

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Wi-Fi Selected")
    case 2:
        print("Bluetooth Selected")
    case 3:
        print("Mobile Data Selected")
    case 4:
        print("Airplane Mode Selected")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Setting")


#3

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Check Balance Selected")
    case 2:
        print("Withdraw Money Selected")
    case 3:
        print("Deposit Money Selected")
    case 4:
        print("Change PIN Selected")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Choice")


#4

signal = input("Enter signal: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")


#5

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Opening Profile")
    case 2:
        print("Opening Courses")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendance")
    case 5:
        print("Logging Out")
    case _:
        print("Invalid Choice")


#6

choice = int(input("Enter category: "))

match choice:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Category")


#7

choice = int(input("Enter service: "))

match choice:
    case 1:
        print("Opening Account Balance")
    case 2:
        print("Opening Mini Statement")
    case 3:
        print("Opening Fund Transfer")
    case 4:
        print("Opening Bill Payment")
    case 5:
        print("Opening Customer Support")
    case _:
        print("Invalid Service")


#8

choice = int(input("Enter show: "))

match choice:
    case 1:
        print("Morning Show Selected")
    case 2:
        print("Afternoon Show Selected")
    case 3:
        print("Evening Show Selected")
    case 4:
        print("Night Show Selected")
    case _:
        print("Invalid Show")


#9

weather = input("Enter weather: ").lower()

match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothes")
    case _:
        print("Unknown Weather")


#10

pay = input("Enter payment method: ").lower()

match pay:
    case "upi":
        print("UPI Payment Selected")
    case "card":
        print("Card Payment Selected")
    case "cash":
        print("Cash Payment Selected")
    case "wallet":
        print("Wallet Payment Selected")
    case _:
        print("Invalid Payment Method")


#11
ext = input("Enter extension: ").lower()

match ext:
    case "pdf":
        print("Document File")
    case "jpg" | "png":
        print("Image File")
    case "mp3":
        print("Audio File")
    case "mp4":
        print("Video File")
    case _:
        print("Unknown File Type")


#12

role = input("Enter role: ").lower()

match role:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest":
        print("Limited Access")
    case _:
        print("Invalid Role")


#13

day = int(input("Enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")


#14

priority = int(input("Enter priority: "))

match priority:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
        print("Urgent Priority")
    case _:
        print("Invalid Priority")


#15

level = int(input("Enter membership level: "))

match level:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("Invalid Membership")


#16

user = int(input("Enter user type: "))

match user:
    case 1:
        print("Student Selected")
        opt = int(input("Enter option: "))

        match opt:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid Option")

    case 2:
        print("Teacher Selected")
        opt = int(input("Enter option: "))

        match opt:
            case 1:
                print("Opening Students")
            case 2:
                print("Entering Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid User Type")


#17

acc = int(input("Enter account type: "))

match acc:
    case 1:
        print("Savings Account")
        op = int(input("Enter operation: "))

        match op:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")

    case 2:
        print("Current Account")
        op = int(input("Enter operation: "))

        match op:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")

    case _:
        print("Invalid Account Type")


#18

cat = int(input("Enter Category: "))

match cat:
    case 1:
        pro = int(input("Enter product: "))

        match pro:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid Product")

    case 2:
        pro = int(input("Enter product: "))

        match pro:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case _:
                print("Invalid Product")

    case _:
        print("Invalid Category")


#19
cat = int(input("Enter category: "))

match cat:
    case 1:
        food = int(input("Enter food: "))

        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid Food")

    case 2:
        food = int(input("Enter food: "))

        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case _:
                print("Invalid Food")

    case _:
        print("Invalid Category")


#20

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator: ")

match op:
    case "+":
        print("Result =", num1 + num2)
    case "-":
        print("Result =", num1 - num2)
    case "*":
        print("Result =", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid Operator")

#21

choice = int(input("Enter choice: "))
temp = float(input("Enter temperature: "))

match choice:
    case 1:
        ans = (temp * 9/5) + 32
        print("Temperature =", ans, "F")
    case 2:
        ans = (temp - 32) * 5/9
        print("Temperature =", ans, "C")
    case _:
        print("Invalid Choice")


#22

choice = int(input("Enter choice: "))
val = float(input("Enter value: "))

match choice:
    case 1:
        print(val * 1000, "meters")
    case 2:
        print(val / 1000, "kilometers")
    case 3:
        print(val * 1000, "grams")
    case 4:
        print(val / 1000, "kilograms")
    case _:
        print("Invalid Choice")


#23

acc = int(input("Enter account type: "))

match acc:
    case 1:
        print("Savings Account")
        amt = float(input("Enter amount: "))

        if amt > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case 2:
        print("Current Account")
        amt = float(input("Enter amount: "))

        if amt > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case _:
        print("Invalid Account Type")


#24

choice = int(input("Enter choice: "))

match choice:
    case 1:
        age = int(input("Enter age: "))

        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")

    case 2:
        print("View Result Selected")

    case 3:
        print("Exit Selected")

    case _:
        print("Invalid Choice")


#25

choice = int(input("Enter ticket type: "))
age = int(input("Enter age: "))

if age < 5:
    print("Free Entry")
else:
    match choice:
        case 1:
            print("Regular Ticket Selected")
        case 2:
            print("Premium Ticket Selected")
        case 3:
            print("VIP Ticket Selected")
        case _:
            print("Invalid Ticket Type")


#26

device = int(input("Enter device: "))

match device:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")


#27

dept = int(input("Enter department: "))

match dept:
    case 1:
        print("General Medicine Selected")
    case 2:
        print("Cardiology Selected")
    case 3:
        print("Orthopedics Selected")
    case 4:
        print("Pediatrics Selected")
    case 5:
        print("Emergency Selected")
    case _:
        print("Invalid Department")


#28

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Book Ticket Selected")
    case 2:
        print("Cancel Ticket Selected")
    case 3:
        print("Check PNR Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Choice")


#29

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Search Book Selected")
    case 2:
        print("Issue Book Selected")
    case 3:
        print("Return Book Selected")
    case 4:
        print("View Issued Books Selected")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Choice")


#30

status = input("Enter status: ").lower()

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid Order Status")   


#30

status = input("Enter order status: ")

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid Order Status")


#31

bank_type = int(input("Enter banking type: "))

match bank_type:
    case 1:
        print("Personal Banking")
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("Business Banking")
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Banking Type")


#32

user_type = int(input("Enter user type: "))

match user_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Marks")
            case 2:
                print("Opening Student Attendance")
            case 3:
                print("Opening Student Homework")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Enter Marks")
            case 2:
                print("Opening Teacher Attendance")
            case 3:
                print("Opening Assign Homework")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Child Marks")
            case 2:
                print("Opening Child Attendance")
            case 3:
                print("Opening Contact Teacher")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid User Type")


#33

transport = int(input("Select transport: "))

match transport:
    case 1:
        seat = int(input("Select seat: "))
        match seat:
            case 1:
                print("Economy Class Selected")
            case 2:
                print("Business Class Selected")
            case _:
                print("Invalid Seat")

    case 2:
        seat = int(input("Select seat: "))
        match seat:
            case 1:
                print("Sleeper Class Selected")
            case 2:
                print("AC Class Selected")
            case _:
                print("Invalid Seat")

    case 3:
        seat = int(input("Select seat: "))
        match seat:
            case 1:
                print("Ordinary Bus Selected")
            case 2:
                print("Volvo Bus Selected")
            case _:
                print("Invalid Seat")
    case _:
        print("Invalid Transport")


#34

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Starting Game")
    case 2:
        print("Loading Game")
    case 3:
        setting = int(input("Select setting: "))
        match setting:
            case 1:
                print("Sound Settings Opened")
            case 2:
                print("Graphics Settings Opened")
            case 3:
                print("Controls Settings Opened")
            case _:
                print("Invalid Setting")
    case 4:
        print("Exiting Game")
    case _:
        print("Invalid Choice")


#35

category = int(input("Select category: "))

match category:
    case 1:
        food = int(input("Select food: "))
        match food:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Food")

    case 2:
        food = int(input("Select food: "))
        match food:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Food")

    case 3:
        food = int(input("Select food: "))
        match food:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Food")

    case 4:
        food = int(input("Select drink: "))
        match food:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Drink")
    case _:
        print("Invalid Category")


#36 Digital Payment Application
payment = int(input("Select payment type: "))

match payment:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Payment Type")


#37

subject = int(input("Select subject: "))

match subject:
    case 1:
        course = int(input("Select course: "))
        match course:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Course")

    case 2:
        course = int(input("Select course: "))
        match course:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Course")

    case 3:
        course = int(input("Select course: "))
        match course:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Course")
    case _:
        print("Invalid Subject")


#38

device = int(input("Select device: "))

match device:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Engine Start Selected")
            case 2:
                print("Engine Stop Selected")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Playing Music")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Song")
            case 4:
                print("Previous Song")
            case _:
                print("Invalid Option")

    case 4:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Device")


#39 

user_type = int(input("Enter user type: "))

match user_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Employee Profile")
            case 2:
                days = int(input("Enter leave days: "))
                if days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("Opening Employee Salary")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Team")
            case 2:
                print("Opening Approve Leave")
            case 3:
                print("Opening Reports")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid User Type")


#40

role = int(input("Enter role: "))
match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Students")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Fees")
            case 2:
                print("Opening Admissions")
            case 3:
                print("Opening Notices")
            case 4:
                print("Opening Departments")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Role")
