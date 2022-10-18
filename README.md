# Task allocation
## _Introduction_

[![V|Lebedeva](/screenshots/icon_ras.png)](https://spcras.ru/units/employee.php?ID=468302)

## Features
* # Input topic:
    * ##### _Parking class have object_
```sh
    • i - number of parking sections UNTIL i=1

    • m_i, n_i - number of rows and columns of nodes of the i-th parking section. LET IT BE 10 ON 20

    • s - step between nodes, m (constant for all sections) LET IT BE 50 cm

    • h, w - the height and width of the vehicle to be placed FIRST FOR ONE CAR 4 TO 2 AND SO IN GENERAL DIFFERENT VALUES CAN BE

    • y_front, y_rear - the coordinate of the center point between the front and rear   wheels CAN BE CALCULATED HERE

    • t - the time of placing the PBX in the parking lot (we will assume that the more time the PBX should be located in the parking lot,
    the farther the parking space in the parking section should be located from the highway) THIS CAN BE A DIFFERENT VALUE
```

* Input 1 to add car on parkin place
* Input 2 to remove car from parkin place
* Input 3 to view parking places
* Input 4 to end this program
* # Output topic:
    * ##### Allocation parking place
```sh
    • column and row
```

## Work example

* # Menu
![menu_list](/screenshots/menu_list.jpg)

* # Add car in list
    * Add car on short parking time
    ![parking1_6](/screenshots/parking_short.jpg)
    * Add car on long parking time
    ![parking6_12](/screenshots/parking_long.jpg)
    * Add car on 12h to 18h

* # Delete car from list
![pick_up_car](/screenshots/pick_up_1.jpg)