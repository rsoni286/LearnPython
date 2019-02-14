# program of a terminal calculator

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print(
    "Welcome! \n \n Select an option \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n q for quitting")
ch = input()
while True:
    if ch == "1":
        print("Sum is :", a + b)
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))

        print(
            "Welcome! \n \n Select an option \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n q for quitting")
        ch = input()
    elif ch == "2":
        print("Difference is : ", a - b)
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))

        print(
            "Welcome! \n \n Select an option \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n q for quitting")
        ch = input()
    elif ch == "3":
        print("Product is : ", a * b)
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))

        print(
            "Welcome! \n \n Select an option \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n q for quitting")
        ch = input()
    elif ch == "4":
        print("Division is : ", a / b)
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))

        print(
            "Welcome! \n \n Select an option \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n q for quitting")
        ch = input()
    elif ch =="q":
        print("Quitting calculator")
        break
    else:
        print("Not a valid option")
        print(
            "Welcome! \n \n Select an option \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n q for quitting")
        ch = input()


# program to find if a year is leap or not

a = int(input("Enter the year : "))
if a % 4 == 0:
    print(a, "is a leap year")
else:
    print(a, "is not a leap year")


# program that checks if a form is valid

name = input("Enter your name : ")
age = input("Enter your age : ")
mob_num = input("Enter mobile number : ")


while True:
    if name =="":
        name = input("Name cannot be empty, enter your name again : ")
    elif name.isalpha() == False:
        name = input("Name can contain only alphabets, enter your name again : ")
    else:
        if age =="":
            age= input("age cannot be empty, enter your age again : ")
        elif age.isdigit() == False:
            age = input("Age can contain only numbers, enter your age again : ")
        elif int(age) < 19:
            age = input("Age can only be over 18, enter your age again : ")
        else:
            if mob_num =="":
                mob_num = input("Mobile number cannot be empty, enter your number again : ")
            elif mob_num.isdigit() == False:
                mob_num = input("Mobile Number can contain only numbers, enter your number again : ")
            else:
                print("Name = ", name , "\nAge = ", age, "\nMobile Number = ", mob_num)
                break



# program to print multiplication table

a = int(input("Enter number for which the table is required : "))

for i in range(1,11):
    print(a ,"*", i, "=", a*i )


# program to add 10 numbers using only one input statement to a list

list = []
i=1
while i <=10:
    a = input("Enter #" + str(i))
    if a.isnumeric():
        list.append(a)
        i = i+1
    else:
        print(a, "is not a number")

print("List of numbers = ", list)



# program to display only even number among a list

list_num = [12,4,35,98,99,13,52,67,1,22,76]
list_even =[]
for x in list_num:
    if x%2 == 0:
        list_even.append(x)

print("List of numbers = ", list_num)
print("List of even numbers = ", list_even)


# program to arrange data in list into different list according to their data type
list = ["a",12,1.89, 66,"rahul", 4.22, "rojan", "himalaya", 44,1.87]
list_int=[]
list_float=[]
list_string=[]
for x in list:
    if isinstance(x, int):
        list_int.append(x)
    elif isinstance(x,str):
        list_string.append(x)
    else:
        list_float.append(x)

print("The list with int :", list_int)
print("The list with float :", list_float)
print("The list with string :", list_string)


# program to remove a user desired number from a list
list = [23, 11, 69, 12, 34, 2, 6, 23, 43, 1233, 23, 222, 69, 23]
print("Old list is ", list)

num = int(input("Enter number to be removed"))

for x in list:
    if x == num:
        list.remove(x)
print("New list is", list)
