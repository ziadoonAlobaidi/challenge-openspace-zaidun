class Seat:
    # Initializing 2 attributes (free, occupant).
    def __init__(self, free=True, occupant=""):
        # Should be boolean.
        self.free = free
        # Should be string.
        self.occupant = occupant

    # set_occupant method allows to assign a seat if it's free, otherwise returns message.
    def set_occupant(self, name):
        """
        Function that allows to assign a seat if it's free, otherwise returns message.

        :param name: Name of a person that you want to assign a seat.
        :return: Returns to whom the seat was assigned or if the seat is free.
        """
        if self.free:
            self.occupant = name
            self.free = False
            return f"Seat assigned to {name}"
        else:
            return 'Seat is not free'

    # remove_occupant method removes someone from a seat and returns name of the person.
    def remove_occupant(self):
        """
        Function that allows to remove someone from a seat and returns name of the person.

        :param self:
        :return: Returns the name of the person that you want to remove or if seat is free.
        """
        if self.free is False:
            previous_occupant = self.occupant
            self.occupant = ""
            self.free = True
            return f"Removed occupant: {previous_occupant}"
        if self.free:
            return "Seat is already free"

    # __str__ shows status of an object that belongs to the class (Seat).
    def __str__(self):
        """
        Function that shows status of an object that belongs to the class (Seat).

        :param self:
        :return: Returns the status of a seat.
        """
        status = "free" if self.free else "occupied"
        return f"Seat is {status}. Occupant: {self.occupant}"

# Creating objects (with True and False) (to check both conditons)(for set_occupant):
a = Seat(True, '')
a2 = Seat(False, 'Johny')

# Creating objects (with True and False) (to check both conditons)(for remove_occupant):
b = Seat(True, '')
b2 = Seat(False, 'Johny')

# testing of set_occupant method.
print(a2.set_occupant('John'))
print(a.set_occupant('Boris'))

print('\n')

# testing of remove_occupant method.
print(b.remove_occupant())
print(b2.remove_occupant())

print('\n')

# testing of __str__ method.
print(a)
print(a2)