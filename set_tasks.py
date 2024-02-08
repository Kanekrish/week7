def observed():
    """
    This function creates a set named 'observations' and populates it with the following items:
    "Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"
    Finally, the function returns the set 'observations'.
    """
    observations = set()
    observations.add("Car")
    observations.add("Sky Scraper")
    observations.add("Sky Scraper")
    observations.add("Bike")
    observations.add("House")
    observations.add("House")
    return observations

def run_task1():
    """
    This function calls the 'observed' function and displays the set returned by the call.
    """
    observations = observed()
    print(observations)

run_task1()