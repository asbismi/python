

import json
from datetime import datetime
from tripdata import get_trips

trips = get_trips()

for trip in trips:

    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y").date()
    
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_output = json.dumps(trips, indent=4)

print(json_output)
