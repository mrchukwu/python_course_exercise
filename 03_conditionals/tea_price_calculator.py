# A tea store offer different prices for different cup sizes.
# Write a program tha calculates the price based on the size

cup = input("Choose your cup size (small, medium, large): ").lower()

if cup == "small":
    print("The price for a small cup of tea is $3.")
elif cup == "medium":
    print("The price for a medium cup of tea is $5.")
elif cup == "large":
    print("The price for a large cup of tea is $8.")
else:
    print("Invalid cup size selected.")