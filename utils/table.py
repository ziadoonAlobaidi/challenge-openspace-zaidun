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
