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
import random

#TODO check the logic, remove unnecessary variables or rename everything in the same style
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
                row_size = len(matrix_a[:,1])
                column_size = len(matrix_a[1,:])
                if row <= (row_size-1) and column <= (column_size-1):
                    A[row][column] = number
                    #self.view_matrix(A)
                    return matrix_a
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

        global matrix_old 
        matrix_old = self.change_car_parking_place(column_, row_, 1, matrix_)
        global matrix_new
        matrix_new = []

        x = - int((h_cell/2)+ y_front) # for h8 = 2
        y =   int((h_cell/2) + (y_rear/2)) #maybe not right = -1 
        
        #version 1.1
        for y in range(x, y): 
            row = row_ - y
            x = int(w_cell/2)
            while x >= -int(w_cell/2):
                column = column_ - (x)
                if column == column_ and row == row_:
                    matrix_new = self.change_car_parking_place(column, row, 1, matrix_old)
                    matrix_old = matrix_new
                    x -= 1
                else:
                    matrix_new = self.change_car_parking_place(column, row, 2, matrix_old)
                    matrix_old = matrix_new
                    x -= 1
        """
        #version 1.2
        for y in range(x, y): 
            row = row_ - y
            #x = int(w_cell/2)
            print("-w_cell/2:", w_cell/2)
            for x in range(int(-w_cell/2), int(w_cell/2)+1):
                column = column_ - (x)
                if column == column_ and row == row_:
                    matrix_new = self.change_car_parking_place(column, row, 1, matrix_old)
                    matrix_old = matrix_new
                    x -= 1
                else:
                    matrix_new = self.change_car_parking_place(column, row, 2, matrix_old)
                    matrix_old = matrix_new
                    x -= 1
        """

        self.view_matrix(matrix_new)
        return matrix_new

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
    
    def search_alg(self, row_x, column_y, column_size, waiting_time):
        print("search_alg!")

        #TODO need to make a time dependency
        if waiting_time > 240 and waiting_time < 600: #time in minute
            print("long parking time")
            print("Time", waiting_time)
            
            if(column_y == 0):
                    row_x -= 1
                    column_y = column_size
            row_x = row_x
            column_y -= 1

            return row_x, column_y

        elif waiting_time < 240 and waiting_time > 0:
            print("short parking time")   
            print("Time", waiting_time)

            if(column_y == 20):
                    row_x += 1
                    column_y = 0
            row_x = row_x
            column_y += 1

            return row_x, column_y
        else:
            print("oh oh something went wrong in def search alg")
            print("Bad range of waiting time")
            return row_x, column_size

    def check_point(self, matrix, h_cell, w_cell, y_front, y_rear, waiting_time):
        #This function search key parking point with "some" algorithm 
        #TODO Rewrite this method
        print("Search!")

        if waiting_time > 240 and waiting_time < 600: #time in minute
            print("long parking time")
            row_x = 20
            column_y = 20
        elif waiting_time < 240 and waiting_time > 0:
            print("short parking time")
            row_x = 0
            column_y = 0

        check_place = True
        find_place = False

        while check_place == True:  
            print("check while...")

            row_size = len(matrix[:,1])
            column_size = len(matrix[1,:]) 
            #hand input test
            #column_ = int(input("Enter column: "))
            #row_ = int(input("Enter row: "))

            print("search_alg")
            row_x = self.search_alg(row_x, column_y, column_size, waiting_time)[0]      #3d argument need add link
            column_y = self.search_alg(row_x, column_y, column_size, waiting_time)[1]

            row_ = row_x #not needed in the future
            column_ = column_y #not needed in the future

            matrix_old = self.change_car_parking_place(column_, row_, 1, matrix)
            matrix_new = []

            check_sector = True

            x = - int((h_cell/2)+ y_front) # for h8 = 2
            y =   int((h_cell/2) + (y_rear/2)) #maybe not right = -1 
            
            for y in range(x, y):
                row = row_ - y
                print("row:", row)
                print("row_size:", row_size -1)
                if row <= (row_size -1):
                    for x in range(int(-w_cell/2), int(w_cell/2)+1):
                        column = column_ - (x)
                        if column <= (column_size - 1) and column >= 0 and row <= (row_size - 1) and row >= 0: 
                            if matrix[row][column] == 2:
                                find_place = False
                                check_place = False
                                check_sector = False
                                #return matrix
                                matrix_new = matrix                           
                                break
                            elif column == column_ and row == row_ and check_sector == True:
                                matrix_new = self.change_car_parking_place(column, row, 1, matrix_old)
                                matrix_old = matrix_new
                                find_place = True
                            elif check_sector == True:
                                matrix_new = self.change_car_parking_place(column, row, 2, matrix_old)
                                matrix_old = matrix_new
                                find_place = True
                        else: 
                            print("Bad range column in 'def check_point'!")
                            #check_place = False
                            find_place = False
                            check_sector = False
                            break
                else: 
                    print("Bad range row in 'def check_point'!")
                    #check_place = False
                    find_place = False
                    break

                if find_place == True:
                    print("Place found!")
                    check_place = False
                elif find_place == False and check_place == False:
                    print("Place not found in while 1")
                    check_place = True
                    matrix_old = matrix
                else:
                    print("Place not found in while 2")
                    check_place = True   

        if(find_place == True):
            print("Found a place in def check_place")
            self.view_matrix(matrix_new)
            return matrix_new
        else:
            print("No place found in def check_place")
            matrix_new = matrix
            self.view_matrix(matrix_new)
            return matrix_new

    def add_car_parking_place(self, matrix_, h_car, w_car, front, rear, waiting_time):

        print("add_car_parking_place_0")
        find_cell = self.find_min_distance_cell(h_car, w_car)

        cell = self.matrix_filling(find_cell[0], find_cell[1])

        center_point = self.check_point(matrix_, cell[0], cell[1], front, rear, waiting_time)
        result = center_point
        #result = self.filling(center_point, matrix_, cell[0], cell[1], front, rear)
        return result

    def remove_car_parking_place(self, column_, row_):
        self.change_car_parking_place(column_, row_, 0)

    def menu(self):
        print("Hello in menu of parking task allokation")
        #TODO make a mathod
        front_wheel = 1
        rear_wheel = -2  
        time = 10       #not use

        matrix = []
        new_matrix = []

        continue_work = True
        while continue_work == True:
            print("Input 1 to add car on parkin place")
            print("Input 2 to delete car from parkin place")
            print("Input 3 to matrix")
            print("Input 4 to end this program")
            menu_button = int(input())

            if menu_button == int(1):
                time = int(input())
                print("Add car menu")
                #output = Parking(1, 20, 20, 50, 4, 2, front_wheel, rear_wheel, time)
                matrix = np.array(matrix)
                new_matrix = np.array(new_matrix)

                if matrix.size == 0:
                    matrix = self.parking_zero_matrix()
                elif new_matrix.size == 0 and matrix.size != 0:
                    new_matrix = matrix
                else:
                    matrix = new_matrix 

                new_matrix = self.add_car_parking_place(matrix, 3, 2, front_wheel, rear_wheel, time)
                
            elif menu_button == int(2):
                print("Delete car menu")
                new_matrix = np.array(new_matrix)
                if np.sum(new_matrix) == 0 or new_matrix.size == 0:
                    print("Matrix is empty!")
                else:
                    print("Matrix is't empty")
                    print("Enter place with car")
            elif menu_button == int(3): 
                print("Matrix: ", matrix)
                print("New_matrix: ", new_matrix)
                
            elif menu_button == int(4): 
                print("Thanks for using this program")
                print("Program is exit")
                continue_work = False
    
    """
    #TODO car dimensions is been in def min size or soth like this method, check and rename
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

front_wheel = 1
rear_wheel = -2  
time = 10

parking_ta = Parking(1, 20, 20, 50, 4, 2, front_wheel, rear_wheel, time)

parking_ta.menu()