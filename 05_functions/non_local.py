def update_order():
    chai_type = "ginger"
    def kitchen():
        nonlocal chai_type
        chai_type = "coffee"
        # print(chai_type)
    kitchen()
    print("After kitchen update", chai_type)
    
update_order()