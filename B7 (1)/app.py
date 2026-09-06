from PyQt6.QtWidgets import QApplication, QListWidgetItem, QMessageBox, QMainWindow
import sys
from PyQt6 import uic
import os
import json

class User:
    def __init__(self, username, email, age, grade):
            self.__username = username
            self.__email = email
            self.__age = age
            self.__grade = grade

    # setters
    def set_username(self, username):
        if len(username) < 6:
            raise ValueError("Username must be at least 3 characters long.")
        self.__username = username

    def set_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")
        self.__email = email
        
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age must be a positive integer.")
        self.__age = age
        
    def set_grade(self, grade):
        self.__grade = grade

    def get_username(self):
          return self.__username
    def get_email(self):
              return self.__email
    def get_age(self):
              return self.__age
    def get_grade(self):
              return self.__grade

    # print
    def __str__(self):
        # hiển thị vào list widget
        return f"Username: {self.__username} - Grade: {self.__grade}"
class UserManager:
    def __int__(self):
         self.users = []
    # CRUD
    #del
    def delete_user(self, email):
          for user in self.user:
                if user.get_email() == email:
                      self.user.remove(user)
                      return True
                return False

    #get all
    def get_all_user(self):
          return self.user
    # search user
    def search_user(self, keyword):
        # tim = grade / username 
        if keyword == "":
            return self.users
        else:
            results = []
            for user in self.users:
                if keyword.lower() in user.get_username().lower() or keyword.lower() in user.get_grade().lower():
                    results.append(user)
            return results
        #add
    def add_user(self, user:User):
         self.__users.append(user)
    def edit_user(self, new_user:User):
        for user in self.user:
              if user.get_email()  == new_user.get_email:
                   user.set_username(new_user.get_username())
                   user.set_age(new_user.get_age())
                   user.set_grade(new_user.get_grade())
                   return True
        return False
# save to JSON -----------------------------
    def save_to_json(self, filename):
        data = []
        for user in self.users:
            data.append({
                "username": user.get_username(),
                "email": user.get_email(),
                "age": user.get_age(),
                "grade": user.get_grade()
            })
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            
    # load from JSON -----------------------------
    def load_from_json(self, filename):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            data = json.load(f)
            for user_data in data:
                user = User(
                    user_data["username"],
                    user_data["email"],
                    user_data["age"],
                    user_data["grade"]
                )
                self.users.append(user)
class HomeWindow(QMainWindow):
    def __int__(self):
        super().__init__()
        uic.loadUi("home.ui", self)
        #khai bao list
        self.user_manager = UserManager()
        #khai bao list  wide
        self.load_users()

        #conner
        self.add_btn.clicked.connect(self.open_add_window)
        self.edit_btn.clicked.connect(self.open_edit_window)
        self.delete_btn.clicked.connect(self.delete_user)
        self.search_user_input.returnPressed.connect(self.search_user)

    def load_user(self):
          self.user_manager.load_from_json("user.json")
          for user in self.user_manager.get_all_user():
               item = QListWidgetItem(str(user))
               self.listWidget.addItem(item)

    def open_add_window(self):
        # mo cua so edit o tren cung
        self.add_window = EditWindow(isEdit=False, user_manager=self.user_manager, parent=self)
        self.add_window.show()

    def open_edit_window(self):
        selected_item = self.listWidget.selectedItem()
        # neu chua chon user nao trong danh sach -> loi
        if not selected_item:
            QMessageBox.warning(self, "Warning", "Please select a user to edit.")
            return
        # lay index cua user duoc chon trong list widget
        selected_index = self.listWidget.row(selected_item)
        # lay user tu danh sach user thong qua index
        user = self.user_manager.get_all_users()[selected_index]
        self.edit_window = EditWindow(isEdit=True, user=user, user_manager=self.user_manager, parent=self)
        self.edit_window.show()
    def delete_user(self):
        selected_item = self.listWidget.selectedItem()
        if not selected_item:
            QMessageBox.warning(self, "Warning", "Please select a user to delete.")
            return
        selected_index = self.listWidget.row(selected_item)
        user = self.user_manager.get_all_users()[selected_index]
        # hien thi message box hoi de chac chan xoa hay khong
        confirm = QMessageBox.question(self, "Confirm Delete", f"Are you sure you want to delete {user.get_username()}?")
        if confirm == QMessageBox.StandardButton.Yes:
            self.user_manager.delete_user(user.get_email())
            self.listWidget.takeItem(selected_index)
            # sua lai danh sach luu trong file json
            self.user_manager.save_to_json("users.json")


    def search_user(self):
        # enter de tim kiem user theo grade hoac username
        keyword = self.search_input.text()
        results = self.user_manager.search_user(keyword)
        # xoa danh sach dang hien thi -> hien thi lai danh sach tim kiem 
        self.listWidget.clear()
        self.listWidget.addItems([str(user) for user in results])
class EditWindow(QMainWindow):
    def __init__(self, isEdit=False, user = None, user_manager=None, parent=None):
        super().__init__(parent)
        uic.loadUI("edit.Ui", self)
        self.isEdit = isEdit
        self.unser = user
        self.user_manager = user_manager

        if self.isEdit:
                self.setWindowTitle("edit user")
                self.Load_current_user()
                self.save_btn.clicked.connect(self.edit_user)
        else:
            self.setWindowTitle("Add user")
            self.setWindowTitle("add new user")


    def add_user(self):
        try:
            # Cắt khoảng trắng thừa
            username = self.username.text().strip()
            email = self.email.text().strip()
            age = int(self.age.text().strip())
            grade = self.grade.text().strip()

            # Kiểm tra dữ liệu nhập vào
            self.__validate_form(email, username, age, grade)

            # Tạo user mới
            new_user = User(username, email, age, grade)

            # Thêm vào danh sách user
            if self.user_manager:
                self.user_manager.add_user(new_user)

                # Hiển thị trên ListWidget
                item = QListWidgetItem(str(new_user))
                self.parent().listWidget.addItem(item)

                # Lưu vào JSON
                self.user_manager.save_to_json("users.json")

                # Đóng cửa sổ
                self.close()

        except ValueError as e:
            # Hiển thị nội dung lỗi trong MessageBox
            QMessageBox.warning(self, "Warning", str(e))

    def load_current_user(self):
        # phai kiem tra user != none -> lam tiep
        if self.user:
            self.username.setText(self.user.get_username())
            self.email.setText(self.user.get_email())
            self.age.setValue(self.user.get_age())
            self.grade.setCurrentText(self.user.get_grade())
            # disable email input -> khong cho chinh sua email
            self.email.setDisabled(True)

    def edit_user(self):
       
        try:
            # Cắt khoảng trắng thừa
            username = self.username.text().strip()
            email = self.email.text().strip()
            age = int(self.age.text().strip())
            grade = self.grade.text().strip()

            # Kiểm tra dữ liệu nhập vào
            self.__validate_form(email, username, age, grade)

            # edit user
            new_user = User(username, email, age, grade)

            # Sua o danh sách user
            if self.user_manager:
                self.user_manager.edit_user(new_user)

                # Hiển thị trên ListWidget (xoa item cu va them item moi)
                selected_item = self.parent().listWidget.selectedItems()[0]
                self.parent().listWidget.takeItem(self.parent().listWidget.row(selected_item))
                item = QListWidgetItem(str(new_user))
                self.parent().listWidget.addItem(item)

                # Lưu vào JSON
                self.user_manager.save_to_json("users.json")

                # Đóng cửa sổ
                self.close()

        except ValueError as e:
            # Hiển thị nội dung lỗi trong MessageBox
            QMessageBox.warning(self, "Warning", str(e))

    def __validate_form(self, email, username, age, grade):
        # kiem tra cac truong du lieu nhap vao
        if not email or not username or not grade or not age:
            raise ValueError("Please fill in all fields.")
        if len(username) < 6:
            raise ValueError("Username must be at least 6 characters long.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")
        if age < 0:
            raise ValueError("Age must be a positive integer.")
        return True 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec())

