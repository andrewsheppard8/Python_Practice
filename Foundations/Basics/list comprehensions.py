##parcels = {
##    "P001": 3200,
##    "P002": 5400,
##    "P003": 7800,
##    "P004": 4100,
##    "P005": 6000
##}

##for parcel,size in parcels.items():
##    if size > 5000:
##        print(f"Parcel {parcel} is greater than 5000")

##large_parcels=[parcel for parcel,size in parcels.items() if size>5000]
##print(large_parcels)

##large_parcels=[size*0.092903 for parcel,size in parcels.items() if size>5000]
##print(large_parcels)

##large_parcels=[
##    (parcel,round(size*0.092903))
##    for parcel, size in parcels.items()
##    if size>5000]
##print(large_parcels)

##large_parcel_str=[f"Parcel {parcel} is {round(size*0.092903)} sq m"
##                  for parcel,size in parcels.items()
##                  if size>5000]
####print(large_parcel_str)
##for line in large_parcel_str:
##    print(line)

##for parcel,size in parcels.items():
##    if size>5000:
####        print(f"Parcel {parcel} is {size} sq m")
##        size_sqm=round(size*0.092903,2)
##        print(f"Parcel {parcel} is {size_sqm} sq m")

##parcels = {
##    "P001": {"acres": 0.5, "land_use": "Residential"},
##    "P002": {"acres": 1.3, "land_use": "Commercial"},
##    "P003": {"acres": 0.8, "land_use": "Residential"},
##    "P004": {"acres": 2.0, "land_use": "Industrial"},
##    "P005": {"acres": 1.5, "land_use": "Commercial"}
##}

##for parcel,attributes in parcels.items():
##    if attributes["land_use"] == "Commercial":
##        print(f"{parcel}")

##parcel_lst=[(parcel,attributes) for parcel,attributes in parcels.items() if attributes["land_use"]=="Commercial"]

##parcel_lst=[
##    {
##        "id": parcel,
##        "area_sqm": round(attributes["acres"]*4046.85642,2),
##        "land_use": attributes["land_use"]
##        }
##    for parcel,attributes in parcels.items()
##    if attributes["land_use"] == "Commercial" and attributes["acres"]*4046.85642>4000]
##
##parcel_sorted= sorted(
##    parcel_lst,
##    key=lambda x:x["area_sqm"],
##    reverse=True
##    )#sort based on size, key function is how to sort based on a specific field
##
##for parcel in parcel_sorted:
##    print(f"Parcel {parcel['id']} is {parcel['area_sqm']} sq m ({parcel['land_use']})")

parcels = {
    "P001": {"acres": 0.5, "land_use": "Residential", "population": 2},
    "P002": {"acres": 1.3, "land_use": "Commercial", "population": 0},
    "P003": {"acres": 0.8, "land_use": "Residential", "population": 4},
    "P004": {"acres": 2.0, "land_use": "Industrial", "population": 0},
    "P005": {"acres": 1.5, "land_use": "Commercial", "population": 0}
}

parcel_lst=[
    {
        "id":parcel,
        "area_sqm": round(attributes['acres']*4046.856452,2),
        "population": attributes['population']
        }
    for parcel,attributes in parcels.items()
    if attributes['acres']*4046.85642>2000 and attributes['land_use']=="Residential"]

##for parcel in parcel_lst:
##    print(parcel)

parcel_sorted=sorted(
    parcel_lst,
    key=lambda x:x['area_sqm'],
    reverse=True
    )

total_pop=sum(p['population'] for p in parcel_sorted)

for p in parcel_sorted:
    print(f"Parcel {p['id']} has a size of {p['area_sqm']} with a population of {p['population']}")
print(f"Total population of residential parcels more than 2000 sq m in size: {total_pop}")

