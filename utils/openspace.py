from table import Table
from table import Seat
import numpy as np
import openpyxl

class Openspace :

    def __init__(self, number_of_tables, seats_per_table):
        self.number_of_tables = number_of_tables
        self.tables = [Table(seats_per_table) for i in range(number_of_tables)]
        

    def organize(self,names) :
        """
        Randomly assign people to Seat objects in the different Table objects.
        """
        shuffleNames = np.random.shuffle(names)
        for name in shuffleNames :
            msg = Table.assign_seat(name)
        return msg
            
    
    def display(self): 
        """
        display the different tables and their occupants in a nice and readable way store(filename)
          store the repartition(table 0 has mehmet + min + ...) in an excel file
        """
        n_tables = 0
        for table in self.tables :
            n_tables +=1
            print("Table number "+ n_tables + " has : ")
            for seat in table.seats :
                print(seat.occupent)
                occupant = seat.occupent
                self.store(occupant)
        
    def store(self, newRecord):
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

