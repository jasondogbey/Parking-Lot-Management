from abc import ABC, abstractmethod
from datetime import timedelta

class Vehicle(ABC):
    def __init__(self, license_plate):
        self.license_plate = license_plate

    @abstractmethod
    def get_vehicle_type(self):
        return self.license_plate

class Car(Vehicle):
    def get_vehicle_type(self):
        return "Car"

class Motorcycle(Vehicle):
    def get_vehicle_type(self):
        return "Motorcycle"

class ParkingSpot:
    def __init__(self, spot_number, vehicle=None):
        self.spot_number = spot_number
        self.vehicle = vehicle
    
    def check_if_available(self):
        return self.vehicle is None
    
    def park_vehicle(self, vehicle):
        if self.check_if_available():
            self.vehicle = vehicle
            return True
        return False
    
    def remove_vehicle(self):
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle
    

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.spots = [ParkingSpot(i) for i in range(1, capacity)]
        self.rate_per_hour = 5

    def find_available_spot(self):
        for spot in self.spots:
            if spot.check_if_available():
                return spot
        return None
            
    def park_vehicle(self, vehicle):
        spot = self.find_available_spot()
        if spot:
            if spot.park_vehicle(vehicle):
                return f"{vehicle.get_vehicle_type()} has been parked at spot {spot.spot_number}"
            else:
                return f"No available spot for {vehicle.get_vehicle_type()}"
        else:
            return "Parking lot is full"
    
    def exit_parking(self, spot_number):
        if 1 > spot_number > self.capacity:
            return "Invalid spot number"
        spot = self.spots[spot_number - 1]
        if spot.check_if_available():
            return "Spot is already empty"
        vehicle = spot.remove_vehicle()
        return self.calculate_fee(vehicle)
    
    def calculate_fee(self, vehicle):
        parked_time = timedelta(hours=2)
        parking_fee = (parked_time.total_seconds() / 3600) * self.rate_per_hour
        return f"The parking fee for {vehicle.get_vehicle_type()} is {parking_fee:.2f}"


# Example Usage:
car1 = Car("ABC123")
car2 = Car("XYZ789")
motorcycle1 = Motorcycle("MOT456")

parking_lot = ParkingLot(10)

print(parking_lot.park_vehicle(car1))  # Park a car
print(parking_lot.park_vehicle(car2))  # Park another car
print(parking_lot.park_vehicle(motorcycle1))  # Park a motorcycle

print(parking_lot.exit_parking(1))  # Remove vehicle from spot 1 and calculate fee

