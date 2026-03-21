class Car:
     total= 0 # class variable
     def __init__(self, brand, model, year):
          self.__brand = brand
          self.model = model
          self.year = year
          Car.total += 1 # class variable
     def get_brand(self):
          return self.__brand
     # def set_brand(self, brand):
     #      self.__brand = brand
     # brand = property(get_brand, set_brand)


     def my_car(self):
          return f"model: {self.model}, year:{self.year}"
     def use_fuel(self):
          return 'petrol or diesel'

my_cars= Car('toyota', 'camry', 2022) # input details
# print(my_cars.brand) # access details
# print(my_cars.model) # access details
# print(my_cars.my_car()) # access details with method 

# inheritence 
class Electric_car(Car):
     def __init__(self, brand, model, year, color, speed):
          super().__init__(brand, model, year)
          self.color = color
          self.speed = speed
     def use_fuel(self):
          return 'Battery or Electric'
new_electric_car= Electric_car('tesla','s', 2026, 'black', 500) # input details
# print(new_electric_car.brand) # access details
# print(new_electric_car.get_brand()) # access details with method
# print(new_electric_car.my_car()) # access details with method 
# print(new_electric_car.color) # access details
# print(new_electric_car.speed) # access details

print(Car.total)


