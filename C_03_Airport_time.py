import airportsdata
from datetime import datetime
from zoneinfo import ZoneInfo


def get_airport_time(airport):
    """Gets the current time of an airport"""

    # Gets the airport data (time)
    airports = airportsdata.load()
    nzaa = airports[airport]

    # Gets the date and time of the current airport
    date = datetime.now(tz=ZoneInfo(nzaa['tz']))

    # Turns date into a readable form and prints it
    airport_t = date.strftime("%Y-%m-%d %H:%M:%S %Z")
    return airport_t


# Main routine goes here
airport_icao = input("ICAO: ")
airport_time = get_airport_time(airport_icao)
print(airport_time)
