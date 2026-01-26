staff = [("Amit", 16), ("Bina", 22), ("Chetan", 19)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is a minor.")
        break
else:
    print("All staff are adults.")
print("End of staff list.")