
class BaseChai:
    def ___init__(self, type_):
        self.type = type_
        
    def prepare(self):
        print(f"Preparing {self.type} chai.")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardmom, ginger, cloves")

class ChaiShop:
    chai_cls = BaseChai
    
    def __init__(self):
        self.chai = self.chai_cls("Regular")
        
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):   
    chai_cls = MasalaChai
    
    def serve(self):
        print(f"Serving {self.chai.type} chai in the fancy shop")
        self.chai.prepare()
        self.chai.add_spices()
        
fancy_shop = FancyChaiShop()
fancy_shop.serve()
print(fancy_shop.chai.type) 