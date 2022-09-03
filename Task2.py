#2* #Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат. Где Х,Y,Z = 0 и 1
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            if not (x or y or z) == (not x and not y and not z):
                print(f'{x}{y}{z} = истинно')
                