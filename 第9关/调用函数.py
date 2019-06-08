def menu(appetizer,course,*barbeque,dessert='绿豆沙'):
    print('一份开胃菜：'+appetizer)
    print('一份主菜：'+course)
    print('一份甜品：'+dessert)
    for i in barbeque:
        print('一份烤串：'+i)
        
menu('农家一碗香','油泼扯面','烤鸡翅','烤茄子','烤玉米')
