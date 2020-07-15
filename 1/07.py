cm = eval(input("請輸入身高(cm)："))
kg = eval(input("請輸入體重(kg)："))

cm=cm/100
bmi = kg/cm**2
print(bmi)

if bmi < 18.5:
    print("體重過輕")
elif 18.5 <= bmi < 24:
    print("健康體位")
elif 24 <= bmi < 27:

    print("過重")
elif 27 <= bmi <30:
    print("輕度肥胖")
elif 30 <= bmi <35:
    print("中度肥胖")
else:
    print("重度肥胖")