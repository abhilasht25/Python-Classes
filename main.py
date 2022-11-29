from ev import EV
from car import Car
def main():
    #using parameterized constructor
    c1=Car()
    c1.Print()
    #using default constructer
    c2=Car(20,"FIAT","black")
    c2.Print()
    #updating member variables for base car
    c2.SetSpeed(255.5)
    c2.SetModel("Ferari")
    c2.SetColor("Red")
    c2.Print()
    #accelerate and decelerate
    c2.Accelerate()
    print("\n The "+ c2.GetModel()+" car with "+ c2.GetColor()+" color now has a top speed of "+ str(c2.GetSpeed())+" mph")
    c2.Decelerate()
    c2.Decelerate()
    print("\n However,Due to an engine snag the top speed has been downgraded to "+ str(c2.GetSpeed())+" mph")
    #Checking how many cars has been made
    print("\n we have manufactured "+ str(c2.GetNumCars())+" cars")
    #Electric Vehicle
    e1=EV() #default
    e1.Print()
    e2=EV(300,"Tesla","Beige","600",3) #parameterized
    e2.Print()
    #updates on EV
    print("\n Performing upgrades on "+e1.GetModel())
    e1.SetSpeed(200.75)
    e1.SetModel("Rivian")
    e1.SetColor("Red")
    e1.SetRange("450")
    e1.SetGen(2)
    print("It has been successfully upgraded to a gen "+str(e1.GetGen())+" "+ e1.GetModel()+" with an updated speed of "+str(e1.GetSpeed())+" mph with a stunning "+e1.GetColor()+" and an amazing range of "+str(e1.GetRange()))
main()