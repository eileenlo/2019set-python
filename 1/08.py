a = int(input("輸入1數:"))

#1
print("----------#1----------")
for i in range(a):
    for j in range(0,i+1):
        print("*",end = '')
    print('')

#2
print("----------#2----------")
for i in range(a):
    for j in range(i,a):
        print("*",end = '')
    print('')

#3
print("----------#3----------")
for i in range(a-1):
    for j in range(0,i+1):
        print("*",end = '')
    print('')
for i in range(a):
    for j in range(i,a):
        print("*",end = '')
    print('')

#4
print("----------#4----------")
for i in range(0,a-1):
    for k in range(a-i-1):
        print(' ',end = '')
    for j in range(i+1):
        print("*",end = '')
    print('')
for i in range(0,a):
    for j in range(i):
        print(" ",end = '')
    for k in range(a-i):
        print('*',end = '')
    print('')
    
#5
print("----------#5----------")
for i in range(1,a):  
    for j in range(i):
        print('*',end = '')
    for k in range(a*2-i*2-1):
        print(" ",end = '')
    for m in range(i):
        print('*',end = '')
    print('')
for i in range(a*2-1):
    print('*',end = '')
print('')
for i in range(1,a):
    for j in range(a-i):
        print('*',end = '')
    for k in range(i*2-1):
        print(" ",end = '')
    for m in range(a-i):
        print('*',end = '')
    print('')