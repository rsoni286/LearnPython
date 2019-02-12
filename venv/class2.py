# Program to take 5 input marks from user, add it it to list and print the sum of the marks
marks_list = []
i = 1
sum = 0

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
