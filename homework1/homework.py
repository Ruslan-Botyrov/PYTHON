# ЗАДАЧА 1 Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

# N = int(input("Введите число N "))
# result = []
# i=1
# digit=1
# result.append(digit)
# while i<N:
#     digit = digit * -3
#     result.append(digit)
#     i=i+1
    
# print(result)





# ЗАДАЧА 2 Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# dictionary = {}
# N = int(input("Введите число N "))

# for i in range(1,N+1):
#     dictionary[i] = 3*i+1

# print(f'Последовательность 3n + 1, для n = {N}: {dictionary}')




# ЗАДАЧА 3 Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.



# def split(row):
#     return [char for char in row]
# first = input('введите первую строку ')
# second = input('введите вторую строку ')


# first_split = split(first)
# second_split = split(second)
# result = []

# for i in second_split:
#     if i in first_split:
#         result.append(i)

# print(len(result))

# print(sum(1 for i in first if i in second))




# ЗАДАЧА 4 Подсчитать сумму цифр в вещественном числе.

# n = input("Введите вещественное число n ")
# print()
# import re
# res_n = re.sub("[.|,|-]","",n)
# # print(res_n)
# sum=0
# for i in res_n:
#     sum+=int(i)
# print('сумма цифр введенного числа = ', sum)





# ЗАДАЧА 5 Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

# N = int(input("Введите число N "))
# i=0
# result = []
# digit=1
# while i<N:
#     digit = digit * (i +1)
#     result.append(digit)
#     i+=1

# print(result)

