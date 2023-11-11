#1
# def read_and_display_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 print(line) 

#     except file_not_found:
#         print(f"Файл {file_path} не найден.")

# read_and_display_file("text1.txt")

#2
# import random
# file_path = 'text1.txt' 
# try:
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
        # if lines:
        #     random_line = random.choice(lines)
          
        #     print(random_line.strip())
        # else:
        #     print("not founded")
            
# except file_not_found:
#     print("error")


#3
# def count_uppercase_characters(file_path):
   
#         with open(file_path, 'r') as file:
#             content = file.read()
#             uppercase_count = sum(1 for char in content if char.isupper())
#             return uppercase_count
   

# file_path = 'text1.txt'
# result = count_uppercase_characters(file_path)
# print(result)

#4
# def count_lines_without_d(filename):
#     count = 0
#     with open(filename, 'r') as file:
#         for line in file:
#             if not line.startswith('D'):
#                 count += 1
#     return count

# filename = 'text1.txt'  
# result = count_lines_without_d(filename)
# print(result)

#5
# def count_words_ending_with_f(file_path):
     
#     with open(file_path, 'r') as file:
#      content = file.read()
#     words = content.split()
#     count = sum(1 for word in words if word.lower().endswith('f'))
#     return count
   
# file_path = 'text1.txt' 
# result = count_words_ending_with_f(file_path)

# print(result)

#6
# def count_words(filename):
   
#         with open(filename, 'r') as file:
#             content = file.read()
#             words = content.split()

#             count_all = words.count("all")
#             count_none = words.count("none")

#             print("all",count_all)
#             print("none",count_none)

# count_words("text1.txt")


#7
# def count_word_frequency(file_path):
#     word_frequency = {}

#     with open(file_path, 'r') as file:
#         content = file.read()
#         words = content.split()

#         for word in words:
#             word = word.strip(".,!?\"'()[]{}")
#             word = word.lower()


#             if word in word_frequency:
#                 word_frequency[word] += 1
#             else:
#                 word_frequency[word] = 1

#     return word_frequency

# file_path = 'text1.txt'
# result = count_word_frequency(file_path)

# for word, frequency in result.items():
#     print(f'{word}: {frequency}')

#8
# def find_longest_word(file_path):

#         with open(file_path, 'r') as file:
#             words = file.read().split()
#             longest_word = max(words, key=len)
#             return longest_word
   
# file_path = 'text1.txt' 
# result = find_longest_word(file_path)

# print(f" длинное слово: {result}")

#9
# def correct_file(file_path):

#         with open(file_path, 'r') as file:
#             content = file.read()
#             corrected_content = content.replace('B', 'J')
#             print(corrected_content)


# correct_file('text1.txt') 

#10
def count_chars(file_path):
    count_a = 0
    count_b = 0

    with open(file_path, 'r') as file:
        for char in file.read().lower():
            if char == 'a':
                count_a += 1
            elif char == 'b':
                count_b += 1

    print(f'a={count_a}, b={count_b}')

count_chars('text1.txt')
