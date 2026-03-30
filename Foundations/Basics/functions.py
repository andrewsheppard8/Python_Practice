##parcels = {
##    "parcel_1": {"area_sqft": 10000},
##    "parcel_2": {"area_sqft": 5000},
##    "parcel_3": {"area_sqft": 20000},
##}

"""Calling a function in a loop"""
##def sqft_to_hectares(sqft):
##    """
##    Convert square feet to hectares.
##    1 sq ft = 0.0000092903 hectares
##    """
##    return sqft*0.0000092903
##
##for parcel_id,parcel_info in parcels.items():
##    hectares = sqft_to_hectares(parcel_info["area_sqft"])
##    parcel_info["area_ha"]=hectares
##
##print(parcels)

"""Calling a function in a function"""
##def convert_hectares(parcel_dict):
##    def sqft_to_hectares(sqft):
##        return sqft*0.0000092903
##    for parcel_id,parcel_info in parcel_dict.items():
##        parcel_info["area_ha"]=sqft_to_hectares(parcel_info["area_sqft"])
##    return parcel_dict
##
##parcels = {
##    "parcel_1": {"area_sqft": 10000},
##    "parcel_2": {"area_sqft": 5000},
##    "parcel_3": {"area_sqft": 20000},
##}
##print(parcels)
##print("")
##print(convert_hectares(parcels))

"""Working with global variables"""
##counter=0
##def add_one():
##    global counter
##    counter += 1
##    print("Inside function:",counter)
##print("Before:",counter)
##add_one()
##add_one()
##print("After:",counter)

#You can call a variable in a function if you are just reading it
##total=100
##def show_total():
##    print("The total is:",total)
##show_total()

value=5

"""Working with a global variable in a nested function"""
##def outer():
##    global value
##    value += 10
##    def inner():
##        global value
##        value *= 2
##    inner()
##outer()
##print(value)

"""Working with arbitrary arguments (integer)"""
##def add_all(*args):
##    return(sum(args))
##print(add_all(1,2,3,4))

"""Working with arbitrary arguments (string)"""
##person_list=[]
##def store_info(**kwargs):
##    person_list.append(kwargs)
##
##store_info(name="Andrew", age=38)
##store_info(name="Betty", age=30)
##
##print(person_list)

##person_dict={}
##def store_info(**kwargs):
##    name=kwargs.get("name")
##    if name:
##        person_dict[name]=kwargs
##
##store_info(name="Andrew",age=38)
##store_info(name="Betty",age=30)
##
##print(person_dict)

"""using a global variable from one function to another"""
##shared_value=None
##def create_value():
##    global shared_value
##    shared_value=42
##def use_value():
##    print("The value is:",shared_value)
##create_value()
##use_value()

"""using return to call a value from one function to another"""
##def create_value():
##    return 40
##def use_value(value):
##    print("The value is:",value)
##value=create_value()
##use_value(value)

"""using a dictionary to store a shared state"""
shared_data = []  # list to hold multiple people
def add_person(name, age):
    person = {"name": name, "age": age}
    shared_data.append(person)  # add new person
def print_people():
    for person in shared_data:
        print(f"{person['name']} is {person['age']} years old.")
# Add multiple people
add_person("Andrew", 38)
add_person("Betty", 30)
add_person("Charles", 25)
# Print all
print_people()
