def statement_generator(deco, statement):
    """Makes a fancy title"""
    print(deco * 5, statement, deco * 5)


def instructions():
    """Displays a set of instructions"""

    statement_generator("-", "Instructions")

    print("""
    1:
    2:
    3:
    """)


statement_generator("*", "Hello world")
