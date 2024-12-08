class automobile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the automobile")

    def stop(self):
        print("Stopping the automobile")

class car(automobile):
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year) # this line means that we are calling the init method of the parent class
        self.top_speed = top_speed

    def accelerate(self):
        print("Accelerating")

def main():
   
    car1 = car("Toyota", "Camry", 2022, 200)
    
    car1.start()
    car1.stop()
    car1.accelerate()
    
    print("Make:", car1.make)
    print("Model:", car1.model)
    print("Year:", car1.year)
    print("Top Speed:", car1.top_speed)

if __name__ == "__main__":
    main()

# polymorphism