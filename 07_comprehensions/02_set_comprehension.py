favourite_tea = [
     "Green tea", "Lipton tea", "Lemon tea", "Green tea", "Milk tea", "Ginger tea", "Milk tea", "Lipton tea"
 ]
 
unique_tea = {tea for tea in favourite_tea}
# print(unique_tea)

unique_tea = {tea for tea in favourite_tea if len(tea) > 8 }
# print(unique_tea)


recipes = {
    "Jolof rice" : ["maggi", "rice", "onions", "ajino", "groundnut oil", "pepper"],
    "Beans" : ["beans", "red oil", "onions", "salt", "maggi", "pepper", "crayfish"],
    "Pasta" : ["spaghetti", "groundnut oil", "crayfish", "onions", "maggi", "salt"]
}

unique_spicies = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spicies)