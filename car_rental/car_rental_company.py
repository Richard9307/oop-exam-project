from datetime import datetime


class CarRentalCompany:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.rentals = []

    def add_car(self, car):
        self.cars.append(car)

    def add_rental(self, rental):
        self.rentals.append(rental)

    def get_available_cars(self):
        available_cars = []
        for car in self.cars:
            if not any(rental.car == car and rental.start <= datetime.now() <= rental.end and not rental.cancelled for rental in self.rentals):
                available_cars.append(car)
        return available_cars


    def get_current_rentals(self):
        return [rental for rental in self.rentals if rental.start <= datetime.now() <= rental.end and not rental.cancelled]

    def rent_car(self, car, start, end):
        from .rental import Rental

        # Check if the car is available for the requested dates
        if any(rental.car == car and rental.start <= end and start <= rental.end and not rental.cancelled for rental in self.rentals):
            return "Car is not available for the requested dates."

        # Check if rental dates are valid
        if start >= end:
            return "Invalid rental dates."

        rental = Rental(car, start, end)
        self.add_rental(rental)
        return rental.get_price()

    def cancel_rental(self, rental):
        rental.cancelled = True
        return f"Rental for {rental.car.license_plate} has been cancelled."

    def list_rentals(self):
        return [rental.get_rental_info() for rental in self.rentals]