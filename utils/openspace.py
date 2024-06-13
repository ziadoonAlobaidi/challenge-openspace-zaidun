from table import Table
from table import Seat
import numpy as np
import openpyxl

class Openspace :

    def __init__(self, number_of_tables, seats_per_table):
        self.tables = []
        
        self.number_of_tables = number_of_tables


        for x in range(number_of_tables):
            self.tables.append(Table(seats_per_table))

    def organize(names) :
        """
        Randomly assign people to Seat objects in the different Table objects.
        """
        shuffleNames = np.random.shuffle(names)
        for name in shuffleNames :
            Table.assign_seat(name)
            
    
    def display(): 
        """
        display the different tables and their occupants in a nice and readable way store(filename) store the repartition in an excel file
        """
        n_tables = 0
        for table in self.tables :
            n_tables +=1
            print("Table number "+ n_tables + " has : ")
            for seat in table.seats :
                print(seat.occupent)
                occupant = seat.occupent
                self.store(occupant)
        
    def store(newRecord):
        """
        store(filename) store the repartition in an excel file
        """

        # Create a new workbook
        workbook = openpyxl.Workbook()

        # Select the active sheet (default sheet created by openpyxl)
        sheet = workbook.active

        # Add a name to cell A1
        sheet['A1'] = newRecord

        # Save the workbook
        workbook.save('names.xlsx')

        print("Name saved successfully.")

