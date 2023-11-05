#1.1
# def get_keys_with_value_true(dictionary):
#     return [key for key, value in dictionary.items() if value == True]
  
# my_dict = {
#     "a": True, "b": False, "c": True
# }

# result = get_keys_with_value_true(my_dict)
# print(result)

#1.2
# def get_unique_elements(input_list):
#     return [x for x in input_list if input_list.count(x) == 1]

# my_list = [1, 2, 3, 1, 2, 4]
# result = get_unique_elements(my_list)
# print(result)

#1.3
# def get_date_in_format(date):
#     return '.'.join(reversed(date.split('.')))

# input_date = "2023.10.23"
# output_date = get_date_in_format(input_date)
# print(output_date)  

#1.4
# def get_elements_with_no_more_than_two_occurrences(input_list):
#     result = []
#     for num in input_list:
#         if input_list.count(num) == 2 and num not in result:
#             result.append(num)
#     return result

# input_list = [1, 2, 3, 1, 2, 4]
# output = get_elements_with_no_more_than_two_occurrences(input_list)
# print(output)

#1.5
# def get_words_from_string(string):
#     return string.split()

# input_string = "This a string with a several words"
# result = get_words_from_string(input_string)
# print(result)


#2.1(6)
# def get_unique_elements_with_count(input_list):
#     return {i: input_list.count(i) for i in set(input_list)}

# my_list = [1, 2, 3, 1, 2, 4, 1, 2]
# result = get_unique_elements_with_count(my_list)
# print(result)

#2.2(7)
# def get_prime_numbers(n):
#     prime_numbers = []
#     for num in range(2, n + 1):
#         if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
#             prime_numbers.append(num)
#     return prime_numbers

# n = int(input())
# prime_numbers = get_prime_numbers(n)
# print(prime_numbers)

#2.3(8)
# def get_prime_numbers_in_list(numbers):
#     prime_numbers = []
#     for num in numbers:
#         if num >= 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 prime_numbers.append(num)
#     return prime_numbers

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
# result = get_prime_numbers_in_list(numbers)
# print(result)

#2.4(9)
# from datetime import datetime

# def get_difference_between_dates(date1, date2):
#     date_format = "%Y.%m.%d"
#     datetime_date1 = datetime.strptime(date1, date_format)
#     datetime_date2 = datetime.strptime(date2, date_format)
    
#     date_difference = abs((datetime_date2 - datetime_date1).days)
    
#     return date_difference

# date1 = "2023.10.23"
# date2 = "2023.10.25"

# difference = get_difference_between_dates(date1, date2)
# print(difference)

#3.1(10) +-+-+-+-
# def get_decimal_number_from_binary_string(binary_string):
#     decimal_number = int(binary_string, 2)
#     return decimal_number

# binary_input = "10110011"
# output_decimal = get_decimal_number_from_binary_string(binary_input)
# print(output_decimal)

#3.2(11)
# def is_expression_true(expression):
#     numbers = map(int, expression.split(', '))

#     for num in numbers:
#         if (num ** 0.5) % 1 != 0:
#             return False  

#     return True  

# input_expression = "4, 25, 81"
# result = is_expression_true(input_expression)
# print(result)  

#3.3(12)
# def sort_by_price(shopping_list):
#     return sorted(shopping_list, key=lambda x: x['price'])

# shopping_list = [
#     {"name": "Apple", "price": 100},
#     {"name": "Banana", "price": 50},
#     {"name": "Orange", "price": 20}
# ]

# sorted_list = sort_by_price(shopping_list)
# print(sorted_list)

#3.4(13)
# def get_words_starting_with_vowel(words):
#     vowels = ['a', 'e', 'i', 'o', 'u'] 
#     words_starting_with_vowel = [word for word in words if word[0].lower() in vowels]
    
#     return words_starting_with_vowel

# input_words = ["apple", "banana", "orange", "bear", "cat"]
# result = get_words_starting_with_vowel(input_words)
# print(result)
