# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

# from random import randint
# numbers = []
# for i in range(int(input("введите количество чисел в списке "))):
#     numbers.append(randint(1, 10))
# print(numbers)
# sum = 0
# j=0
# while j< len(numbers):
#     if j % 2 !=0:
#         sum+=numbers[j]
#     j+=1
    
# print(f'сумма чисел стоящих на нечетных позициях = {sum}')


# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# from random import randint
# numbers = []
# for i in range(int(input("введите количество чисел в списке "))):
#     numbers.append(randint(1, 10))

# multiplication = []
# j=0
# digit=0

# while j< len(numbers)/2:
#     digit=numbers[j]*numbers[len(numbers)-1-j]
#     multiplication.append(digit)
#     j+=1
# print(f'{numbers} => {multiplication}')   




# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# numbers = []
# for i in range(int(input("введите количество чисел в списке "))):
#     numbers.append(random.uniform(1, 10))

# formated_numbers = [round(elem, 2) for elem in numbers]

# print (formated_numbers)

# fractional_part = []
# digit = 0
# for j in range(len(numbers)):
#     # digit=formated_numbers[j]%1
#     digit = round (numbers[j]%1, 2)
#     fractional_part.append(digit)
   

# min_digit=fractional_part[0]
# max_digit=fractional_part[0]

# for k in range(len(fractional_part)):
#     if min_digit>fractional_part[k]:
#         min_digit=fractional_part[k]
        
#     elif max_digit<fractional_part[k]:
#         max_digit=fractional_part[k]
        

# print(f'разница между максимальным и минимальным значением дробной части элементов списка равна: {max_digit - min_digit}')



# Написать программу преобразования десятичного числа в двоичное

# def dec_to_bin(n):
#     return int(bin(n)[2:])

# bin_number = dec_to_bin(int(input("введите десятичное число ")))
# print(bin_number)



# dec_number = int(input("введите десятичное число "))
# bin_number = ''
 
# while dec_number > 0:
#     bin_number = str(dec_number % 2) +bin_number
#     dec_number //= 2
 
# print(bin_number)

# НЕ РАБОТАЕТ.......
# def decToBin(n): 
#     if n==0: 
#         return ''
#     else:
#         return decToBin(n/2) + str(n%2)

# bin_number = decToBin(int(input("введите десятичное число ")))
# print(bin_number)