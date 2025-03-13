import pandas as pd
# Class representing a single car
class Car:
    def __init__(self, model, price, fuel_efficiency, brand, horsepower, safety_rating, color):
        self.model = model
        self.price = price
        self.fuel_efficiency = fuel_efficiency
        self.brand = brand
        self.horsepower = horsepower
        self.safety_rating = safety_rating
        self.color = color
    def __repr__(self):
        return f"{self.model} ({self.brand}): ${self.price}, {self.fuel_efficiency} MPG, Safety: {self.safety_rating} Stars"

# Class representing the car shop with available cars
class CarShop:
    def __init__(self):
        self.cars = []
    def add_car(self, car):
        self.cars.append(car)
    def get_available_cars(self):
        return self.cars


# Class representing a car buyer, who can choose a car based on preferences
class CarBuyer:
    def __init__(self, budget, min_fuel_efficiency, brand_preference, min_safety_rating):
        self.budget = budget
        self.min_fuel_efficiency = min_fuel_efficiency
        self.brand_preference = brand_preference
        self.min_safety_rating = min_safety_rating
    def filter_cars(self, cars):
        # Filter cars based on the buyer's preferences
        matching_cars = [
            car for car in cars
            if car.price <= self.budget
            and car.fuel_efficiency >= self.min_fuel_efficiency
            and (self.brand_preference.lower() in car.brand.lower() or self.brand_preference == "")
            and car.safety_rating >= self.min_safety_rating ]
        return matching_cars
    def recommend_car(self, car_shop):
        available_cars = car_shop.get_available_cars()
        filtered_cars = self.filter_cars(available_cars)
        if not filtered_cars:
            print("No cars match your criteria. Please adjust your preferences.")
        else:
            print(f"\nHere are the cars that match your preferences (Price <= ${self.budget}, Min Fuel Efficiency >= {self.min_fuel_efficiency} MPG, Brand: {self.brand_preference}, Min Safety Rating >= {self.min_safety_rating}):")
            for car in filtered_cars:
                print(car)
# Example usage:
# 1. Create a CarShop and add some cars
car_shop = CarShop()
# Adding some car models to the car shop
car_shop.add_car(Car('Honda Civic', 22000, 30, 'Honda', 158, 4.5, 'Red'))
car_shop.add_car(Car('Toyota Corolla', 21000, 32, 'Toyota', 139, 4.7, 'Blue'))
car_shop.add_car(Car('BMW 3 Series', 35000, 25, 'BMW', 255, 4.2, 'Black'))
car_shop.add_car(Car('Ford Focus', 20000, 28, 'Ford', 160, 4.3, 'White'))
car_shop.add_car(Car('Chevrolet Malibu', 23000, 26, 'Chevrolet', 160, 4.4, 'Silver'))
# 2. Ask for buyer preferences and create a CarBuyer object
print("Welcome to the car shop!\n")
# Get buyer preferences (for simplicity, input is taken as plain text)
try:
    budget = float(input("Enter your maximum budget (in USD): $"))
    min_fuel_efficiency = float(input("Enter the minimum fuel efficiency (in MPG): "))
    brand_preference = input("Enter your preferred brand (leave blank for any): ")
    min_safety_rating = float(input("Enter the minimum safety rating (out of 5): "))
    buyer = CarBuyer(budget, min_fuel_efficiency, brand_preference, min_safety_rating)
    # 3. Get recommendations based on buyer preferences
    buyer.recommend_car(car_shop)

except ValueError:
    print("Invalid input! Please enter valid numbers for budget, fuel efficiency, and safety rating.")
