class Seat:

    # Initializing 2 attributes (free, occupant)
    def __init__(self, free=True, occupant=""):
        # Should be boolean
        self.free = free
        # Should be string
        self.occupant = occupant

    # set_occupant method allows to assign a seat if it's free, otherwise returns message not free.
    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
            return f"Seat assigned to {name}"
        else:
            return 'Seat is not free'

    # remove_occupant method removes someone from a seat and returns name of the person
    def remove_occupant(self):

        if self.free is False:
            previous_occupant = self.occupant
            self.occupant = ""
            self.free = True
            return f"Removed occupant: {previous_occupant}"
        if self.free:
            return "Seat is already free"


# Examples:
a = Seat(True, '')
a2 = Seat(False, 'Johny')
print(a2.remove_occupant())
print(a.remove_occupant())
print(a2.set_occupant('John'))
print(a.set_occupant('John'))