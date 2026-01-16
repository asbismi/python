# main.py

import json
from datetime import datetime
from tripdata import get_trips

# Get list of trip dictionaries
trips = get_trips()

# Process each trip
for trip in trips:
    # Convert date string to date object
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y").date()
    
    # Format date as "Month Day, Year"
    trip["date"] = date_obj.strftime("%B %d, %Y")

# Convert list of trips to JSON string
json_output = json.dumps(trips, indent=4)

# Print JSON string
print(json_output)
