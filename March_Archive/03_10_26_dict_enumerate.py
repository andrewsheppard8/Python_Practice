####students = ["Alice"]
####scores = [88]
##
##students = ["Alice", "Bob", "Charlie", "David"]
##scores = [88, 92, 79, 95]
##
##my_dict=dict(zip(students,scores))
##
####for index,(student,score) in enumerate(my_dict.items()):
####    print(f"Index {index}: {student} has score {score}")
##
##grades = {
##    student: ('A' if score >= 90 else
##              'B' if score >= 80 else
##              'C' if score >= 70 else
##              'F')
##    for student, score in my_dict.items()
##    }
##
####for student,grade in grades.items():
####    if grade=='A':
####        score=my_dict[student]
####        print(f"These students have an A: {student} with a score {score}")
##
####for student,score in my_dict.items():
####    grade = grades[student]
####    if grade == 'A':
####        print(f"These students have an A: {student} with a {score}")
##
####for idx, (student, score) in enumerate(my_dict.items(), start=1):
####    if grades[student] == 'A':
####        print(f"{idx}. These students have an A: {student} with a score {score}")
##
###start used to redefine first value in list from 0 to 10 in this case
##[print(f"{idx}. These students have an A: {student} with a score {my_dict[student]}")
## for idx, (student, grade) in enumerate(grades.items(), start=10) if grade == 'A']

students = ["Alice", "Bob", "Charlie", "David"]
scores = [88, 92, 79, 95]

# zip lists into a dictionary (like a table)
my_dict = dict(zip(students, scores))

# enumerate over items, calculate grade inline, filter like a SQL WHERE
for idx, (student, score) in enumerate(my_dict.items(), start=1):
    # inline SQL-style CASE logic
    grade = (
        'A' if score >= 90 else
        'B' if score >= 80 else
        'C' if score >= 70 else
        'F'
    )
    # filter like a SQL WHERE clause
    if grade == 'A':
        print(f"{idx}. {student} has an A with a score {score}")


