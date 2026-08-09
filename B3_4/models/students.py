class Student:
    def __init__(self, student_id, name, birthdate, subject_list):
        self.__student_id = student_id
        self.__name = name
        self.__birthdate = birthdate
        self.__subject_list = subject_list
        
    def __str__(self):
        return f"""
Student ID: {self.__student_id}
Name: {self.__name}
Birthdate: {self.__birthdate}
    """
# getter
    def get_C(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name
    
    def get_birthdate(self):
        return self.__birthdate
    
    def get_subject_list(self):
        return self.__subject_list


    # setter
    def set_student_id(self, student_id):
        if student_id and len(student_id) >= 6: self.__student_id = student_id
        else: raise ValueError("Student ID must be at least 6 characters long.")
        
    def set_name(self, name):
        if name: self.__name = name
        else: raise ValueError("Name cannot be empty.")
        
    def set_birthdate(self, birthdate):
        # check string format dd/mm/yyyy
        if len(birthdate) == 10 and birthdate[2] == '/' and birthdate[5] == '/':
            # check if the date is valid
            day, month, year = birthdate.split('/')
            if len(year) == 4 and  1 <= int(day) <= 31 and 1 <= int(month) <= 12:
                    self.__birthdate = birthdate
            else: raise ValueError("Invalid date format. Please use dd/mm/yyyy.")   
            
    def set_subject_list(self, subject_list:SubjectList):
        self.__subject_list = subject_list

    def GTA(self):
        pass











