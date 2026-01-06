attendance=[18,20,19,15,21]
full_days=0
total_attendance=0
for students in attendance:
    total_attendance += students
    if students>=20:
        print("full")
        full_days += 1
    else:
        print("not full")
print("Number of full days:", full_days)
print("Total attendance:", total_attendance)