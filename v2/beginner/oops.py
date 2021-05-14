
class Farmer():
    
    def __init__(self, 
                 name: str,
                 number: int, 
                 language: str, 
                 crop: str, 
                 variety: str,
                 district: str,
                 market: str):
        
        self.name = name
        self.number = number
        self.language = language
        self.crop = crop
        self.variety = variety
        self.district = district
        self.market = market
        
    def __str__(self):
        return f"{self.name} has {self.number} searched for {self.crop}, {self.variety} at {self.district} & {self.market} "
    
    def farmer_info(self):
        return f"{self.name} has {self.number} searched for {self.crop}, {self.variety} at {self.district} & {self.market} "
    
    def married_status(self, status):
        return f"{self.name} is {status}"


class FarmerDetails(Farmer):
    pass

class Car():
    
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
     
    # to modify the generic output of the class constructor    
    def __str__(self):
        return f"The {self.color} has {self.mileage} miles"



class Dog():
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetreiver(Dog):
    
    def speak(self, sound = "Bark"):
        return super(). speak(sound)


farmer1 = Farmer("karthik",8500004959,"en", "Maize", "LOCAL", "Davengere","Davengere")

print(farmer1.married_status("single"))

print(farmer1.farmer_info())

print(farmer1)

bluecar = Car("blue car", 20000)
redcar = Car("red car", 30000)

print(bluecar)
print(redcar)