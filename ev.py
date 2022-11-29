from car import Car
class EV(Car):
    __range=0.0
    __gen=1
    def GetRange(self)->float:
        return self.__range
    def GetGen(self)->int:
        return self.__gen
    def SetRange(self,range:float):
        self.__range=range
    def SetGen(self,gen:int):
        self.__gen=gen
    def Print(self):
        super().Print()
        print("\n Also I am very friendly to the environment because I am an electric vehicle of "+str(self.__gen)+" generation. I  can travel upto " + str(self.__range) + " miles in a single charge.")
    def __del__(self):
        super().__del__()              
    def __init__(self,speed:float=20,model:str="hot wheels",color:str="White",range:float=100,gen:int=1):
        super().__init__(speed, model, color)
        self.__range=range
        self.__gen=gen
        print("\n Manufactuing an electric vehicle with model name "+str(self.GetModel()))