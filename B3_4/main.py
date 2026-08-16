from models.courses import Course
from models.students import Student
from models.subjects import Subject, SubjectList

# khai bao danh sach mon hoc cua tung hoc sinh (moi hoc sinh 1 SubjectList rieng)

subject_list1 = SubjectList()
subject_list2 = SubjectList()
subject_list3 = SubjectList()
subject_list4 = SubjectList()
subject_list5 = SubjectList()

# them 3 mon hoc cho hoc sinh 1
subject_list1.add_subject(Subject("Math", "Math for KID", 8, 9, 10))
subject_list1.add_subject(Subject("Python Co Ban", "Nhap mon lap trinh Python", 7, 8, 9))
subject_list1.add_subject(Subject("GameMaker Studio", "Lam game co ban voi GameMaker", 9, 9, 8))

# them 3 mon hoc cho hoc sinh 2
subject_list2.add_subject(Subject("Math", "Math for KID", 7, 6, 8))
subject_list2.add_subject(Subject("Python Co Ban", "Nhap mon lap trinh Python", 8, 7, 7))
subject_list2.add_subject(Subject("GameMaker Studio", "Lam game co ban voi GameMaker", 6, 7, 7))

# them 3 mon hoc cho hoc sinh 3
subject_list3.add_subject(Subject("Math", "Math for KID", 9, 10, 9))
subject_list3.add_subject(Subject("Python Co Ban", "Nhap mon lap trinh Python", 10, 9, 10))
subject_list3.add_subject(Subject("GameMaker Studio", "Lam game co ban voi GameMaker", 8, 9, 9))

# them 3 mon hoc cho hoc sinh 4
subject_list4.add_subject(Subject("Math", "Math for KID", 6, 7, 6))
subject_list4.add_subject(Subject("Python Co Ban", "Nhap mon lap trinh Python", 7, 6, 7))
subject_list4.add_subject(Subject("GameMaker Studio", "Lam game co ban voi GameMaker", 7, 8, 6))

# them 3 mon hoc cho hoc sinh 5
subject_list5.add_subject(Subject("Math", "Math for KID", 8, 8, 9))
subject_list5.add_subject(Subject("Python Co Ban", "Nhap mon lap trinh Python", 9, 8, 8))
subject_list5.add_subject(Subject("GameMaker Studio", "Lam game co ban voi GameMaker", 9, 8, 9))

# khai bao hoc sinh
student1 = Student("SV0001", "Nguyen Van A", "01/01/2000", subject_list1)
student2 = Student("SV0002", "Tran Thi B", "02/02/2001", subject_list2)
student3 = Student("SV0003", "Le Van C", "03/03/2002", subject_list3)
student4 = Student("SV0004", "Pham Thi D", "04/04/2003", subject_list4)
student5 = Student("SV0005", "Hoang Van E", "05/05/2004", subject_list5)

# khai bao lop
pti39 = Course("PTI39-Class", "Python App Producer Intensive for KID", "01/06/2026", 14)

# them hoc vien
pti39.add_student(student1)
pti39.add_student(student2)
pti39.add_student(student3)
pti39.add_student(student4)
pti39.add_student(student5)

print(pti39)

for student in pti39.get_student_list():
    print(student)
    print(f"GPA: {student.get_GPA()}")
    print("--------------------")
    
ranked_students = pti39.ranking_by_GPA(3)
if ranked_students:
    print("Top 3 students by GPA:")
    for i, student in enumerate(ranked_students):
        print(f"Rank {i+1}: {student.get_name()} - GPA: {student.get_GPA()}")