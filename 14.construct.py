class car:
    def __init__(self,color,brand,wheels,gears,windows,lights):
        self.color=color
        self.brand=brand
        self.wheels=wheels
        self.gears=gears
        self.windows=windows
        self.lights=lights

    def showDescription(self):
            print("This car is",self.color,self.brand,self.wheels,self.gears,self.windows,self.lights)
    def changeColor(self,color):
                self.color=color
    def setWheels(self,wheels):
                self.wheels=wheels
    def changeBrand(self,brand):
                self.brand=brand

c=car('Black','Toyota','Wheels 4','gears 6','windows 2','lights 4')
c.showDescription()
c.changeColor('WHITE')
c.setWheels('wheels 8')
c.changeBrand('LAMBORGINI')
c.showDescription()

car={"color":"Black","brand":"Toyota","wheels":"4","gears":"6","windows":"2","lights":"4"}
for key in car:
        print( key,car [key])