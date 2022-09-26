"""

This program module has the following test data set
Input:
• i - number of parking sections UNTIL i=1
• m_i, n_i - number of rows and columns of nodes of the i-th parking section. LET IT BE 10 ON 20
• s - step between nodes, m (constant for all sections) LET IT BE 50 cm
• h, w - the height and width of the vehicle to be placed FIRST FOR ONE CAR 4 TO 2 AND SO IN GENERAL DIFFERENT VALUES CAN BE
• y_front, y_rear - the coordinate of the center point between the front and rear wheels CAN BE CALCULATED HERE
• t - the time of placing the PBX in the parking lot (we will assume that the more time the PBX should be located in the parking lot,
 the farther the parking space in the parking section should be located from the highway) THIS CAN BE A DIFFERENT VALUE

"""

from distutils.log import error
import numpy as np
from time import sleep

print("Parkin module start")

class Parking:
    def __init__(self, i, m_i, n_i, s, h, w, y_front, y_rear, t):
        self.number_of_parking = i          #       number of parking sections
        self.row_i = m_i                    #       number of rows and columns of nodes
        self.columns_i = n_i                # of the i-th parking section
        self.step_n = s                     #       step between nodes, m (constant for all sections)
        self.hight = h                      #       height and 
        self.wight = w                      # width of the PBX(АТС) to be placed
        self.front_wheels = y_front         #       coordinate of the center point 
        self.rear_wheels = y_rear           # between the front and rear wheels
        self.patking_time = t               #       'the time the PBX is located in the parking lot 
                                            # (we will assume that the more time the PBX should be 
                                            # located in the parking lot, the farther the parking 
                                            # space in the parking section should be located from the highway)'
    
    def parking_zero_matrix(self):
        row = []
        column = []
        for x in range(self.columns_i):
            column.append(0)
        for x in range(self.row_i):
            row.append(column)
        A = row
        A = np.array(A)

        return A

    def view_matrix(self, matrix):
        for line in matrix:
            print(*line)

    def change_car_parking_place(self, column, row, number, matrix):
        def matrix_input_check(matrix_a):
            if (number == 0 or number == 1 or number == 2):
                row_size = len(A[:,1])
                column_size = len(A[1,:])
                if row <= (row_size-1) and column <= (column_size-1):
                    A[row][column] = number
                    #self.view_matrix(A)
                    return A
                else:
                    error("Bad value 'column' or 'row' in funtion add_car_parking_place")
                    return 1
            else:
                error("Bad value 'number 'in function add_car_parking_place")
                return 1

        matrix = np.array(matrix)
        if matrix.size == 0:
            A = self.parking_zero_matrix()
            matrix_input_check(A)
            return A
        else:
            A = matrix
            matrix_input_check(A)
            return A

    def filling(self, center_point, matrix_, h_cell, w_cell, y_front, y_rear):
        print("filinig")
        column_ = center_point[0]
        row_ = center_point[1]

        global test_old 
        test_old = self.change_car_parking_place(column_, row_, 1, matrix_)
        global test_new
        test_new = []

        x = - int((h_cell/2)+ y_front) # for h8 = 2
        y =   int((h_cell/2) + (y_rear/2)) #maybe not right = -1 
        for y in range(x, y): 
            row = row_ - y
            x = int(w_cell/2)
            while x >= -int(w_cell/2):
                column = column_ - (x)
                if column == column_ and row == row_:
                    test_new = self.change_car_parking_place(column, row, 1, test_old)
                    test_old = test_new
                    x -= 1
                else:
                    test_new = self.change_car_parking_place(column, row, 2, test_old)
                    test_old = test_new
                    x -= 1
        self.view_matrix(test_new)

    def cell_cm_in_metr(self):
        cm_step = self.step_n 
        meter_step = cm_step / 100
        return meter_step

    def find_min_distance_cell(self, h_car, w_car):
        cell = self.cell_cm_in_metr()
        h_cell = h_car / cell 
        w_cell = w_car / cell 
        print("cell", cell)
        print("h ", h_cell)
        print("w ", w_cell)
        return h_cell, w_cell

    def matrix_filling(self, h_cell, w_cell):
        print("matrix fillin")
        parity_variable = None
        if h_cell %2 == 0 and w_cell %2 == 0:
            print("even value")
            parity_variable = True
        else:
            print("odd value")
            parity_variable = False
        if parity_variable == True:
            print("True")
            return h_cell, w_cell
        else:
            print("False")
    
    def search_point(self):
        #This function search key parking point with "some" algorithm 
        print("search!")
       
    def add_car_parking_place(self, column_, row_, matrix_, h_car, w_car, front, rear):
        print("add_car")
        center_point = [column_, row_]

        find_cell = self.find_min_distance_cell(h_car, w_car)
        
        cell = self.matrix_filling(find_cell[0], find_cell[1])

        result = self.filling(center_point, matrix_, cell[0], cell[1], front, rear)

        return result

    def remove_car_parking_place(self, column_, row_):
        self.change_car_parking_place(column_, row_, 0)
"""
    def car_dimensions(self, hight, wight, front_wheel, rear_wheel):
        test = "car_dimensions"
        print(test)

    def horizontal_placement(self, matrix_A):
        test = "horizontal_placement"
        print(test)

    def vertical_placement(self, matrix_A):
        test = "vertical_placement"
        print(test)
"""
front_wheel = 2
rear_wheel = -2  
time = 10       #not use

output = Parking(1, 20, 30, 50, 4, 2, front_wheel, rear_wheel, time)

matrix = []
output.add_car_parking_place(4,4, matrix, 3, 2, front_wheel, rear_wheel)