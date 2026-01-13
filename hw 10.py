# tracker.py

def create_travel_record(city, comment, visit_date):
    """
    Creates and returns a travel record dictionary.
    visit_date should be in 'dd-mm-yyyy' format.
    """
    return {
        "city": city,
        "comment": comment,
        "visit_date": visit_date
    }
# main.py

import json
from datetime import datetime
from tracker import create_travel_record

# Create a list of travel records
records = [
    create_travel_record("Paris", "Visited the Eiffel Tower", "05-06-2022"),
    create_travel_record("Rome", "Explored the Colosseum", "14-09-2021"),
    create_travel_record("Tokyo", "Enjoyed cherry blossoms", "28-03-2023")
]

# Convert date format to "Month Day, Year"
for record in records:
    date_obj = datetime.strptime(record["visit_date"], "%d-%m-%Y")
    record["visit_date"] = date_obj.strftime("%B %d, %Y")

# Convert records list to JSON string
json_data = json.dumps(records, indent=4)
print("JSON Data:")
print(json_data)

print("\nParsed Records:")

# Parse JSON back to Python object
parsed_records = json.loads(json_data)

# Display each record on a separate line
for record in parsed_records:
    print(record)
