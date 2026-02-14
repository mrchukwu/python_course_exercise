
class Chai:
    temperature = "Hot"
    strength = "Strong"
    

cutting = Chai()
print(cutting.temprature)

cutting.temperature = "mild"
print(f"Cutting temperature {cutting.temperature}")
print(f"Cutting temperature {Chai.temperature}")



print(cutting.__doc__)