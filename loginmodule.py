from datetime import datetime

class CreateUser:
    def get_details(self):
        self.fname = input("Enter the first name:")
        self.lname = input("Enter the last name:")
        self.phone =int(input("Enter the phone number:"))
        self.dob = input("Enter the dob:")
        self.aadhar = int(input("Enter the aadhar number:"))
        self.generate_id_age(self.fname, self.lname, self.phone, self.dob)

    def generate_id_age(self, fname, lname, phone, dob):
        self.user_id = fname[:2] + lname[:2] + phone[4:]
        print("User ID:", self.user_id)
        self.sliced = dob[:4]
        self.current_date = datetime.now()
        self.system_date = self.current_date.strftime("%Y")
        self.age = int(self.system_date) - int(self.sliced)
        print("Age:", self.age)


class CheckAdmin:
    def check(self, username, password):
        if username == "admin123" and password == "password":
            print("Login done successfully")
            print("Welcome admin")
            options = input("Enter the options to proceed:")
            if options == "1":
                print("Create new user")
                create_user = CreateUser()
                create_user.get_details()
            elif options == "2":
                print("Transaction of user")
            else:
                print("Invalid option")
        else:
            print("The username or password is incorrect")


username = input("Enter the username:")
password = input("Enter the password:")
c1 = CheckAdmin()
c1.check(username, password)
