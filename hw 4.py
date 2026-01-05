frontend_students={"alice", "bob", "charlie"}
backend_students={"charlie", "dave", "eve"}
backend_students.add("frank")
frontend_students.remove("bob")
both_courses=frontend_students & backend_students
backend_only=backend_students - frontend_students
unique_students=frontend_students | backend_students
total_students=len(unique_students)

course_counts={
    "frontend": len(frontend_students),
    "backend": len(backend_students)
}
course_count_with_fullstack={
    **course_counts,
    "fullstack": course_counts["frontend"] + course_counts["backend"]
}
print("Students in both courses:", both_courses)
print("Students only in backend course:", backend_only)
print("Total unique students:", total_students)
print("course counts with fullstack:", course_count_with_fullstack)