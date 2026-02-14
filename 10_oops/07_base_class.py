class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# Code duplication
# class GingerChai(Chai):
#     def __init__(self, type_, strength, ginger_amount):
#         self.type = type_
#         self.strength = strength
#         self.ginger_amount = ginger_amount
        

# Explicit Call
# class Ginger(Chai):
#     def __init__(self, type_, strength, ginger_amount):
#         Chai.__init__(self, type_, strength)
#         self.ginger_amount = ginger_amount

# Better way to call the base class constructor:  Supper()
class GingerChai(Chai):
    def __init__(self, type_, strength, ginger_amount):
        super().__init__(type_, strength)
        self.ginger_amount = ginger_amount