# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input(f'Введите значение "x" ->  '))
y = int(input(f'Введите значение "y" ->  '))
z = int(input(f'Введите значение "z" ->  '))
first = not(x or y or z)
second = not x and not y and not z
result = first == second
if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')