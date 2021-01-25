
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


    def getSen(self):
        return self._y_coordinate / self.getHypotenuse()


    def getCos(self):
        return self._x_coordinate / self.getHypotenuse()


    def getTan(self):
        return self._y_coordinate / self._x_coordinate


    def getCsc(self):
        return self.getHypotenuse() / self._y_coordinate


    def getSec(self):
        return self.getHypotenuse() / self._x_coordinate


    def getCot(self):
        return self._x_coordinate / self._y_coordinate


def main():
    #ask for the user the x and y coordinates
    x_coord = float(input('Enter the X coordinate: '))

    y_coord = float(input('Enter the Y coordinate: '))

    trig_function_calc = TrigFunctionCalc(x_coord, y_coord)

    print('Sen:', format(trig_function_calc.getSen(), '.2f'))
    print('Cos:', format(trig_function_calc.getCos(), '.2f'))
    print('Tan:', format(trig_function_calc.getTan(), '.2f'))
    print('Csc:', format(trig_function_calc.getCsc(), '.2f'))
    print('Sec:', format(trig_function_calc.getSec(), '.2f'))
    print('Cot:', format(trig_function_calc.getCot(), '.2f'))


if __name__=="__main__":
    main()
