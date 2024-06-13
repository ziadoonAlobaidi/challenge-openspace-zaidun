from table import Table

class Openspace :

    def __init__(self, number_of_tables, seats_per_table):
        self.tables = []
        self.number_of_tables
        for x in range(number_of_tables):
            self.tables.append(Table(seats_per_table))
        