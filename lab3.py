# 1)
# a= int(input("enter a number: "))

# if a <= 0:
#     print("pls enter a positive integer")
# else:
#     i = 2
#     while i <= a:
#         print(i)
#         i += 2  
# 2)
a= int(input("enter a number: "))

factorial = 1
while a> 1:
    factorial *= a
    a -= 1
print("factorial is: ", factorial)


# 3)
# while True:
#     user_input = input("введите число: ")
    
#     if user_input == '42':
#         print("молодес,программа завершена")
#         break

# print("программа завершена")

# 4)
# str = input("Enter a word:")
# count = 0
# for letter in str:
#     if letter == 'a':
#         count += 1
# print(count)


# 5)
# n = int(input("enter the number:"))
# summa = 0

# while n > 0:
#     digit = n % 10
#     summa =+ digit
#     n = n // 10

# print("sum of digits:", summa)


# 6)
# f = int(input("количество чисел фибоначи: "))
# a, b = 0, 1

# while f > 0:
#     print(a, end=" ")
#     a, b = b, a + b
#     f -= 1


# 7)
#print(input("введите строку:")[::-1])

# 8)
# summa = 0

# while True:
#     a = input("введите число для выхода q: ")
    
#     if a == 'q':
#         break
    
#     num = int(a)
#     if num % 2 == 0:
#         continue
    
#     summa += num
# print(f"сумма нечетных чисел: {summa}")


# 9)
# import random
# secret_num = random.randint(1, 100)

# while True:
#     guess = int(input("угадай число 1 до 100: "))
    
#     if guess < secret_num:
#         print("слишком маленькое число.")
#     elif guess > secret_num:
#         print("слишком большое число.")
#     else:
#         print("молодес,угадал")
#         break

# 10)
# str = input()

# if str == str[::-1]:
#     print("string is palindrome")
# else:
#     print("not a palindrome :( ")

# 11)
# x = int(input("a number: "))
# y = int(input("Power:"))
# i = 1
# result = 1

# while i <= y:
#     result *= x
#     i += 1
# print(result)


# 12) 
# n= int(input())

# for number in range(2, n + 1):
#     prime = True

#     for divisor in range(2, int(number ** 0.5) + 1):
#         if number % divisor == 0:
#             prime = False
#             break

#     if prime:
#         print(number)


# 13)
# a = input("число: ")
# b = a[::-1]

# print("Число в обратном порядке:", b)

# 14)
# def prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def next_prime(num):
#     num += 1
#     while True:
#         if prime(num):
#             return num
#         num += 1

# while True:
#     try:
#         a = int(input())
#         if a == 0:
#             break

#         if prime(a):
#             print(f"{a} - это простое число.")
#         else:
#             next_prime = next_prime(a)
#             print(f"{a} не является простым. простое число: {next_prime}")

#     except ValueError:
#         print("Pls введите целое число")

#15
# def caesar_cipher(str, shift):
#     encrypted_text = ""
#     for char in str:
#         if char.isalpha():
#             offset = 65 if char.isupper() else 97
#             encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
#         else:
#             encrypted_text += char
#     return encrypted_text

# str = input("строка: ")
# shift = int(input("сдвиг на целое число: "))

# encrypted_text = caesar_cipher(str, shift)
# print("шифрованная строка:", encrypted_text)


print('a'.islower())
print('a'.isupper())