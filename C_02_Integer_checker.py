def integer_checker(question, low):
    """A simple integer checker that has a minimum value and accepts xxx"""

    # Sets up an error message
    error = f"Please enter a whole number greater than or equal to {low}."

    while True:

        # Asks the question
        answer = input(question)

        # Allows xxx as an answer
        if answer == "xxx":
            return answer

        # Checks that it can be an integer
        try:
            answer = int(answer)

            # If the number is less than the minimum, print an error
            if answer < low:
                print(error)

            # If all is good, return the answer
            else:
                return answer

        # Prints an error if the answer isn't an integer
        except ValueError:
            print(error)


# Main routine goes here

# For testing
number_refined = integer_checker("Number: ", 1)
print(number_refined)

