class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        return (
            f"Sipping a {self.sweetness} sweet chai with {self.milk_level} milk level."
        )

    def add_sugar(self, amount):
        self.sweetness += amount 
        return f"Added {amount} sweetness. New sweetness level: {self.sweetness}."


my_chai = Chai(sweetness=3, milk_level=3)

my_chai.add_sugar(2)
print(my_chai.sip())
