#1.1
# stroka = input("строк без пробелов: ")
# tuple = tuple(stroka)
# print("Созданный кортеж:", char_tuple)

#1.2
# tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
# stroka = ''.join(tuple)
# print(stroka)

#1.3
# tuple_A = (1, 2, 3, 4, 5, 6, 7)
# tuple_B = (5, 6, 7, 9, 7, 1, 10)
# result = tuple_A[:len(tuple_A)//2] + tuple_B[len(tuple_B)//2:]
# print(result)

#1.4



#1.5
# tuple = (55, 6, 777, 70.0, '7', 'A')

# num_tuple = tuple(item for item in tuple if isinstance(item, (int, float)))
# str_tuple = tuple(item for item in tuple if isinstance(item, str))
# print(num_tuple)
# print(str_tuple)


#2.1

# stroka = input("введите строку без пробелов: ")
# result= set(stroka)
# print(result)

#2.2
# set_A = {1, 2, 3, 4, 5}
# set_B = {5, 7, 8, 9, 2, 10}

# result = set_A - set_B | set_B - set_A
# print(result)

#2.3
# set_A = {1, 2, 3, 4, 5}
# set_B = {5, 7, 8, 9, 2, 10}

# set_A = set_A - set_B
# print(set_A)

#2.4
# set_A = {1, 2, 3, 4, 7}
# set_B = {8, 7, 9, 4, 2, 0, 10}
# set_C = {4, 0, 1}

# set_A -= set_C  
# set_B |= set_C  

# print("new set_A =", set_A)
# print("new set_B =", set_B)
# print("new set_C =", set_C)


#2.5
# import random
# A = {1, 2, 3, 4, 5, 6}
# n = 3
# m = 5

# result = []
# while len(result) < m:
#     combination = random.sample(A, n)
#     if set(combination) not in result:
#         result.append(set(combination))

# print(result)

#3
# cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'),
#              ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

# manufacturer_models = {}
# for manufacturer, model in cars_list:
#     if manufacturer in manufacturer_models:
#         manufacturer_models[manufacturer].append(model)
#     else:
#         manufacturer_models[manufacturer] = [model]

# for manufacturer, models in manufacturer_models.items():
#     print(f"{manufacturer} {len(models)}")
#     for model in models:
#         print(f"- {model}")
