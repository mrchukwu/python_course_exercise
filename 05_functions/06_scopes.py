def serve_tea():
    tea_type = "Milk choco" # Local scope inside the function
    print(f"Serving {tea_type} tea")

tea_type = "coffee" #global scope variable
serve_tea()
print(tea_type) # Global scope outside the function


def chai_counter():
    chai_order = "lemon"
    
    def print_order():
        chai_order = "ginger"
        print("inner: ", chai_order)
        
    print_order()
    print("outer: ", chai_order)
    

chai_order = "choco"
chai_counter()
print("global: ", chai_order)