# pure functions
def pure_chai(cups):
    return cups * 10
total_chai = 0

#impue function (not recommended)
def impure_chai(cups):
    global total_chai
    total_chai += cups

# recursive functions
def pour_chai(n):
    print(f"Pouring chai {n} times")
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)

print(pour_chai(3))


#Lambdas functions
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

print(strong_chai)