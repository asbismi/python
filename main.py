# main.py

import json
from datetime import datetime
from tracker import create_travel_record
records = [
    create_travel_record("Paris", "Visited the Eiffel Tower", "05-06-2022"),
    create_travel_record("Rome", "Explored the Colosseum", "14-09-2021"),
    create_travel_record("Tokyo", "Enjoyed cherry blossoms", "28-03-2023")
]
for record in records:
    date_obj = datetime.strptime(record["visit_date"], "%d-%m-%Y")
    record["visit_date"] = date_obj.strftime("%B %d, %Y")
json_data = json.dumps(records, indent=4)
print("JSON Data:")
print(json_data)

print("\nParsed Records:")
parsed_records = json.loads(json_data)
for record in parsed_records:
    print(record)
