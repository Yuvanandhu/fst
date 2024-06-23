class vehicle:
    def wheels(self,bike=None,car=None,bus=None):
        if bike!=None and car!=None and bus!=None:
            return bike,car,bus
        elif bike!=None:
            return bike
        elif car!=None:
            return car
        else:
            return bus
v=vehicle()
print("vehicle wheels is:",v.wheels())
print("bike wheels is :",v.wheels(input('enter bike wheels:')))
print("car wheels is :",v.wheels(input('enter car wheels:')))
print("bus wheels is :",v.wheels(input('enter bus wheels:')))

