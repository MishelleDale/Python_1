# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import os

os.system('cls')
print('проверить предикат ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \n')

this_predicat = True #считаем, что выражение истинно


print('таблица истинности')
print('  X   |  Y   |  Z   | ¬(X ⋁ Y ⋁ Z) | ¬X ⋀ ¬Y ⋀ ¬Z | итог ')
print('------------------------------------------------------------')

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            left_part = not (x or y or z)
            right_part = not x and not y and not z
            this_predicat = (left_part == right_part)
            print('%6s|%6s|%6s|%14s|%14s|%5s' % (x, y, z, left_part, right_part, (left_part == right_part)))

print('------------------------------------------------------------')

if this_predicat :
    print('выражение - истинно')
else :
    print('выражение - ложно')

