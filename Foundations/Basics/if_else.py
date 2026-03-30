##import string
##
####land_use='Residential'
####land_use='Commercial'
####land_use='industrial'
##land_use='single family'
##acre=2.5
##if string.capwords(land_use) == "Single Family" or "Multi Family":
##    land_use="Residential"
##if string.capwords(land_use) == 'residential' or string.capwords(land_use) == 'commercial':
##    print(f"This is a {string.capwords(land_use)} parcel of {acre} acres")
##else:
##    print(f"Other parcel type ({string.capwords(land_use)}) of {acre} acres")

####land_use='Residential'
####land_use='Commercial'
####land_use='industrial'
##land_use='single family'
##acre=2.5
##landuse_title=land_use.title()
####if landuse_title == "Single Family" or landuse_title == "Multi Family":
##if landuse_title in ["Single Family","Multi Family"]:
##    landuse_title="Residential"
##if landuse_title == 'Residential' or landuse_title == 'Commercial':
##    print(f"This is a {landuse_title} parcel of {acre} acres")
##else:
##    print(f"Other parcel type ({landuse_title}) of {acre} acres")

land_use='industrial'
acre=2.5

landuse_title=land_use.title()

if landuse_title in ["Residential","Single Family","Multi Family"]:
    category = "Residential"
elif landuse_title == "Commercial":
    category = "Commercial"
else:
    category = landuse_title

if category in ["Residential","Commercial", "Industrial"]:
    print(f"This is a {category} parcel of {acre} acres")
else:
    print(f"Other parcel type ({category}) of {acre} acres")
