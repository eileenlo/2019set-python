n = int(input("please input:"))
if n >= 1:
    for i in range(n):
        print(' '*abs(n-i-1)+'*'*abs(i*2+1))
    for j in range(1,n):
        print(' '*j+'*'*((n-j)*2-1))
else:
    print("請輸入大於等於1的數字")