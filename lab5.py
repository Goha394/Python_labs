#1.1
# user_input = input()
# user_input = user_input.lower()  # Преобразуем все символы в строке в нижний регистр

# char_list = list(user_input)
# print("Created list is:", char_list)

#1.2
# user_input = input()
# user_list = user_input.lower()
# frequency_list = []

# for char in user_list:
#     if (char, user_list.count(char)) not in frequency_list:
#         frequency_list.append((char, user_list.count(char)))

# print(frequency_list)

#1.3
# user_input = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]

# list_vow = [item for item in user_input if item[0] in 'aeiouAEIOU']
# list_cons = [item for item in user_input if item[0] not in 'aeiouAEIOU']
# list_symb = [item for item in user_input if not item[0].isalpha()]

# print("list_vow =", list_vow)
# print("list_cons =", list_cons)
# print("list_symb =", list_symb)

#1.4
# def divide_into_quartiles(list_A):
#     sorted_list = sorted(list_A)
    
#     length = len(sorted_list)
#     q1_index = length // 4
#     q2_index = q1_index * 2
#     q3_index = q1_index * 3

#     q1 = sorted_list[:q1_index] + [0] * (q1_index - length % 4) 
#     q2 = sorted_list[q1_index:q2_index]
#     q3 = sorted_list[q2_index:q3_index]
#     q4 = sorted_list[q3_index:]

#     return q1, q2, q3, q4

# list= [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]
# q1, q2, q3, q4 = divide_into_quartiles(list)
# print("q1 =", q1)
# print("q2 =", q2)
# print("q3 =", q3)
# print("q4 =", q4)

#2.1
# student_name = 'Adam'
# assignment_scores = [82, 56, 44, 30]
# lab_scores = [78.20, 77.20]
# test_scores = [78, 77]

# student = { 'name': student_name,'assignment': assignment_scores,'test': test_scores,'lab': lab_scores}
# print(student)

#2.2

# student = {'name': 'Adam', 
#            'assignment': [82, 56, 44, 30], 
#            'test': [78, 77], 
#            'lab': [78.20, 77.20]
#            }

# check = {student['name']: 0}
# if len(student['assignment']) == 4:
#     check[student['name']] += 4

# if len(student['lab']) == 2:
#     check[student['name']] += 2

# if len(student['test']) == 2:
#     check[student['name']] += 2

# print(check)

#2.3
# student = {'name': 'Adam', 
#            'assignment': [82, 56, 44, 30], 
#            'test': [78, 77], 
#            'lab': [78.20, 77.20]}
# submission_rate = {'Adam': 8}

# if student['name'] in submission_rate and submission_rate[student['name']] >= 4:
#     final_grade = 0.3 * sum(student['assignment']) / 4 + 0.5 * sum(student['lab']) / 2 + 0.2 * sum(student['test']) / 2
#     student['final_grade'] = round(final_grade, 2)
# else:
#     student['final_grade'] = 0

# print(student)

#2.4
# student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
# student_data = {
#     'assignment': student['assignment'],
#     'test': student['test'],
#     'lab': student['lab'],
#     'final_grade': student['final_grade']
# }

# students = {student['name']: student_data}

# print(students)

#3
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]
stats = {}

for user_id, transaction_type in transactions:
    if user_id not in stats:
        stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': 0, 'lft': 0}

    stats[user_id][transaction_type] += 1

for user, user_stats in stats.items():
    transactions_count = [user_stats[1], user_stats[2], user_stats[3]]
    mft_index = transactions_count.index(max(transactions_count))
    lft_index = transactions_count.index(min(transactions_count))

    user_stats['mft'] = mft_index + 1
    user_stats['lft'] = lft_index + 1

for user, user_stats in stats.items():
    del user_stats[1]
    del user_stats[2]
    del user_stats[3]

print(stats)
