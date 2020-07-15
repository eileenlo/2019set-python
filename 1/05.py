import random
L = [i for i in range(10)]
for i in range(10):
    random.shuffle(L)
    avg = 0
    for j in range(6):
        avg = avg + L[j]
    avg = avg / 6
    print(L[0:6] , "average=", "%.2f" % avg)