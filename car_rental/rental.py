class Rental:
    def __init__(self, car, start, end):
        self.car = car
        self.start = start
        self.end = end
        self.cancelled = False

    def get_price(self):
        return (self.end - self.start).days * self.car.rental_price