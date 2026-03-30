##parcel_dict={}
##parcel_dict["parcel_id"]="P001"
##parcel_dict["owner"]="Alice"
##parcel_dict["acreage"]=2.5
##
##print(parcel_dict)
##print(parcel_dict["owner"])

parcel_dict={}
parcel_dict["001"]={
    "owner":"Alice",
    "acreage":2.5,
    "land_use":"Residential"
    }

##print(parcel_dict)

parcel_dict["002"]={
    "owner":"Betty",
    "acreage":4.0,
    "land_use":"Commercial"
    }

parcel_dict["003"]={
    "owner":"Craig",
    "acreage":7.0,
    "land_use":"Residential"
    }

##print(parcel_dict)
##print(parcel_dict["001"])
##print(parcel_dict["001"]["owner"])

##for key in parcel_dict:
##    if key == "001":
##        print(key)

##for p in parcel_dict.values():
##    if p["land_use"]=="Residential":
##        print(p)

##for parcel_id,p in parcel_dict.items():
##    if p["land_use"] == "Residential":
##        print(parcel_id, p)

##for parcel_id,p in parcel_dict.items():
##    if p["acreage"]>3:
##        print(parcel_id)

##selected_parcels=[]
##for parcel_id,p in parcel_dict.items():
##    if p["acreage"]>3:
##        selected_parcels.append(parcel_id)
##
##print(selected_parcels)

##selected_parcels=[
##    (parcel_id,p["owner"]) for parcel_id,p in parcel_dict.items()
##    if p["acreage"]>3
##    ]
##print(selected_parcels)

##selected_parcels=[
##    p["owner"] for p in parcel_dict.values()
##    if p["land_use"]=="Residential"
##    ]
##print(selected_parcels)

##selected_parcels=[
##    (parcel_id,p["owner"]) for parcel_id,p in parcel_dict.items()
##    if p["land_use"]=="Residential"
##    ]
##print(selected_parcels)

selected_parcels={
    parcel_id:p
    for parcel_id,p in parcel_dict.items()
    if p["land_use"]=="Residential" and p["acreage"]>3
    }
print(selected_parcels)
