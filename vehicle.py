from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def Print():
        pass
    def __init__(self):
        pass
    def __del__(self):
        pass