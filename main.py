import random as r
import time


flag = True
start_range = int(input('Загадай начало отрезка!: '))
print(f"Твое число: {start_range}")
last_range = int(input('Загадай конец отрезка!: '))
print(f"Твое число: {last_range}")
new = r.randint(start_range, last_range)
while flag:
    print("Попробуй угадать!")
    answer = int(input())
    if answer == new:
        print('DA')
        break
    else:
        continue 
            

    
    


