##for i in range(1,11,1):
##    print(i)

##for i in range (1,21,1):
##    if i%2==0:
##        print(i)

##x=5
##while x>0:
##    print(x)
##    x=x-1

##x=10
##while x>0:
##    if x%2==0:
##        print(x)
##    x=x-1

##x=10
##while x>0:
##    print(x)
##    x=x-2

##total=0
##while True:
##    try:
##        num_input=int(input("Give me a number: "))
##    except ValueError:
##        print("Enter a number, not a letter")
##        continue
##    if num_input<0:
##        print("Must be greater than zero")
##        continue
##    if num_input==0:
##        break
##    total += num_input
##    print(f"Running total is {total}")
##print(f"Final total is {total}")

##parcels = {
##    "P001": {"acres": 1.2, "land_use": "Residential"},
##    "P002": {"acres": -0.5, "land_use": "Commercial"},
##    "P003": {"acres": "3.1", "land_use": "Industrial"},
##    "P004": {"acres": 0, "land_use": "Residential"},
##}
##
##for parcel_id, data in parcels.items():
##    try:
##        acres=float(data["acres"])
##    except ValueError:
##        print(f"{parcel_id} has an invalid acreage (not a number)")
##        continue
##    if acres<0:
##        print(f"{parcel_id} has an invalid acreage (negative)")
##    elif acres==0:
##        print(f"{parcel_id} has an invalid acreage (zero)")
##    else:
##        print(f"{parcel_id} is valid")
##    if acres<0:
##        print(f"{parcel_id} has an invalid acreage (negative)")
##        continue
##    if acres==0:
##        print(f"{parcel_id} has an invalid acreage (zero)")
##        continue
##    print(f"{parcel_id} is valid")

##parcel_acres = [1.2, -0.5, 0, 50.0, 3.5, 7.8, 10.0, 2.1, 6.3]
##
##stop_threshold = 50  # if a parcel is >= this, stop processing
##count = 0
##
##for indx, acres in enumerate(parcel_acres, start=1):
##    if acres <= 0:
##        print(f"Skipping invalid parcel at index {indx}: {acres} acres")
##        continue
##    if acres >= stop_threshold:
##        print(f"Stopping loop at index {indx} for parcel with {acres} acres")
##        break
##    print(f"Processing parcel at index {indx}: {acres} acres")
##    count+=1
##
##print(f"Total valid parcels: {count}")

parcels = {
    "P001": {"acres": 1.2, "land_use": "Residential"},
    "P002": {"acres": -0.5, "land_use": "Commercial"},
    "P003": {"acres": "3.1", "land_use": "Industrial"},
    "P004": {"acres": 0, "land_use": "Residential"},
    "P005": {"acres": 7.8, "land_use": "Commercial"},
    "P006": {"acres": 50.0, "land_use": "Industrial"},  # stop threshold
    "P007": {"acres": 2.1, "land_use": "Residential"}
}

##stop_threshold=50
##processed_count=0
##total_acres=0
##
##parcel_keys=list(parcels.keys())
##indx=0
##
##while indx < len(parcel_keys):
##    parcel_id = parcel_keys[indx]
##    data=parcels[parcel_id]
##    try:
##        acres=float(data["acres"])
##    except ValueError:
####        print(f"Skipping parcel {parcel_id} at index {indx+1}: invalid acreage (not a number)")
##        indx+=1
##        continue
##    if acres<=0:
####        print(f"Skipping parcel {parcel_id} at index {indx+1}: invalid acreage (less than or equal to zero)")
##        indx+=1
##        continue
##    elif acres>=stop_threshold:
##        print(f"Stopping at parcel {parcel_id} at index {indx+1}: exceeds stop threshold for acreage size")
##        break
##    else:
##        total_acres+=acres
##        print(f"Processing parcel {parcel_id} at index {indx+1}: {acres} acres")
##        processed_count+=1
##        indx+=1
##print(f"total acres before stopped value: {total_acres}")
##print(f"Total valid parcels processed: {processed_count}")

stop_threshold = 50
processed_count = 0
total_acres = 0

# Pythonic for loop with enumerate to get index + parcel ID
for idx, parcel_id in enumerate(parcels, start=1):
    data = parcels[parcel_id]

    try:
        acres = float(data["acres"])
    except ValueError:
        print(f"Skipping parcel {parcel_id} at index {idx}: invalid acreage (not a number)")
        continue

    if acres <= 0:
        print(f"Skipping parcel {parcel_id} at index {idx}: invalid acreage (<= 0)")
        continue

    if acres >= stop_threshold:
        print(f"Stopping at parcel {parcel_id} at index {idx}: exceeds stop threshold ({acres} acres)")
        break

    # Valid parcel
    total_acres += acres
    processed_count += 1
    print(f"Processing parcel {parcel_id} at index {idx}: {acres} acres")

# Summary
print(f"\nTotal acres before stop threshold: {total_acres}")
print(f"Total valid parcels processed: {processed_count}")
