def F(a):
    total = 1
    if a ==1:
        total = 1
    else:
        total = a * F(a-1)
    return total

     
        
n = int(input("please input:"))

#1
if n >= 1:
    print("%d!=%d" % ( n,F(n)))
else:
    print("請輸入大於等於1的數字")


#2
sum = 1
if n >= 1:
    for i in range(1,n+1):
        sum = sum * i
    print("%d!=%d" % ( n, sum ))
else:
    print("請輸入大於等於1的數字")