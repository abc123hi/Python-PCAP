# Define a class car( part of lesson 13 and 14 )

class Car:
    def __init__(self,numberDoors,registrationNum,make,model,year,max_speed,acceleration_rate,deceleration_rate) -> None:
        self.numberDoors = numberDoors
        self.registrationNum = registrationNum
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.acceleration_rate = acceleration_rate
        self.deceleration_rate = deceleration_rate
        self.mileage_miles = 0
        self.speed_mph = 0
    def __str__(self) -> str:
        return f"Car{{'number_doors':{self.numberDoors}, 'registration_number':{self.registrationNum}, 'make':{self.make}, 'model':{self.model}, 'year':{self.year}, 'max_speed:{self.max_speed}, 'acceleration_rate':{self.acceleration_rate}, 'deceleration_rate':{self.deceleration_rate}}}"
    def acceleration(self) -> None:
        print(f"{self.make} {self.model} accelerating...")