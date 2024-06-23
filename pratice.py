class vehicle:
    def wheels(self,bike=None,car=None,bus=None):
        if bike!=None and car!=None and bus!=None:
            return bike,car,bus
        elif bike!=None:
            return bike
        elif car!=None:
            return car
        elif bike!=None and car!=None:
            return bike,car
        else:
            return bus
    def color(self,bike=None,car=None,bus=None):
        if bike!=None and car!=None and bus!=None:
            return bike,car,bus
v=vehicle()
print("color wheels is:",v.wheels())
print("vehicle wheels is:",v.wheels())
print("bike and car and bus wheels is:",(v.wheels(input("enter bike wheels:")),(input("enter car wheels:")),(input("enter bus wheels:"))))