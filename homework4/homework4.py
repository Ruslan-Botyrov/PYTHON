# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]

# from itertools import combinations

# number_list = [1, 5, 2, 3, 4, 6, 1, 7]
# print(number_list)
# long = len(number_list)
# result = []
# while long > 0:
#     temp = combinations(number_list, long)
#     for i in list(temp):
#         count = 0
#         for j in range(1,len(i)):
#             if i[j]<i[j-1]:
#                 count+=1
#         if count ==0: 
#             result.append(i)
#     if len(result)==0: 
#         long-=1
#     else: 
#         print(result[0])
#         break    

        

# Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию.

# from random import randint

# numbers=randint(5,10)
# with open ('file.txt', 'w') as data:
#     for i in range(numbers):
#         data.write(str(randint(0,10)) + '\n')
# print(numbers)

# file_numbers = []
# with open('file.txt', 'r') as data:
#     for i in data:
#         file_numbers.append(int(i))
# print(file_numbers)

# for i in range(numbers-1):
#     for j in range(numbers-i-1):        
#         if file_numbers[j]>file_numbers[j+1]:
#             file_numbers[j], file_numbers[j+1] = file_numbers[j+1] , file_numbers[j]


# print(file_numbers)

# либо через sorted
# sorted_file_numbers = sorted(file_numbers)
# print(sorted_file_numbers)




#  найти триплеты и просто выводить их на экран. 
# Триплетом называются три числа, которые в сумме дают 0. 
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования). 

# file_numbers = []
# with open('1Kints.txt', 'r') as data:
#     for i in data:
#         file_numbers.append(int(i))
# print(file_numbers)

# for i in file_numbers:
#     for j in file_numbers:
#         for k in file_numbers:
#             if i + j +k == 0:
#                 print(f'{i} + {j} + {k} = 0')
