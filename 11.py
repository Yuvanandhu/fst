try:
    value1=int(input("enter fst value :"))
    value2=int(input("enter sec value :"))
    result=value1/value2
    print(result)
except:
    print("cant be divide zero") 
try :
    evennumbers=[2,4,6,8,10,12,14] 
    print(evennumbers[8])
except IndexError:
        print("index out of bound")