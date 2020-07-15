def F(n):
    if (n == 0 or n ==1):
        return n
    else:
        return F(n-1) + F(n-2)


a = int(input("請輸入一個整數："))
print("fib(" , a , ") = " , F(a))