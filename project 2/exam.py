total_working_days = int(input("Enter total number of working days: "))
days_absent = int(input("Enter total number of days absent: "))

days_attended = total_working_days - days_absent

attendance_percentage = (days_attended / total_working_days) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("The student is eligible to sit for the exam.")
else:
    print("The student is NOT eligible to sit for the exam.")