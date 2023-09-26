#1.1
# a = [4,8,15,16,23,42]
# b = ""
# for num in a:
#     b += str(num) + " "
# print(b)

#1.2
# a= [4,8,15,16,23,42]
# for num in a:
#     print(num)
    
#1.3

# a = int(input("vvedite chislo: "))

# print(a)
# print(a + 1)
# print(a + 2)

# print(f" {a }\n,{a+1 }\n,{a+2}")


#1.4
# a=int(input("pervoe ch:"))
# b=int(input("vtoroe ch:"))
# c=int(input("trete ch:"))
# sum =a+b+c
# print(sum)

#1.5

# a = int(input("Enter the edge length of the cube:"))
# volume = a ** 3
# surface_area = 6 * (a ** 2)

# print("Volume =" , volume)
# print("Total surface area =", surface_area)

#2.1

# deti = int(input("chislo detei: "))
# mandariny = int(input("chislo mandarinov: "))

# a = mandariny // deti
# b = mandariny % deti
# print(a)
# print(b)

# #2.2
# number = int(input("Введите четырехзначное число: "))
# if len(number) != 4 or not number.isdigit():
#     print("введите четырехзначное число")
# else:
#     print(f"Цифра в тысячах: {number[0]}")
# #     print(f"Цифра в сотнях: {number[1]}")
# #     print(f"Цифра в десятках: {number[2]}")
# #     print(f"Цифра в единицах: {number[3]}")
# print("tysachi: ",number//1000)
# print("sotni: ",(number//100)%10)
# print("desyat:",(number//10)%10)
# print("edinisy: ", number%10)

#2.3
# population = int(input("количество жителей вселенной:"))
# if population % 2 == 0:
#     survivors = population // 2
# else:
#     survivors = (population + 1) // 2

# print("Количество выживших:", survivors)

#2.4
a = int(input("Enter a number: "))
result = a << 1
if result == 0:
    print("Warning: The result of << is zero.")
else:
    print("The result of << is " , result)

#2.5
# a = float(input("первое число: "))
# b = float(input("второе число: ")) 
# operation = input("Выберите операцию (+, -, *, /): ")

# if operation == "+":
#     result = a + b
#     print(f"{a} + {b} = {result}")
# elif operation == "-":
#     result = a - b
#     print(f"{a} - {b} = {result}")
# elif operation == "*":
#     result = a * b
#     print(f"{a} * {b} = {result}")
# elif operation == "/":
#     if b == 0:
#         print("ошибка")
#     else:
#         result = a / b
#         print(f"{a} / {b} = {result}")
# else:
#     print("Ошибка: Неверная операция")
