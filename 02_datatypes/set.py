
essential_spices = {"cardamom", "ginger", "clove", "cinnamon", "nutmeg"}
optional_spices = {"nutmeg", "saffron", "vanilla"}

# Combine both sets using union operator
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# common spices (if any)
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# difference between essential and optional spices
only_in_essential = essential_spices - optional_spices
print(f"Spices only in essential: {only_in_essential}")

# membership test
print(f"Is nutmeg an essential spice? {"nutmeg" in essential_spices}")

# freeze set
