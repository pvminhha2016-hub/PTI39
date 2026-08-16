from models.students import Student


class Course:
    def __init__(self, name, description, start_date, number_of_lessons):
        self.__name = name
        self.__description = description
        self.__student_list = []
        self.__start_date = start_date
        self.__number_of_lessons = number_of_lessons
        
    def __str__(self):
        return f"""
Course: {self.__name}
Description: {self.__description}
Start Date: {self.__start_date}
Number of Lessons: {self.__number_of_lessons}
Number of Students: {len(self.__student_list)}
    """
    
    # getter
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_student_list(self):
        return self.__student_list
    
    def get_start_date(self):
        return self.__start_date
    
    def get_number_of_lessons(self):
        return self.__number_of_lessons
    
    # setter
    def set_name(self, name):
        if name and len(name)>=6: self.__name = name
        else: raise ValueError("Name must be at least 6 characters long.")
        
    def set_description(self, description):
        if description: self.__description = description
        else: raise ValueError("Description cannot be empty.")
        
    def set_start_date(self, start_date):
        # check string format dd/mm/yyyy
        if len(start_date) == 10 and start_date[2] == '/' and start_date[5] == '/':
            # check if the date is valid
            day, month, year = start_date.split('/')
            if len(year) == 4 and  1 <= int(day) <= 31 and 1 <= int(month) <= 12:
                    self.__start_date = start_date
            else: raise ValueError("Invalid date format. Please use dd/mm/yyyy.")
            
    def set_number_of_lessons(self, number_of_lessons):
        if 4 < number_of_lessons < 30: self.__number_of_lessons = number_of_lessons
        else: raise ValueError("Number of lessons must be between 4 and 30.")
        
    # -----------------------
    # add student to course
    def add_student(self, student:Student):
        self.__student_list.append(student)
    
    # delete student from course
    def remove_student(self, student:Student):
        self.__student_list.remove(student)
    
    # get student list of course (read)
    def get_student_list(self):
        return self.__student_list
    
    # get student by id (read)
    def get_student_by_id(self, student_id):
        for student in self.__student_list:
            if student.get_student_id() == student_id:
                return student
        return None
    
    # get student_list by name (read)
    def get_student_list_by_name(self, name):
        # if name.lower() in student.get_name().lower(): kiem tra trong ten co ki tu khong? 
        return [student for student in self.__student_list if name.lower() in student.get_name().lower()]
    
    # ranking by GPA (read)
    def ranking_by_GPA(self, number_of_top_sudent:int = "3"):
        if 1 <= number_of_top_sudent <= len(self.__student_list):
            sorted_student = sorted(self.__student_list,
                                    key = lambda student: student.get_GPA(), 
                                    reverse= True)

            return sorted_student[:number_of_top_sudent]
        return None #so luongko hop le