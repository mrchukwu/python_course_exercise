def coffee_tea():
    yield "Lemo Tea"
    yield "Ginger Tea"

def imported_tea():
    yield "Matcha"
    yield "Oolong"
    
def full_menu():
    yield from coffee_tea()
    yield from imported_tea()

for tea in full_menu():
    print(tea)


def coffee_stall():
    try:
        while True:
            order = yield "Waiting for tea order"
    except:
        print("Stall closed, No more tea")

stall = coffee_stall()
print(next(stall))
stall.close()