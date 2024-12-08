from uuid import uuid4

class Car:
    __created_cars = 0
    def __init__(self, id, make, model, year, km = 0):
        self.__id = str(uuid4()) # incapsulation. private attribute
        self.__km = km # incapsulation. private attribute
        self.make = make
        self.model = model
        self.year = year
        # this means that we are calling the init method of the parent class
        Car.__created_cars += 1
    
    def get_id(self):
        return self.__id
    
    def get_km(self):
        return self.__km
    
    def add_km(self, km):
        if km > 0:
            self.__km += km
        else:
            print("Invalid km")
    
    @classmethod
    def get_created_cars(cls):
        return cls.__created_cars
        
    
def main():
    car = Car(1, "Toyota", "Camry", 2022)
    print(car.get_id())
    car.add_km(1000)
    print(car.get_km())
    car.add_km(-1000)
    print(car.get_km())

    print(Car.get_created_cars())

if __name__ == "__main__":
    main()