
def chai_flavor (flavor="masadal"):
    """return the flavor of chai."""
    chai="ginger"
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

def generate_bill(chai=0, samosa=0):
    """_summary_
    Args:
        chai (int, optional): _description_. Defaults to 0.
        samsosa (int, optional): _description_. Defaults to 0.
        :param chai: Number of chai cups (10 each)
        :param samosa: Number of samosa (15 each)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting kennedy.com"

generate_bill(2, 3)