# Найти НОК двух чисел, НОК - наименьшее общее кратное...есть ощущение, что тут можно намного легче...

# first = int(input('Введите первое число '))
# second = int(input('Введите второе число '))
# maximum=first
# if first<second:
#     maximum = second

# multiple_first=[]
# multiple_second=[]

# for i in range(1,maximum+1):
#     digit = 0
#     digit = i*first
#     multiple_first.append(digit)


# for i in range(1,maximum+1):
#     digit = 0
#     digit = i*second
#     multiple_second.append(digit)


# result=list(set(multiple_first) & set(multiple_second))
# print(f'НОК чисел {first} и {second} = {min(result)}')



# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 
# не понимаю, что требуется в данной задаче сделать




# Составить список простых множителей натурального числа N

# N = int(input("Введите число N "))

# multipliers_N = []

# i=2

# while N>=2:
#     while N%i==0:
#         multipliers_N.append(i)
#         N=N/i
#     i=i+1
# print(multipliers_N)


# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# from random import randint
# numbers = []
# for i in range(int(input("введите количество чисел в списке "))):
#     numbers.append(randint(1, 10))
# print(numbers)
# unique_numbers = []
# unique = set(numbers)
# for i in unique:
#         unique_numbers.append(i)

# print(unique_numbers)



# + на тему файловой системы:
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

# from random import randint

# numbers=randint(5, 10)
# with open ('file.txt', 'w') as data:
#     for i in range(numbers):
#         data.write(str(randint(0,10)) + '\n')
# print(numbers)

# file_numbers = []
# with open('file.txt', 'r') as data:
#     for line in data:
#         file_numbers.append(int(line[:-1]))
# print(file_numbers)

# odd_numbers = []
# for i in file_numbers:
#     if i%2!=0:
#         odd_numbers.append(i)

# print(odd_numbers)