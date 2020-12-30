import sys


class Citizen:
    ''' Blueprint for a Python Citizen '''
    def __init__(self, first_name, last_name):
        self.first_name = str(sys.argv[1])
        self.last_name = str(sys.argv[2])

    def full_name(first_name, last_name):
        return(first_name + " " + last_name)

    greeting = str("For the glory of Python!")


print(Citizen.full_name())
