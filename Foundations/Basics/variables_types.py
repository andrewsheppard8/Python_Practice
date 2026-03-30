##list_a=['Parcel_A','Parcel_B','Parcel_C','Parcel_D','Parcel_E']
##list_b=[10890,21780,32670,43560,54450]
##final_list=dict(zip(list_a,list_b)) #using zip to combine two lists into a dictionary
##print(final_list)
##list_acre=[]
##for i in list_b:
##    acre=i/43560
##    list_acre.append(acre)
##final_acre=dict(zip(list_a,list_acre))
'''best solution'''
##final_acre={name:(sqft/43560) for name,sqft in zip(list_a,list_b)}
''' '''
##print(list_acre)
##print(final_acre)
##for key,value in final_acre.items():
##    print(f"Parcel {key} is {value} acres.")

##parcel_names=[]
##parcel_sqft=[]
##while True:
##    name=input("Enter parcel name: ")
##    parcel_names.append(name)
##    sq_feet=float(input("Enter parcel size(ft): "))
##    parcel_sqft.append(sq_feet)
##
##    cont=input("Add another parcel? (Y/N): ").strip().upper()
##    if cont == "Y":
##        continue
##    else:
##        break #Exit the loop if not "Y"
##
##total_parcel={name:sqft for name,sqft in zip(parcel_names,parcel_sqft)}
##print("\nAll parcels:")
##for key, value in total_parcel.items():
##    print(f"Parcel {key} has {value} square feet.")
##
##change=input("\nDo you want to convert square feet to acres? (Y/N): ").strip().upper()
##
##if change == "Y":
##    total_parcel={parcel:sqft/43560 for parcel,sqft in total_parcel.items()}
####    for key in total_parcel:
####        total_parcel[key]=total_parcel[key]/43560
##    print("\nAcres updated: ")
##    for key,value in total_parcel.items():
##        print(f"Parcel {key} has {value} acres")
##else:
##    print("Completed")

##parcels={}
##while True:
##    #name validation
##    while True:
##        name=input("Enter parcel name: ")
##        if name != "":
##            break
##        else:
##            print("Parcel name cannot be blank.")
##    #size validation
##    while True:
##        try:
##            sq_feet = float(input("Enter parcel size(ft): "))
##            break
##        except ValueError:
##            print("Enter a valid number")
##    parcels[name]=sq_feet
##    #Y/N validation
##    while True:
##        cont=input("Add another parcel? (Y/N): ").strip().upper()
##        if cont == "Y":
##            break
##        elif cont == "N":
##            break
##        else:
##            print("Please enter Y or N.")
##    if cont=="N":
##        break
##print("\nAll parcels:")
##for key,value in parcels.items():
##    print(f"Parcel {key} is {value} sqare feet in size.")
##while True:
##    change=input("\nDo you want to convert square feet to acres? (Y/N): ").strip().upper()
##    if change not in ("Y","N"):
##        print("Please enter Y or N.")
##        continue
##    if change == "Y":
##        parcels={p:s/43560 for p,s in parcels.items()}
##        print("\nAcres updated")
##        for key,value in parcels.items():
##            print(f"Parcel {key} is {value} acres in size.")
##    else:
##        print("Completed")
##    break

def get_parcel_name():
    while True:
        name = input("Enter parcel name: ").strip()
        if name:
            return name
        print("Parcel name cannot be blank.")

def get_sqft():
    while True:
        try:
            return float(input("Enter parcel size (ft): "))
        except ValueError:
            print("Enter a valid number.")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().upper()
        if answer in ("Y", "N"):
            return answer
        print("Please enter Y or N.")

def average_size(parcel_dict):
   return sum(parcel_dict.values())/len(parcel_dict)

def total_size(parcel_dict):
    return sum(parcel_dict.values())

def largest_size(parcel_dict):
    largest_parcel=max(parcel_dict, key=parcel_dict.get)
    largest_size=parcel_dict[largest_parcel]
    return largest_parcel,largest_size

parcels = {}

while True:
    name = get_parcel_name()
    sqft = get_sqft()
    parcels[name] = sqft # this is what actually builds the dictionary
    cont = get_yes_no("Add another parcel? (Y/N): ")
    if cont == "N":
        break

print("\nAll parcels:")
for key, value in parcels.items():
    print(f"{key}: {value:.2f} sq ft")
print(f"Total parcel size: {total_size(parcels)} square feet")
print(f"Average parcel size: {round(average_size(parcels))} square feet")
largest_parcel_name, largest_parcel_size = largest_size(parcels)
print(f"Largest parcel is {largest_parcel_name} with a size of {largest_parcel_size} square feet")
change = get_yes_no("\nConvert square feet to acres? (Y/N): ")

if change == "Y":
    parcels = {k: v / 43560 for k, v in parcels.items()}
    print("\nAcres updated:")
    for key, value in parcels.items():
        print(f"Parcel {key} is {value} acres")
else:
    print("Completed")

