import json

def retrieve(spartans, spartan_id):
    try:
        text = str(spartans[spartan_id])
    except KeyError:
        text = "Error: id not found"
    return text

def remove(spartans, spartan_id):
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
