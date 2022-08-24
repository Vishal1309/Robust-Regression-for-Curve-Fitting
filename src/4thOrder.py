import numpy as np
from Regression import Regression, data_O4
order = 4
model = Regression(order)
x = np.array(data_O4['x'])
y = np.array(data_O4['y'])
x_four = np.power(x,4)
x_cube = np.power(x,3)
x_square = np.power(x,2)
#printing the coefficents that give the best least square error
x_func = np.stack((x_four, x_cube, x_square, x, np.ones((len(x)), dtype = int)), axis = 1)
model.solve(x_func,y,order)

plot_4 = model.visualize(x, y, True)