
def infinite_tea_generator():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refil = infinite_tea_generator()
user2 = infinite_tea_generator()

# print(next(refil))

for _ in range(5):
    print(next(refil))

for _ in range(3):
    print(next(user2))

#