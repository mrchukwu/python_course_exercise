# import recipes.flavors

# print(recipes.flavors.mil_flavor_tea())
# print(recipes.flavors.choco_flavor_tea())

# from recipes.flavors import mil_flavor_tea, choco_flavor_tea
# print(mil_flavor_tea())
# print(choco_flavor_tea())

from .recipes.flavors import mil_flavor_tea, choco_flavor_tea
print(mil_flavor_tea())
print(choco_flavor_tea())