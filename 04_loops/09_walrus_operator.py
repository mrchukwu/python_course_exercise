# The sign of walrus operator := this is used to run an expression an asign to a variable without initially ccreating the variable.

flavours = ["vanilla", "chocolate", "strawberry", "mint"]

print("Available flavours: ", flavours)

while (flavour := input("What flavour would you like? ")) not in flavours:
    print(f"Sorry, we don't have {flavour}.")
print(f"Here is your {flavour} flavour.")