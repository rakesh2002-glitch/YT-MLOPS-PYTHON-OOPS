class Employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("Finished executing data")

    def travel(self,destination):
        print("This travel method was called manually")
        print(f"emplyee is now travelling to {destination}")



#Creating an object or instance of the class
sam=Employee()

sam.travel("Gurgaon")

