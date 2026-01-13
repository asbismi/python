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
