def statement_generator(deco, statement):
    """Makes a fancy title"""

    # Prints the fancy title
    print(deco * 5, statement, deco * 5)


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


def instructions():
    """Displays a set of instructions"""

    # Makes a fancy title
    statement_generator("-", "Instructions")

    # Prints the instructions
    print("""
    1:
    2:
    3:
    """)


# Main routine goes here

# Title
statement_generator("*", "Hello world")

# Asks if they want instructions
instructions_yes_no = yes_no("Do you require instructions? ")

# If they said yes the display them
if instructions_yes_no == "YES":
    instructions()

# Says "Good luck"
print("Good luck!")
