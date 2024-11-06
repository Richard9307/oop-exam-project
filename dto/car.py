from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, license_plate, car_type, rental_price):
        self.license_plate = license_plate
        self.car_type = car_type
        self.rental_price = rental_price

    @abstractmethod
    def get_info(self):
        pass