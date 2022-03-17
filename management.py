from spartan import *
import json


def add_spartan(self, spartans):
    self.set_id(spartans)
    self.set_first_name()
    self.set_last_name()
    self.set_birth_day()
    self.set_birth_month()
    self.set_birth_year()
    self.set_course()
    self.set_stream()


def remove_spartan():
    while True:
        removeid_str = input("Please Enter the Spartan ID that you want to remove: ")
        if removeid_str.isdigit():
            return removeid_str
        else:
            print("WARNING: Enter valid Spartan ID: ")


def retrieve_details():
    while True:
        retreiveid_str = input("Please Enter the ID of the Spartan's details you wish to Retrieve: ")
        if retreiveid_str.isdigit():
            return retreiveid_str
        else:
            print("WARNING: Enter valid Spartan ID: ")

def read_options(): # outside of class (not needed in class)
    valid_options = ["1", "2", "3", "4", "5"]
    while True:
        options_str = input("Please select an option: \n'1' to Add new Spartan \n'2' to Remove a Spartan\n"
                            "'3' to see a list of the Spartan(s)' details"
                            "\n'4' to Retrieve a Spartan's Data  \n'5' to Exit")

        options_str = options_str.strip()
        if options_str in valid_options:
            return options_str
        else:
            print("WARNING: Please Enter a Valid Option: ")

if __name__ == "__main__":

    spartans = {}

    try:
        with open("spartan_data.json", "r") as data_file:
            spartans = json.load(data_file)
        spartans = Spartan.format_object(spartans)

        print(spartans)
    except Exception as ex:
        print(ex)

    try:
        with open("user_action.txt", "a+") as fh:
            fh.write("\n---------User has Entered the System----------")
    except Exception as ex:
        print(ex)

    while True:
        options = read_options()  # access the 'read_options' method

        if options.lower() == "1":
            with open("user_action.txt", "a+") as fh:
                fh.write("\nUser chose to add a new Spartan details")
            spartan = Spartan()
            spartan.add_spartan(spartans)
            spartans[spartan.id] = spartan  # Spartan. is to access the class    # .spartans is to access dictionary
            # spartan.id is to be able to access details via id
            # spartan is the variable that stores this particular employee's details
            print(str(spartan))  # str returns all the __str__ data & print() prints it
            with open("user_action.txt", "a+") as fh:
                fh.write("\nUser added a new Spartan's details")

        elif options.lower() == "2":
            with open("user_action.txt", "a+") as fh:
                fh.write("\nUser chose to remove an Spartan's details")
            while True:
                remove_id = Spartan.remove_spartan()
                try:
                    del spartans[remove_id]
                    break
                except KeyError:  # KeyError is trying to look for a key in a dictionary that does not exist
                    print("This id does not exist")
            with open("user_action.txt", "a+") as fh:
                fh.write("\nUser removed an Spartan's details")

            print(f"Spartan with id {remove_id} is removed")

        elif options.lower() == "4":
            with open("user_action.txt", "a+") as fh:
                fh.write("\nUser chose to see a List of all Spartans' details")
            list_of_spartans = list(spartans.values())  # values are all the Spartans' details
            for spartan in list_of_spartans:
                print(str(spartan))

        elif options.lower() == "5":
            with open("user_action.txt", "a+") as fh:
                fh.write("\nUser chose to retrieve a Spartan's details")
            while True:
                retrieveID = Spartan.retrieve_details()
                try:
                    print(str(spartans[retrieveID]))
                    break
                except KeyError:
                    print("This id does not exist")
            with open("user_action.txt", "a+") as fh:
                fh.write("\nUser Retrieved a Spartan's details")

        else:
            for key, value in spartans.items():
                spartans[key] = value.__dict__
            with open("spartan_data.json", "w") as jsonfile:  # jsonfile is the pointer to the file
                json.dump(spartans, jsonfile, indent=4)