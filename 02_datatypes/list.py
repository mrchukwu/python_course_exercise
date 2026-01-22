
ingredients = ["flour", "sugar", "eggs", "butter", "milk"]

# adding an ingredient
ingredients.append("vanilla extract")
print("Ingredients after adding vanilla extract:", ingredients)

# removing an ingredient
ingredients.remove("sugar")
print("Ingredients after removing sugar:", ingredients)

spcie_options = ["ginger", "nutmeg"]
chai_ingredients = ["water", "milk"]

# extending the list with another list
chai_ingredients.extend(spcie_options)
print("Chai ingredients after adding spices:", chai_ingredients)

# adding at specific index
chai_ingredients.insert(2, "tea leaves")
print("Chai ingredients after inserting tea leaves:", chai_ingredients)

# using pop to remove last item
last_added  = chai_ingredients.pop()
print("Last added ingredient removed:", last_added)
print("Chai ingredients after popping last ingredient:", chai_ingredients)

# reverse the list
print("Chai ingredients before reversing:", chai_ingredients)
chai_ingredients.reverse()
print("Chai ingredients after reversing:", chai_ingredients)

# sorting the list
chai_ingredients.sort()
print("Chai ingredients after sorting:", chai_ingredients)

# maximum and minimum values
sugar_levels = [5, 10, 3, 8, 2]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

# Operator overloading
base_liquid = ["water", "milk"]
extra_flavor = ["honey", "lemon"]
full_liquid_mix = base_liquid + extra_flavor
print("Full liquid mix:", full_liquid_mix)

strong_brew = ["tea leaves"] * 3
print("Strong brew ingredients:", strong_brew)

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print("Modified spice data:", raw_spice_data.decode("utf-8"))