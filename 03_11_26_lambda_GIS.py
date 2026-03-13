##x=[1,2,3]
##y= list(map(lambda z:z*10,x))
##print(y)
##

##check_oddeven= lambda x: "Even" if x%2 ==0 else "Odd"
##print(check_oddeven(5))

##parcels = [
##    {"parcel_id": "A101", "acreage": 1.2},
##    {"parcel_id": "A102", "acreage": 0.4},
##    {"parcel_id": "A103", "acreage": 3.1},
##    {"parcel_id": "A104", "acreage": 0.9}
##]

##parcel_size=list(map(lambda x: "Big" if x["acreage"]>1 else "Small",parcels))
##print(parcel_size)

##parcel_size=list(map(lambda x: (x["parcel_id"], "Big" if x["acreage"] > 1 else "Not Big"),
##                     parcels))
##print(parcel_size)

##parcel_size= [p["parcel_id"] if p["acreage"] > 1 else "Small" for p in parcels]
##print(parcel_size)

##parcel_size = [p["parcel_id"] for p in parcels if p["acreage"]>1]
##print(parcel_size)

##students = [
##    {"name": "Alice", "score": 88},
##    {"name": "Bob", "score": 72},
##    {"name": "Charlie", "score": 95},
##    {"name": "Diana", "score": 64},
##    {"name": "Evan", "score": 91}
##]

##filtered_students=list(filter(lambda s:s["score"]>=80,students))
##print(filtered_students)

##filtered_students={s["name"]:s["score"] for s in students if s["score"] >= 80}
##print(filtered_students)

##filtered_students={s["name"]:s["score"] for s in students if s["score"] >= 80}
##sorted_students=sorted(filtered_students.items(), key=lambda x:x[1], reverse=True)
####print(sorted_students)
##
##for name,score in sorted_students:
##    print(f"{name} passed with a score of {score}.")

##[print(f'{s["name"]} passed with a score of {s["score"]}')
## for s in sorted(filter(lambda s:s["score"] >=  80, students),
##                 key=lambda s:s["score"], reverse=True)]

parcels = [
    {"parcel_id": "A101", "acreage": 12, "zone": "Residential"},
    {"parcel_id": "A102", "acreage": 4, "zone": "Commercial"},
    {"parcel_id": "A103", "acreage": 31, "zone": "Residential"},
    {"parcel_id": "A104", "acreage": 9, "zone": "Industrial"},
    {"parcel_id": "A105", "acreage": 25, "zone": "Commercial"},
    {"parcel_id": "A106", "acreage": 18, "zone": "Residential"}
]

##filtered_parcels=list(filter(lambda s:s["acreage"] > 1,parcels))
filtered_parcels=[p for p in parcels if p["acreage"] > 1]
##print(filtered_parcels)
zones=set(p["zone"] for p in filtered_parcels)
grouped_parcels={zone:[p for p in filtered_parcels if p["zone"] == zone] for zone in zones}
##print(grouped_parcels)
for zone,parcels_list in grouped_parcels.items():
    parcels_list.sort(key=lambda p:p["acreage"],reverse=True)
print(grouped_parcels)
zone_totals={
    zone: sum(p["acreage"] for p in parcels)
    for zone,parcels in grouped_parcels.items()
}

print(zone_totals)

filtered_parcels=[p for p in parcels if p["acreage"]>10]
zones=set(p["zone"] for p in filtered_parcels)
grouped_parcels={zone:[p for p in filtered_parcels if p["zone"] == zone] for zone in zones}
for zone,parcel_list in grouped_parcels.items():
    parcel_list.sort(key=lambda p:p["acreage"],reverse=True)

for x,y in grouped_parcels.items():
    y.sort(key=lambda z:z["acreage"], reverse=True)


zone_totals={
    zone: sum(p["acreage"] for p in parcels)
    for zone,parcels in grouped_parcels.items()
}
print(zone_totals)
