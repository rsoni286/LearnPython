# Program to take 5 input marks from user, add it it to list and print the sum of the marks
marks_list = []
i = 1
sum = 0

if __name__ == "__main__":
    while (i <= 5):
        mark = int(input("Enter the mark of subject # " + str(i)))
        marks_list.append(mark)
        sum = sum + mark
        i = i + 1
    print('Marks of the subjects are :' ,marks_list)
    print("Total marks = ", sum)

    #Program to take a string from user and ask which string needs to be counted

    input_string = input("Enter the string :")
    check_string = input("Enter the string or character to be counted :")
    print(input_string.count(check_string))


    # program to get maximum and minimum values and print them

    list = [4,55,1,0,33,87,21,44,21]
    print("The list is ", list)
    print('The maximum number is ', str(max(list)), " and the minimum is ", str(min(list)))

    # program to replace a word from the string and convert it into uppercase
    input_string = input("Enter the string :")
    check_string = input("Enter the word to be replaced :")
    replacing_string = input("Enter the word which replaces the old word :")
    print("The new capitalized string is : ", input_string.replace(check_string, replacing_string).upper())


    #program to arrange data in list into different list according to their data type
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


