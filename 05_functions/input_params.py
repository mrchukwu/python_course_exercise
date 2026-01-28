chai = "Ginger tea"

def prepare_chai(order):
    print("Preparing ", order)

prepare_chai(chai)


def make_tea(tea, milk, sugar):
    print(tea, milk, sugar)

make_tea( "PH", "Yes", "Low") #positonal
make_tea(tea="Green tea", sugar="Medium", milk="No") # keywords

def special_chai(*inredients, **extras):
    print("Ingredients: ", inredients)
    print("Extras: ", extras)
    
special_chai("Cinnamon", "Cardmom", sweetner="Honey", foaam="yes")


# handling default values
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# chai_order()
# chai_order()
# chai_order()

#soliving above issue
def chai_order(order=None):
    if order is None:
        order = []
        print(order)

chai_order()
chai_order()
chai_order()


