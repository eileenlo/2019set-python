def isPrime(p):
    for i in range(2, p):
        if p % i == 0:
            return False               
    return True


n = int(input("請輸入一個整數："))
if (n < 2):
    print("請輸入大於2的數字")
else:
    if (n % 2 == 0):
        print(n , "為偶數")
    else:
        print(n , "不是偶數")
    if(isPrime(n)):
        print(n , "為質數")
    else:
        print(n , "不是質數")


    