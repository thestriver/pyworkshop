def name_length(name):
    return len(name)
def lower_name(name):
    return name.lower()

def upper_name(name):
    return name.upper()

if __name__ == "_main_":
    name = "Nina"
    length = name_length(name)
    upper_case = upper_name(name)
    print(f"The length of my name is {length} and the upper case form is {upper_case}")