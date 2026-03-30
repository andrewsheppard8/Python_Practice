##numbers = [1, 2, 3, 2, 1, 4]
##unique_num=set(numbers)
##print(unique_num)

##land_uses = ["Residential", "Commercial", "Residential", "Industrial"]
##unique_landuse=set(land_uses)
##print(unique_landuse)

##parcels = [
##    (1, "Residential"),
##    (2, "Commercial"),
##    (3, "Residential"),
##    (4, "Industrial"),
##    (5, "Industrial")
##]
##
##unique_parcels={landuse for id_num,landuse in parcels}
##
##for t in unique_parcels:
##    count=0
##    for id_num,landuse in parcels:
##        if landuse==t:
##            count+=1
##    print(f"{t} occurs {count} times in parcels")

##parcels = [
##    {"id": 1, "land_use": "Residential"},
##    {"id": 2, "land_use": "Commercial"},
##    {"id": 3, "land_use": "Residential"},
##    {"id": 4, "land_use": "Industrial"},
##    {"id": 5, "land_use": "Industrial"},
##    {"id": 6, "land_use": "Residential"}
##    ]

##all_landuse=[parcel["land_use"] for parcel in parcels]
##print(all_landuse)
##unique_landuse=set(all_landuse)
##print(unique_landuse)
##
##unique_landuse={parcel["land_use"] for parcel in parcels} #set comprehension
##print(unique_landuse)

"""basic counter for counting land use types"""
##for t in unique_landuse:
##    count = 0
##    for parcel in parcels:
##        if parcel["land_use"]==t:
##            count += 1
##    print(f"{t} occurs {count} times in parcels")
##
##unique_landuse={parcel["land_use"] for parcel in parcels}

"""print how often land use types occur in this list"""
##landuse_counts={landuse:sum(parcel["land_use"]==landuse for parcel in parcels) for landuse in unique_landuse}
####print("Parcel counts by land use:",landuse_counts)
####for landuse,count in landuse_counts.items():
####    print(f"{landuse} has a total of {count} parcels")
##for land_use in sorted(landuse_counts):
##    print(f"{land_use}: {landuse_counts[land_use]} parcels")

parcels = [
    {"id": 1, "land_use": "Residential", "zone": "A"},
    {"id": 2, "land_use": "Commercial",  "zone": "B"},
    {"id": 3, "land_use": "Residential", "zone": "A"},
    {"id": 4, "land_use": "Industrial",  "zone": "B"},
    {"id": 5, "land_use": "Industrial",  "zone": "B"},
    {"id": 6, "land_use": "Commercial",  "zone": "B"},
    {"id": 7, "land_use": "Residential", "zone": "C"},
]

"""print how often land use and zone types occur in this list"""
##unique_landuse={parcel["land_use"] for parcel in parcels}
##unique_zone={parcel["zone"] for parcel in parcels}
##
##landuse_count={landuse:sum(parcel["land_use"]==landuse for parcel in parcels) for landuse in unique_landuse}
##for landuse,count in landuse_count.items():
##    print(f"{landuse} has {count} parcels")
##zone_count={zone:sum(parcel["zone"]==zone for parcel in parcels) for zone in unique_zone}
##for zone,count in zone_count.items():
##    print(f"{zone} has {count} parcels")

"""for Residential parcels, how often do different zone types occur"""
##parcel_lst=[parcel for parcel in parcels if parcel["land_use"]=="Residential"]
####unique_zones={parcel["zone"] for parcel in parcels} #if a list of all possible zone types, regardless of Residential status, are desired
##unique_zones={parcel["zone"] for parcel in parcel_lst}
##zone_count={zone:sum(parcel["zone"]==zone for parcel in parcel_lst) for zone in unique_zones}
##for zone,count in zone_count.items():
##    print(f"Residential parcels with a zone of {zone} occur {count} times in this group")

"""counting land use per zone for ALL land uses"""
unique_landuse={parcel["land_use"] for parcel in parcels}
unique_zone={parcel["zone"] for parcel in parcels}
landuse_zone_counts={
    lu:{zone:sum(parcel["land_use"]==lu and parcel["zone"]==zone for parcel in parcels)
        for zone in unique_zone}
    for lu in unique_landuse
    }

for lu,zones in landuse_zone_counts.items():
    print(f"{lu}:")
    for zone,count in zones.items():
        print(f" Zone {zone}: {count}")
        

