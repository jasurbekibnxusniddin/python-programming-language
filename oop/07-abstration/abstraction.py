from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstrakt sinf
    @abstractmethod
    def start_engine(self):
        pass  # Realizatsiya yo'q

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"

    def stop_engine(self):
        return "Bike engine stopped"

# Obyektlar yaratish
car = Car()
bike = Bike()

print(car.start_engine())  # Car engine started
print(bike.start_engine())  # Bike engine started
