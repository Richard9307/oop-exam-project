from .car import Car

class PassengerCar(Car):
    def __init__(self, license_plate, car_type, rental_price, num_seats, trunk_size):
        super().__init__(license_plate, car_type, rental_price)
        self.num_seats = num_seats
        self.trunk_size = trunk_size

    def get_info(self):
        return (f"Passenger car: {self.car_type} ({self.license_plate}), {self.num_seats} seats, {self.trunk_size} liters trunk. "
                f"Daily price: {self.rental_price} Ft.")