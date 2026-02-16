# MRO Method Resolution Order

class A:
    label = "A: Base class"

class B(A):
    label = "B: Derived class"

class C(A):
    label = "C: Derived class"

class D(B, C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)  # Method Resolution Order