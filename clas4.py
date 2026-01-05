python_students={"alice","charlie","liza"}
data_science_students={"charlie","dave","mike"}
python_students.add("nina")
data_science_students.remove("dave")
both_courses=python_students & data_science_students
print("Students in both courses:", both_courses)
python_only=python_students - data_science_students
print("Students only in Python course:", python_only)
all_students=python_students | data_science_students
print("all entrolled students:", all_students)
cousre_students={
    "python": len(python_students),
    "data_science": len(data_science_students)
}
for course, count in cousre_students.items():
    print(f"course:{course},students:{count}")

    growth_projection={course:count*2 for course,count in cousre_students.items()}
print("growth projection:", growth_projection)
     
