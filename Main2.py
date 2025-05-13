# Activity 2: Class Vehicle
# Define the class Vehicle
class Vehicle:
    def _init_(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
# Ask the user for input
max_speed_input = input("Enter the vehicle's maximum speed (in km/h): ")
mileage_input = input("Enter the vehicle's mileage (in km): ")
# Create an object of class Vehicle using user input
car = Vehicle(max_speed_input, mileage_input)
# Print the values using the object
print("\nVehicle Information:")
print("Maximum Speed:", car.max_speed, "km/h")
print("Mileage:", car.mileage, "km")