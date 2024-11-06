from datetime import datetime, timedelta
from car_rental import CarRentalCompany, Rental
from dto import PassengerCar, Truck

def initialize_rental_company():
    rental_company = CarRentalCompany("Richard Rent")

    # Adding cars
    rental_company.add_car(PassengerCar("ABC-123", "Suzuki Swift", 15000, 5, 350))
    rental_company.add_car(PassengerCar("GHI-789", "Toyota Corolla", 18000, 5, 450))
    rental_company.add_car(Truck("DEF-456", "Mercedes Sprinter", 25000, 3500))

    # Adding rentals
    rental_company.add_rental(Rental(rental_company.cars[0], datetime(2024, 10, 2), datetime(2024, 10, 12)))
    rental_company.add_rental(Rental(rental_company.cars[0], datetime(2024, 11, 1), datetime(2024, 11, 2)))
    rental_company.add_rental(Rental(rental_company.cars[1], datetime(2023, 5, 5), datetime(2024, 5, 6)))
    rental_company.add_rental(Rental(rental_company.cars[2], datetime(2024, 11, 2), datetime(2024, 11, 3)))

    return rental_company

def rental_menu(company):
    while True:
        print(f"Welcome to the {company.name} Car Rental Company!")
        print("Please select an operation:")
        print("1. Rent a car")
        print("2. Cancel a rental")
        print("3. List rentals")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Available cars:")
            for car in rental_company.get_available_cars():
                print(car.get_info())

            license_plate = input("Enter the desired car's license plate: ").upper()
            car = next((c for c in rental_company.cars if c.license_plate == license_plate), None)
            if car:
                try:
                    start = datetime.strptime(input("Enter the rental start date (yyyy-mm-dd): "), "%Y-%m-%d")
                    end = start + timedelta(days=1)
                    result = rental_company.rent_car(car, start, end)
                    if isinstance(result, str):
                        print(result)
                    else:
                        print(f"The rental cost is {result} Ft.")
                except ValueError:
                    print("Invalid date format. Please use the format 'yyyy-mm-dd'.")
            else:
                print("Sorry, the car with that license plate is not found.")
        elif choice == "2":
            print("Current rentals:")
            for rental in company.get_current_rentals():
                print(f"{rental.car.get_info()} - {rental.start.strftime('%Y-%m-%d')} - {rental.end.strftime('%Y-%m-%d')}")
            license_plate = input("Enter the license plate of the car to cancel the rental: ").upper()
            rental = next((r for r in company.get_current_rentals() if r.car.license_plate == license_plate), None)

            if rental:
                company.cancel_rental(rental)
                print("The rental has been successfully cancelled.")
            else:
                print("Sorry, there is no active rental with that license plate.")
        elif choice == "3":
            print("Active rentals:")
            for rental in company.get_current_rentals():
                print(f"{rental.car.get_info()} - {rental.start.strftime('%Y-%m-%d')} - {rental.end.strftime('%Y-%m-%d')}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    rental_company = initialize_rental_company()
    rental_menu(rental_company)
