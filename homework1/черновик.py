# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# N = int(input("Введите N "))
# i=1
# dictionary = {N:3*N+1}
# while i<=N:
#     dictionary[i] = {i:3*i+1}
#     i+=1

   
# print(dictionary)


dictionary = {}
N = int(input("Введите число N "))

for i in range(1,N+1):
    dictionary[i] = 3*i+1

print(f'Последовательность 3n + 1, для n = {N}: {dictionary}')











# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
