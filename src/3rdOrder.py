import numpy as np
from Regression import Regression, data_O3

order = 3
model = Regression(order)
x = np.array(data_O3['x'])
y = np.array(data_O3['y'])
x_cube = np.power(x,3)
x_square = np.power(x,2)
#printing the coefficents that give the best least square error
x_func = np.stack((x_cube, x_square, x, np.ones((len(x)), dtype = int)), axis = 1)
model.solve(x_func,y,order*2)

model.visualize(x, y, True)