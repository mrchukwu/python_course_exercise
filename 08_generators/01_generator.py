def serve_tea():
    yield "Cup 1: Ginger tea"
    yield "Cup 2: Milk tea"
    yield "Cup 3: Lemon tea"
    
stall = serve_tea()

for cup in stall:
    print(cup)

# function uses return
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

def get_tea_gen():
    yield "Cup 1: Chai"
    yield "Cup 2: Chai"
    yield "Cup 3: Chai"
    
tea = get_tea_gen()
print(next(tea))
print(next(tea))
print(next(tea))
print(next(tea)) # gives an error: StopIteration

