masal_spices = ("cumin", "coriander", "turmeric", "chili powder", "garam masala")

# unpacking
(spice1, spice2, spice3, spice4, spice5) = masal_spices
print(spice1)  # Output: cumin
print(spice2)  # Output: coriander 

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio}, C: {cadramom_ratio}")  # Output: Ratio is G: 2, C: 1

# swaping values
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"After swapping, Ratio is G: {ginger_ratio}, C: {cadramom_ratio}")  # Output: After swapping, Ratio is G: 1, C: 2

# memebership
print(f"Is turmeric in masala spices? {"turmeric" in masal_spices}")  # Output: True 