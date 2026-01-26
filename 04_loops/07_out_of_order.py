flavours = ["vanilla", "Out of stock", "strawberry", "Discontinued", "mint"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item is found")
        break
    print(f"{flavour} is available")
print("End of flavour list.")