import csv
import numpy as np
import matplotlib.pyplot as plt
# 中文亂碼處理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 開啟 CSV 檔案
with open('Drunk driving.csv', newline='') as csvfile:

    # 讀取 CSV 檔案內容
    rows = csv.DictReader(csvfile)

    totalA1_count = 0
    totalA2_count = 0
    year = np.array([])
    A1 = np.array([]) 
    A2 = np.array([]) 
    A1_hurt = np.array([]) 
    A2_hurt = np.array([]) 
    Dead = np.array([]) 

    # 以迴圈輸出每一列
    for row in rows:
        #A1 A2的總件數
        totalA1_count += int(row['A1'])
        totalA2_count += int(row['A2'])

        year = np.insert([row['year']], 0, year, axis=0)
        A1 = np.insert([int(row['A1'])], 0, A1, axis=0)
        A2 = np.insert([int(row['A2'])], 0, A2, axis=0)
        A1_hurt = np.insert([int(row['A1hurt'])], 0, A1_hurt, axis=0)
        A2_hurt = np.insert([int(row['A2hurt'])], 0, A2_hurt, axis=0)
        Dead = np.insert([int(row['dead'])], 0, Dead, axis=0)


# 敘述統計
A1_mean = np.mean(A1, axis = 0)         #平均數
A1_var = np.var(A1, axis = 0)           #變異數
A1_std = np.std(A1, axis = 0)           #標準差
A1_median = np.median(A1, axis = 0)     #中位數
print("A1件數\n平均數A1_mean：", A1_mean ,
        "\n變異數A1_var：" , A1_var ,
        "\n標準差A1_std：" , A1_std ,
        "\n中位數A1_median：" , A1_median , 
        "\n A1類發生事件總件數：" , totalA1_count)

A2_mean = np.mean(A2, axis = 0)
A2_var = np.var(A2, axis = 0)
A2_std = np.std(A2, axis = 0)
A2_median = np.median(A2, axis = 0)
print("A2件數\n平均數A2_mean：", A2_mean ,
        "\n變異數A2_var：" , A2_var ,
        "\n標準差A2_std：" , A2_std ,
        "\n中位數A2_median：" , A2_median ,
        "\n A2類發生事件總件數：" , totalA2_count)

A1hurt_mean = np.mean(A1_hurt, axis = 0)   
A1hurt_var = np.var(A1_hurt, axis = 0)    
A1hurt_std = np.std(A1_hurt, axis = 0)   
A1hurt_median = np.median(A1_hurt, axis = 0)
print("A1受傷人數\n平均數A1hurt_mean：", A1hurt_mean ,
        "\n變異數A1hurt_var：" , A1hurt_var ,
        "\n標準差A1hurt_std：" , A1hurt_std ,
        "\n中位數A1hurt_median：" , A1hurt_median)

A2hurt_mean = np.mean(A2_hurt, axis = 0)  
A2hurt_var = np.var(A2_hurt, axis = 0)   
A2hurt_std = np.std(A2_hurt, axis = 0)   
A2hurt_median = np.median(A2_hurt, axis = 0)
print("A2受傷人數\n平均數A2hurt_mean：", A2hurt_mean ,
        "\n變異數A2hurt_var：" , A2hurt_var ,
        "\n標準差A2hurt_std：" , A2hurt_std ,
        "\n中位數A2hurt_median：" , A2hurt_median)

dead_mean = np.mean(Dead, axis = 0)  
dead_var = np.var(Dead, axis = 0)   
dead_std = np.std(Dead, axis = 0)   
dead_median = np.median(Dead, axis = 0)
print("死亡人數\n平均數dead_mean：", dead_mean ,
        "\n變異數dead_var：" , dead_var ,
        "\n標準差dead_std：" , dead_std ,
        "\n中位數dead_median：" , dead_median)

#1
plt.plot(year, A1_hurt, label = 'A1類受傷人數',color = 'darkblue')
plt.plot(year, A2_hurt, label = 'A2類受傷人數',color = 'gold')
plt.plot(year, Dead, label = 'A1類死亡人數',color = 'deeppink')
plt.legend(loc = 'upper right')
plt.xlabel("年度")
plt.ylabel("人數")
plt.title("近年來因酒駕肇事的受傷/死亡人數", {"fontsize" : 12})
plt.figure()

#2
index = np.arange(10)+1
plt.bar(x = index,
        height = A1,
        width = 0.35,
        label = 'A1類發生次數',
        alpha = 0.9,
        color = 'greenyellow')
plt.bar(x = index+0.35,
        height = A2,
        width = 0.35,
        label = 'A2類發生次數',
        alpha = 0.9,
        color = 'tomato')  
plt.xticks(index+.3 / 2 ,year)
plt.legend(loc = 'upper right')
plt.xlabel("年度")
plt.ylabel("次數")
plt.title("各年發生事件之次數", {"fontsize" : 12})
plt.figure()

#3
count = np.array([totalA1_count,totalA2_count])

labels = np.array(['A1','A2'])
piecolor = np.array(['cornflowerblue' , 'gold'])
plt.pie(count,
        labels = labels, 
        autopct="%1.1f%%",
        pctdistance = 0.6,
        colors = piecolor)
plt.axis('equal')  
plt.title("A1類,A2類發生次數百分比", {"fontsize" : 12})
plt.show()