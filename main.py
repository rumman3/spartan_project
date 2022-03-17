from flask import Flask, request, jsonify
from spartan import Spartan
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
    spartan_data = request.json
    spartan_id = spartan_data['s_id']
    first_name = spartan_data['f_name']
    last_name = spartan_data['l_name']
    birth_day = spartan_data['b_day']
    birth_month = spartan_data['b_month']
    birth_year = spartan_data['b_year']
    course = spartan_data['course']
    stream = spartan_data['stream']
    # Call the method that will create employee record
    return f"The Spartan with the following details will be added to the system:\nID: {spartan_id}\nFirst Name: {first_name}\nLast Name: {last_name}" \
           f"\nBirth Date: {birth_day}/{birth_month}/{birth_year}\nCourse: {course}\nStream: {stream}"

@web_app.route('/spartan/<spartan_id>', methods=["GET"])
def spartan_record_getter(spartan_id):                     # must pass the changing variable as the parameter
    # Check the database. read from a file, etc till you get the data

    try:
        text = str(spartans[spartan_id])
    except KeyError:
        text = "Error: id not found"
    return text

# http://127.0.0.1:5000/spartan/remove?id=spartan_id
@web_app.route('/spartan/remove', methods=["GET"])
def spartan_remover():                     # must pass the changing variable as the parameter
    spartan_id = request.args.get("id")
    try:
        del spartans[spartan_id]
        text = f"Spartan id  successfully removed."

        spartans_json = {}
        for key, value in spartans.items():
            spartans_json[key] = value.__dict__
        with open("spartan_data.json", "w") as jsonfile:  # jsonfile is the pointer to the file
            json.dump(spartans_json, jsonfile, indent=4)

    except KeyError:
        text = "Error: id not found"
    return text


@web_app.route('/spartan', methods=["GET"])
def list_getter():
    return f"You are asking to view a list of all Spartan Records:"

if __name__ == "__main__":
    web_app.run()
