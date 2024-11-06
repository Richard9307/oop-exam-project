from .car import Car

class Truck(Car):
    def __init__(self, license_plate, car_type, rental_price, load_capacity):
        super().__init__(license_plate, car_type, rental_price)
        self.load_capacity = load_capacity

    def get_info(self):
        return (f"Truck: {self.car_type} ({self.license_plate}), {self.load_capacity} load Capacity. "
                f"Daily price: {self.rental_price} Ft.")