def chai_customer():
     print("Welcome! what chai would you like ?")
     order = yield
     while True:
         print(f"Preparing: {order}")
         order = yield

customer = chai_customer()
next(customer) # start the generator

customer.send("Ginger tea")
customer.send("Lemon tea")