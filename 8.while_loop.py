total=0
number=int(input("enter a number:"))
while number!=0:
    total+=number
    number=int(input("enter a number:"))
    print("total=",total)
    age=32
    while age>=18:
        print("you can vote")
        break
else:
        print ("you can vote")