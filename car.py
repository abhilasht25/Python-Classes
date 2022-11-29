from vehicle import Vehicle

class Car(Vehicle):
    __speed=0.0
    __model=""
    __color=""
    NumCars=0
    def GetSpeed(self)->float:
        return self.__speed
    def GetModel(self)->str:
        return self.__model
    def GetColor(self)->str:
        return self.__color
    def SetSpeed(self, speed: float):
        self.__speed=speed
    def SetModel(self, model: str):
        self.__model=model
    def SetColor(self, color: str):
        self.__color=color
    def Print(self):
        print("\n Hi! My model name is "+self.__model + ", I am  " + self.__color + " in color and my top speed is " + str(self.__speed) + " mph.")
    def Decelerate(self)->float:
        self.__speed=self.__speed-10
        return self.__speed
    def Accelerate(self)->float:
        self.__speed=self.__speed+10
        return self.__speed
    def GetNumCars(self)->int:
        return self.NumCars
    def __del__(self):
        Car.NumCars=Car.NumCars-1
        print("\n Scrapping car with model name "+self.__model+" , "+str(self.GetNumCars())+" cars are remaining" )
    def __init__(self,speed:float=20,model:str="Base Car",color:str ="Colourless"):
        self.__speed=speed
        self.__model=model
        self.__color=color
        Car.NumCars += 1