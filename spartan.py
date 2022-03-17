class Spartan:

    def __init__(self):
        self.id = None
        self.firstname = ""
        self.lastname = ""
        self.birthday = None
        self.birthmonth = None
        self.birthyear = None
        self.course = ""
        self.stream = ""


    def read_id(self, spartans):
        while True:
            try:
                self.id = int(input("Please Enter a Spartan ID: "))
            except ValueError:
                print("The ID should only contain digits")
                continue   # continue brings you back to the top of the loop to try again
            if self.id not in spartans.keys():
                return self.id
            else:
                print("This ID is already taken")


    def read_first_name(self):
        while True:
            self.firstname = input(f"Please Enter The First Name: ")
            if len(self.firstname.strip()) > 1:
                self.firstname = str(self.firstname)
                break
            else:
                print("Name must be a minimum of 2 characters")

    def read_last_name(self):
        while True:
            self.lastname = input(f"Please Enter The Last Name: ")
            if len(self.lastname.strip()) > 1:
                self.lastname = str(self.lastname)
                break
            else:
                print("Name must be a minimum of 2 characters")

    def read_birth_day(self):
        while True:
            self.birthday = input("Please Enter the Spartan's Birth Day: ")
            self.birthday = self.birthday.strip()
            if self.birthday.strip():
                self.birthday = int(self.birthday)
                if (self.birthday >= 1) and (self.birthday <= 31):
                    break
                else:
                    print("Employee Birth Day must be between 1 and 31")
            else:
                print("Employee Birth Day must contain only digits")

    def read_birth_month(self):
        while True:
            self.birthmonth = input("Please Enter the Spartan's Birth Month: ")
            self.birthmonth = self.birthmonth.strip()
            if self.birthmonth.isdigit():
                self.birthmonth = int(self.birthmonth)
                if (self.birthmonth >= 1) and (self.birthmonth <= 12):
                    break
                else:
                    print("Birth Month must be between 1 and 12")
            else:
                print("Birth Month must contain only digits")

    def read_birth_year(self):
        while True:
            self.birthyear = input("Please Enter the Spartan's Birth Year: ")
            self.birthyear = self.birthyear.strip()
            if self.birthyear.isdigit():
                self.birthyear = int(self.birthyear)
                if (self.birthyear >= 1900) and (self.birthyear <= 2004):
                    break
                else:
                    print("Birth Year must be between 1900 and 2004")
            else:
                print("Birth Year must contain only digits")

    def read_course(self):
        while True:
            self.course = input("Please Enter The Spartan's Course Name:")
            if len(self.course.strip()) > 0:
                self.course = str(self.course)
                break
            else:
                print("WARNING: Enter Valid Course Name")

    def read_stream(self):
        while True:
            self.stream = input("Please Enter The Spartan's Stream Name:")
            if len(self.stream.strip()) > 0:
                self.stream = str(self.stream)
                break
            else:
                print("WARNING: Enter Valid Stream Name")

    def __str__(self):
        text = f"Spartan ID: {self.id} \nSpartan First Name: {self.firstname.capitalize().strip()} " \
               f"\nSpartan Last Name: {self.lastname.capitalize().strip()}\nSpartan Birth Date: {self.birthday}/" \
               f"{self.birthmonth}/{self.birthyear} \nSpartan Course Name: {self.course.capitalize().strip()}" \
               f"\nSpartan Stream Name: {self.stream.capitalize().strip()}"

        return text

    @staticmethod
    def format_object(spartans):
        for key, value in spartans.items():
            spartan = Employee()
            spartan.firstname = value["firstname"]
            spartan.lastname = value["lastname"]
            spartan.birthday = value["birthday"]
            spartan.birthmonth = value["birthmonth"]
            spartan.birthyear = value["birthyear"]
            spartan.id = value["id"]
            spartan.position = value["position"]
            spartan.graduate = value["graduate"]
            spartans[key] = spartan
        return spartans


