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

# I am gonna create table class in table.py

class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]


    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False         
    
    def assign_seat(name):
        for seat in self.seats:
            if seat.free:
                seat.set
