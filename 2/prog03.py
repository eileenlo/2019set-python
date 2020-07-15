import random
L = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    random.shuffle(L)
    L1 = L[0:8]
    print(L1[0:8] , "max=%d, min=%d" %(max(L1),min(L1)))