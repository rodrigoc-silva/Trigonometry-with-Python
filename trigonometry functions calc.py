
# This program calculates the six trigonetric functions,
# asking to the user the coordinates on the graph

import math

class TrigFunctionCalc:

    #initializer
    def __init__(self, x_coordinate, y_coordinate):
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate

        
    #getters
    def getXCoordinate(self):
        return self._x_coordinate

    
    def getYCoordinate(self):
        return self._y_coordinate
    

    #setters
    def setXCoordinate(self, x_coordinate):
        self._x_coordinate = x_coordinate


    def setXCoordinate(self, x_coordinate):
        self._x_coordinate = x_coordinate


    #class methods
    def getHypotenuse(self):
        return math.sqrt(pow(self._x_coordinate, 2)+pow(self._y_coordinate, 2))


def main():

    x_coord = float(input('Enter the X coordinate: '))

    y_coord = float(input('Enter the Y coordinate: '))

    coord1 = TrigFunctionCalc(x_coord, y_coord)

    print(coord1.getHypotenuse())


if __name__=="__main__":
    main()
