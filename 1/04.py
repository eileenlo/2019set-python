import random

max = 100
min = 0
ans = random.randint(min, max)
#print("ans =" , ans)
minput = int(input("請輸入數字( %d < ? < %d ):" % (min,max)))
while minput != ans:
    if min <= minput <= max:
        if minput < ans:
            min = minput + 1
        else:
            max = minput - 1
    else:
        print("輸入範圍錯誤,", end='')
    minput = int(input("請輸入數字( %d < ? < %d ):" % (min,max)))
else:
    print("bingo~~ ans =",ans)