## user : có full name, birthdate, email, passwork, username, gender
class User:
    def __init__(self, full_name, birthdate, email, passwork, username, gender):
        #TODO: khai bao  bien can dung
        self.__full_name = full_name
        self.__birthdate = birthdate
        self.__email = email
        self.__passwork = passwork
        self.__username = username
        self.__gender = gender

    def get_full_name(self, full_name):
        return self.__full_name

    def get_birthdate(self, birthdate):
        return self.__birthdate

    def get_username(self, username):
        return self.__username
           

    def get_passwork(self, passwork):
        return self.__passwork

    def get_email(self, email):
        return self.__email


    def set_passwork(self, passwork, old_passwork):
        if old_passwork  == self.__passwork:
            if len(passwork) > 6:
                self.__passwork = passwork
            else:
                print(" New passwork must be longer than 6 character")
        else:
            print(" old passwork is incorrect")
        







        # gender (male, female, other)
        def set_gender(self, gender):
            if gender in ['male', 'female', 'other']:
                self.__gender = gender # thay doi gia tri moi cho thuoc tinh gender
            else:
                print("Invalid gender. Please choose from 'male', 'female', or 'other'.")













        

