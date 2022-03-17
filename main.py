from flask import Flask, request
from spartan import Spartan
from management import *
import json

web_app = Flask(__name__)

with open("spartan_data.json", "r") as data_file:
    spartans = json.load(data_file)
spartans = Spartan.format_object(spartans)

@web_app.route('/', methods=["GET"])
def home_page():
    return "---------Welcome to the Sparta-Trainee Management page!--------- \nThis is where all the Spartan's details will be managed using APIs." \
           " To begin with, here is a tutorial to clarify how APIs (Application Programming Interface) can be used:" \
           "\n\nThink of an API as the middleman between any two entities that want to connect with each other for a specified task." \
           " For example, each time you use an app like Facebook, when you sign in from your phone you are using an API call to tell the application" \
           " that you would like to access the account.\nYour API options are as follows:\n\n--- Type '/spartan/add' to add a new Spartan to the system." \
           "\n--- Type '/spartan/<spartan_id>' to view that particular Spartan's details. E.g if my ID is '1', I would view my details by typing '/spartan/1'." \
           "\n--- Type '/spartan/remove?id=sparta_id' to remove a Spartan from the system. E.g. to remove myself I would type '/spartan/remove?id=1'." \
           "\n--- Type '/spartan' to view a list of details of all the Spartans in the system. "

@web_app.route('/spartan/add', methods=["POST"])
def add_spartan():
    spartan = Spartan()
    spartan_data = request.json
    text1 = spartan.set_id(spartans, spartan_data["id"])
    if text1:
        return text1
    text2 = spartan.set_first_name(spartan_data["firstname"])
    if text2:
        return text2
    text3 = spartan.set_last_name(spartan_data["lastname"])
    if text3:
        return text3
    text4 = spartan.set_birth_day(spartan_data["birthday"])
    if text4:
        return text4
    text5 = spartan.set_birth_month(spartan_data["birthmonth"])
    if text5:
        return text5
    text6 = spartan.set_birth_year(spartan_data["birthyear"])
    if text6:
        return text6
    text7 = spartan.set_course(spartan_data["course"])
    if text7:
        return text7
    text8 = spartan.set_stream(spartan_data["stream"])
    if text8:
        return text8
    spartans[spartan.id] = spartan

    spartans_json = {}
    for key, value in spartans.items():
        spartans_json[key] = value.__dict__
    with open("spartan_data.json", "w") as jsonfile:  # jsonfile is the pointer to the file
        json.dump(spartans_json, jsonfile, indent=4)

    # Call the method that will create employee record
    return str(spartan)

@web_app.route('/spartan/<spartan_id>', methods=["GET"])
def spartan_record_getter(spartan_id):                     # must pass the changing variable as the parameter
    # Check the database. read from a file, etc till you get the data
    return retrieve(spartans, spartan_id)

# http://127.0.0.1:5000/spartan/remove?id=spartan_id
@web_app.route('/spartan/remove', methods=["GET"])
def spartan_remover():                     # must pass the changing variable as the parameter
    spartan_id = request.args.get("id")
    return remove(spartans, spartan_id)


@web_app.route('/spartan', methods=["GET"])
def list_getter():
    return list(spartans)

if __name__ == "__main__":
    web_app.run()
