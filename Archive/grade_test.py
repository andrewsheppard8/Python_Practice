#creates a list of integers based on a string value for a grade range
def grd_range(grd_range):

    mapping={"TK":-1,"K":0}
    grd_clean=grd_range.strip("()").replace(" ","")
    parts=grd_clean.split("-")
    start,end=(mapping[p] if p in mapping else int(p) for p in parts)

    # print(list(range(start,end+1)))

    return list(range(start,end+1))

#checks to see if a grade value exists within that list
def grd_check(grade,grd_range):
    if grade in grd_range:
        print("Grade within list")
    else:
        print("Grade not within list")
    return grade in grd_range

grade=4
grade_list=grd_range("(K-5)")
grd_check(grade,grade_list)
