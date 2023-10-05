#1
# a = int(input("четырёхзначное число: "))

# a1  = a // 1000
# a2 = (a // 100) % 10
# a3 = (a // 10) % 10
# a4 = a % 10

# if a1 + a4 == a2 - a3:
#     print("YES")
# else:
#     print("NO")

#2
# age = int(input("vvedite age: "))

# if age >= 18:
#     print("acception")
# else:
#     print("!not acception!")

#3
# a = int(input("первое число: "))
# b = int(input("второе число: "))
# c = int(input("третье число: "))

# if b - a == c - b:
#     print("YES")
# else:
#     print("NO")
#4
x1 = int(input("введите номер столбца первой клетки от 1 до 8: "))
y1 = int(input("введите номер строки первой клетки от 1 до 8: "))
x2 = int(input("введите номер столбца второй клетки от 1 до 8: "))
y2 = int(input("введите номер строки второй клетки от 1 до 8: "))

if x1 == x2 +1 or abs(y1-y2) <=1 :
    print("YES")
else:
    print("NO")

# 5
# x1 = int(input("введите номер столбца первой клетки от 1 до 8: "))
# y1 = int(input("введите номер строки первой клетки от 1 до 8: "))
# x2 = int(input("введите номер столбца второй клетки от 1 до 8: "))
# y2 = int(input("введите номер строки второй клетки от 1 до 8: "))

# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#     print("YES")
# else:
#     print("NO")

# 6
# a = int(input())
# b = int(input())
# c = int(input())

# average = a + b + c - min(a, b, c) - max(a, b, c)
# print(average)

# 7
# month = int(input("введите порядковый номер месяца: "))

# if month == 2:
#     print("28")
# elif month in (4, 6, 9, 11):
#     print("30")
# else:
#     print("31")

# 8
# weight = int(input("вес боксера: "))

# if weight <= 60:
#     print("light weight")
# elif weight <= 64:
#     print("first welterweight")
# elif weight <= 69:
#     print("welterweight")
# else:
#     print("!NE PODXODIT!")

# 9
# password = input()
# confirmation = input()

# if password == confirmation:
#     print("password accepted")
# else:
#     print("password not accepted")

# 10
# a = int(input())

# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 11
# a = int(input())
# b = int(input())
# if a < b:
#     print(a)
# else:
#     print(b)

# 12
# age = int(input("возраст: "))
# if age <= 13:
#     print("childhood")
# elif 14 <= age <= 24:
#     print("youth")
# elif 25 <= age <= 59:
#     print("maturity")
# else:
#     print("old age")

# 13
# a = int(input())
# b = int(input())
# c = int(input())

# if a == b == c:
#     print("Equilateral")
# elif a == b or b == c or a == c:
#     print("Isosceles")
# else:
#     print("Versatile")
