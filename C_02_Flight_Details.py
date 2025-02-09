import time


def statement_generator(deco, statement):
    """Makes a fancy title"""

    # Prints the fancy title
    print(deco * 10, statement, deco * 10)


def yes_no(question):
    """Asks a yes or no question the returns the answer"""

    # Repeats until an acceptable answer has been inputted.
    while True:

        # Valid answers
        valid_yes = ("YES", "Y", "1", "NEGATIVE", "+")
        valid_no = ("NO", "N", "0", "POSITIVE", "-")

        # Asks the question
        want_instructions = input(question).upper()

        # Checks if they said yes of no and returns the response
        if want_instructions in valid_yes:

            return valid_yes[0]

        elif want_instructions in valid_no:

            return valid_no[0]

        # Outputs an error if and unacceptable answer has been entered. Then loops until an acceptable answer has
        else:
            print("Error: Unacceptable answer, unable to comply.")


def flight_details(daylight_time):

    # Collects and stores flight details
    departure = input("Departure ICAO: ")
    arrival = input("Arrival ICAO: ")
    airline_icao = input("Airline ICAO: ")
    flight_number = input("Flight number: ")
    date_utc = input("Date (UTC): ")
    date = input("Date: ")
    aircraft_icao = input("Aircraft ICAO: ")
    aircraft = input("Aircraft: ")
    departure_time_utc = int(input("Departure time UTC (military time): "))
    arrival_time_utc = int(input("Arrival time UTC (military time): "))
    air_time = input("Air time: ")
    block_time = input("Block time: ")

    # Checks if it's dt or st and makes the appropriate change.
    if daylight_time == "YES":
        add_dt = 1300       # CHANGE THESE VALUES TO YOUR LOCAL TIME DIFFERENCE

    else:
        add_dt = 1200       # CHANGE THESE VALUES TO YOUR LOCAL TIME DIFFERENCE

    # Local departure time calculation
    departure_time = departure_time_utc + add_dt

    # Makes sure it stays within a day
    if departure_time > 2400:
        departure_time -= 2400

    # Local arrival time calculation
    arrival_time = arrival_time_utc + add_dt

    # Makes sure it stays within a day
    if arrival_time > 2400:
        arrival_time -= 2400

    # Make the data look nice and out put it.

    # Statement generator
    statement_generator("-", "Details")
    print(f"""
    Departure:      {departure}             Departure Time (UTC):   {departure_time_utc}    
                                            Departure Time:         {departure_time}
                                            
    Arrival:        {arrival}               Arrival Time (UTC):     {arrival_time_utc}
                                            Arrival Time:           {arrival_time_utc}
                                            
    Airline ICAO:   {airline_icao}          Flight Number:          {flight_number}

    Aircraft ICAO:  {aircraft_icao}         Aircraft:               {aircraft}
    
    Date (UTC):     {date_utc}              Date:                   {date}
    
    Block time:     {block_time}            Air time                {air_time}
    """)


# Main routine goes here
dt = yes_no("Is it daylight savings time? ")
flight_details(dt)

