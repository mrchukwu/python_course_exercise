
class Person:
    def __init__(self, name, career):
        self.name = name
        self.career = career
    
    def summary(self):
        print(f"My name is {self.name} and I am a {self.career}.")
    
    def get_name(self):
        return self.name

person1 = Person("Kennedy", "Software Engineer")

print(person1.summary())
print(person1.get_name()) 


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def description(self):
        print(f"{self.name} is a {self.species}.")
        

animal1 = Animal("Leo", "Lion")
print(animal1.description())