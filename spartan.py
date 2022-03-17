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


    def set_id(self, spartans, id):
        text = ""
        if id in spartans.keys():
            text = "Id already in use."
        try:
            id = int(id)
        except:
            text = "Please enter a number."
        self.id = id
        return text

    def get_id(self):
        return self.id


    def set_first_name(self, firstname):
        text = ""
        if firstname.isdigit():
            text = "Please enter letters only for the first name."
        if len(firstname.strip()) <= 1:
            text = "First name needs to be at least 2 characters."
        self.firstname = firstname
        return text

    def get_first_name(self):
        return self.firstname

    def set_last_name(self, lastname):
        text = ""
        if lastname.isdigit():
            text = "Please enter letters only for the last name."
        if len(lastname.strip()) <= 1:
            text = "Last name needs to be at least 2 characters."
        self.lastname = lastname
        return text

    def get_last_name(self):
        return self.lastname

    def set_birth_day(self, birthday):
        text = ""
        try:
            birthday = int(birthday)
        except ValueError:
            text = "Please enter only digits for the Birth Day."
            return text
        if not ((birthday >= 1) and (birthday <= 31)):
            text = "Employee Birth Day must be between 1 and 31"
        self.birthday = birthday
        return text

    def get_birth_day(self):
        return self.birthday

    def set_birth_month(self, birthmonth):
        text = ""
        try:
            birthmonth = int(birthmonth)
        except ValueError:
            text = "Please enter only digits for the Birth Month."
            return text
        if not ((birthmonth >= 1) and (birthmonth <= 12)):
            text = "Employee Birth Month must be between 1 and 12"
        self.birthmonth = birthmonth
        return text

    def get_birth_month(self):
        return self.birthmonth

    def set_birth_year(self, birthyear):
        text = ""
        try:
            birthyear = int(birthyear)
        except ValueError:
            text = "Please enter only digits for the Birth Year."
            return text
        if not ((birthyear >= 1900) and (birthyear <= 2004)):
            text = "Employee Birth Year must be between 1900 and 2004"
        self.birthyear = birthyear
        return text

    def get_birth_year(self):
        return self.birthyear

    def set_course(self, course):
        text = ""
        if course.isdigit():
            text = "Please enter letters only for the course."
        if len(course.strip()) <= 0:
            text = "Course name needs to be at least 1 character."
        self.course = course
        return text

    def get_course(self):
        return self.course

    def set_stream(self, stream):
        text = ""
        if stream.isdigit():
            text = "Please enter letters only for the stream."
        if len(stream.strip()) <= 0:
            text = "Stream needs to be at least 1 character."
        self.stream = stream
        return text

    def get_stream(self):
        return self.stream

    def __str__(self):
        text = f"Spartan ID: {self.id} \nSpartan First Name: {self.firstname.capitalize().strip()} " \
               f"\nSpartan Last Name: {self.lastname.capitalize().strip()}\nSpartan Birth Date: {self.birthday}/" \
               f"{self.birthmonth}/{self.birthyear} \nSpartan Course Name: {self.course.capitalize().strip()}" \
               f"\nSpartan Stream Name: {self.stream.capitalize().strip()}"

        return text

    @staticmethod
    def format_object(spartans):
        for key, value in spartans.items():
            spartan = Spartan()
            spartan.firstname = value["firstname"]
            spartan.lastname = value["lastname"]
            spartan.birthday = value["birthday"]
            spartan.birthmonth = value["birthmonth"]
            spartan.birthyear = value["birthyear"]
            spartan.id = value["id"]
            spartan.course = value["course"]
            spartan.stream = value["stream"]
            spartans[key] = spartan
        return spartans


