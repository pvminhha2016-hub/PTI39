class Subject:
    def __init__(self, name, description, check_point_1, check_point_2, final_exam):
        self.__name = name
        self.__description = description
        self.__check_point_1 = check_point_1
        self.__check_point_2 = check_point_2
        self.__final_exam = final_exam

    def __str__(self):
        return f"""
Subject: {self.__name}
Description: {self.__description}
    """


    def get_name(self):
       return self.__name
    def get_description(self):
        return self.__description
    def get_check_point_1(self):
        return self.__check_point_1
    def get_check_point_2(self):
            return self.__check_point_2
    def get_final_exam(self):
            return self.__final_exam


    def set_name(self, name):
         if name: self.__name = name
         else: raise ValueError("Name cannot be empty")
    def set_description(self, description):
         if description: self.__description =description
         else:  raise ValueError("description cannot be empty")
    def set_check_point_1(self, check_point_1):
         if  0 <= check_point_1  <= 10 : self.__name = check_point_1
         else: raise ValueError("check point1 must be between 0 and 10")
    def set_check_point_2(self, check_point_2):
             if  0 <= check_point_2  <= 10 : self.__name = check_point_2
             else: raise ValueError("check point1 must be between 0 and 10")
    def set_final_exam(self, final_exam):
             if  0 <= final_exam  <= 10 : self.__name = final_exam
             else: raise ValueError("check point1 must be between 0 and 10")

class SubjectList:
    def __init__(self):
            self.__subjects = []
    #update
    def add_subjects(self, subjects:Subject):
        self.__subjects.append(subjects)


    #read( xem danh sach mon hoc)
    def __str__(self):
          output = " Subject List:\n"
          #for subjects in self:
                #output += subjects + "\n--------------\n"
          return "subjects List:\n" + " ". join([subjects + "\n-----------------\n" for subjects in self.__subjects]) 

    #delete
    def remove_subjects(self, name):
        #duyet tung mon hoc de tim ten -> xoa
        for subjects in self.__subjects:
             if subjects.get_name() == name:
                  self.__subjects.remove(subjects)
                  print(f"Subject '{name}' has been removed")
                  return# ham ket thuc 

        print(f"Subject '{name}' not found ")
        