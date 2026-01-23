
chai_order = dict(type="Masala Chai", size="Large", sugar=2, milk=True)
print(f"chai order: {chai_order}")

chai_recipe = {} # Initialize an empty dictionary
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe["base"]}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

# membership test
print(f"Is milk in recipe? {'milk' in chai_recipe}")


chai_order = {"types": "Ginger tea", "size": "Midium", "Sugar": 2, "Milk": True}

# get the keys
print(f"Order details (Keys): {chai_order.keys()}")
# get the values
print(f"Order details (Values): {chai_order.values()}")
# get the items
print(f"Order details (Items): {chai_order.items()}")

# get last item
last_item = chai_order.popitem()
print(f"Last item removed: {last_item}")

extra_order = {"flavor": "Cardamom", "temperature": "Hot"}

# update chai_order with extra_order
chai_order.update(extra_order)
print(f"Updated chai order: {last_item}")

# using get method
chai_size = chai_order.get("size", "NO size specified")
print(f"Chai size: {chai_size}")