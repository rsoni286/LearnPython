# # # data = {"name": "Rahul",
# # #         "age": 19,
# # #         "place": "Biratnagar",
# # #         "courses": ["python", "android", "frontend", "backend"],
# # #         "marks": {"python": 98,
# # #                   "android": 97,
# # #                   "frontend": 70,
# # #                   "backend": 90
# # #                   }
# # #         }
# # #
# # # # try:
# # # #     list = data["courses"]
# # # #     for i in list:
# # # #         print(i)
# # # #
# # # #     mark_dict = data["marks"]
# # # #     mark_android = mark_dict["android"]
# # # #     print("Android :", mark_android)
# # # #
# # # # except TypeError:
# # # #     print("List not found")
# # #
# # #
# # # if "marks" in data:
# # #     print("marks is a key")
# # #
# # # for x in data.values():
# # #     if x == "Rahul":
# # #         print("Found Rahul\n")
# # #
# # # for x, y in data.items():
# # #
# # #     if type(y) == dict:
# # #         print("\n" + x, ":")
# # #         for z, w in y.items():
# # #             print(z, '=', w)
# # #     elif type(y) == list:
# # #         print("\n" + x, ":")
# # #         for z in y:
# # #             print(z)
# # #     else:
# # #         print(x, y)
# #
# # class name:
# #     def __init__(self, name, age, roll):
# #         self.name = name
# #         self.age = age
# #         self.roll = roll
# #
# #     def display(self):
# #         print(self.name)
# #         print(self.age)
# #         print(self.roll, "\n")
# #
# #
# # class student(name):
# #     def __init__(self, degree, name):
# #         self.degree = degree
# #         self.name = name.name
# #         self.age = name.age
# #         self.roll = name.roll
# #
# #     def display(self):
# #         print(self.name)
# #         print(self.degree)
# #
# #
# # n = name('Rahul', 12, 1)
# # s = student('CSIT', n)
# #
# # n.display()
# # s.display()
#
#
# def capital(c):
#     return c.upper()
#
# def iseven(a):
#     if a%2==0:
#         return True
#     else:
#         return False
#
# list1=[1,2,3,4,5,6,7,8,9,34]
# list_capital= list(filter(iseven,list1))
# print(list_capital)