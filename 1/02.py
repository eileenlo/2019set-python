n = int(input("請輸入一個整數："))
if (n < 0):
    print("請輸入大於0的數字")
else:
    a=0
    for i in range(n+1):
        a = a + i
    print(n , "!=" , a)