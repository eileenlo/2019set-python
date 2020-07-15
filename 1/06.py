def compareTotal(*numbers , compare = 0):
    total = 0
    for i in numbers:
        total = total + i
   
    if (total == compare):
        print("總和:" , total ,"兩個相等")
    elif (total < compare):
        print("總和:" , total ,"比" ,compare , "小")
    else:
        print("總和:" , total ,"比" ,compare , "大")

compareTotal(1,2,3)
compareTotal(1,2,3 ,compare = 3)
compareTotal(1,2,3 ,compare = 6)
compareTotal(1,2,3 ,compare = 9)
compareTotal(1,2,3,6,4,3,2 ,compare = 14)