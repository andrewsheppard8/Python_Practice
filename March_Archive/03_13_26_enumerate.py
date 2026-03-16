##cities = ["LA", "Denver", "Chicago"]

##for city in cities:
##    print(city)

##for i in range(len(cities)):
##               print(i,cities[i])

##for i,city in enumerate(cities):
##    print(i,city)

##for i, city in enumerate(cities):
##    if i == 1:
##        print(city)

##for i, city in enumerate(cities):
##    print(f"City {i} is {city}")

##for i,city in enumerate(cities, start=2):
##    print(i,city)

##students = [
##    {"name": "Anna", "score": 80},
##    {"name": "Ben", "score": 90},
##    {"name": "Cara", "score": 85}
##]
##
##for i,s in enumerate(students, start=1):
##    print(f"{i}. {s['name']} score {s['score']}")

##features = ["ParcelA", "ParcelB", "ParcelC"]
##
##for i,feature in enumerate(features,start=1):
##    print(f"Processing parcel {i} with name {feature}.")

##parcels = [
##    {"parcel_id": "A101", "acreage": 0.8},
##    {"parcel_id": "A102", "acreage": 2.3},
##    {"parcel_id": "A103", "acreage": 1.7},
##    {"parcel_id": "A104", "acreage": 0.5},
##    {"parcel_id": "A105", "acreage": 1.5},
##]

##for i,parcel in enumerate(parcels):
##    if parcel["acreage"] > 1:
##        print(f"Parcel at position {i} ({parcel['parcel_id']}) is larger than one acre")

##for i,parcel in enumerate(parcels,start=1):
##    if i % 5 == 0:
##        print(f"{parcel['parcel_id']}")

"""Write a program that prints any parcel that is larger than the parcel immediately before it."""
##acreages = [0.8, 1.2, 0.9, 1.5, 1.6]
##
##for i,value in enumerate(acreages):
##    if i == 0:
##        continue
##    if value > acreages[i-1]:
##        print(f"Parcel {i} is larger than the previous parcel.")

parcels = [
    {"id":"A101","acreage":0.8},
    {"id":"A102","acreage":1.2},
    {"id":"A103","acreage":0.9},
    {"id":"A104","acreage":1.5}
]

for i,parcel in enumerate(parcels,start=1):
    if i==0:
        continue
    if parcel['acreage']>parcels[i-2]['acreage']:
        print(f"Parcel {parcel['id']} is larger than the previous parcel.")
