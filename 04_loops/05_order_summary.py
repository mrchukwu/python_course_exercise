names = ["Alice", "Bob", "Charlie", "Diana"]
bills = [23.50, 45.00, 12.75, 67.80]

for name, bill in zip(names, bills):
    print(f"Customer: {name}, Bill Amount: ${bill:.2f}")