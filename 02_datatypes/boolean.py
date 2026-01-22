is_boiling = True
is_raining = False

# upcasting
stri_count = 5
total_actions = stri_count + is_boiling
print(f"Total actions (with upcasting): {total_actions}") 


# Falsey values 0, "", None, [], {}, set()
milk_present = 0 # no milk present meaing False
print(f"Is milk present? {bool(milk_present)}")