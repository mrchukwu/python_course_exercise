
class Chaicup:
    cup_size = 150
    
    def chaicup_description(self):
        print(f"This is a {self.cup_size}ml cup of chai.")
    
my_cup = Chaicup()
my_cup.cup_size = 200
print(my_cup.chaicup_description())
print(f"Chaicup class: {Chaicup}")
print(f"my_cup object: {my_cup}")

print(Chaicup.chaicup_description(my_cup))

