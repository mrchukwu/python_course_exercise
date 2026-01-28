def make_chai():
    return "Here is your tea"

return_value = make_chai()
print(return_value)


def chai_report():
    return 100, 20, 10 # sold, rmaining

sold, remaining, _ = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)
