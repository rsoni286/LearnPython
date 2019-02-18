
a=open("File.txt", "w")
text = input("add text here...write quit to exit")

while True:
    if text!="quit":
        a.writelines(text+"\n")
        text =input()
    elif text =="quit":
        break

print('Exiting program....Bye')
a.close()

class LowAgeError(Exception):
    def __init__(self):
        super(LowAgeError,self).__init__("Age should be greater than 18")

age = int(input("Enter the age"))
try:
    if age<18:
        raise LowAgeError
    else:
        print("Accepted")
except LowAgeError as e:
    print(e)

list = [x for x in range(2, 2500) if not [y for y in range(2, x) if (x % y == 0)]]
c = 0
for a in list:
    c = c + 1
    print(c,":",a)

