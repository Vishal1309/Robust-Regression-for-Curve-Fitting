from Regression import Regression, data_O2
import numpy as np
order = 2
model = Regression(order)
x = np.array(data_O2['x'])
x_square = np.power(x,2)
#printing the coefficents that give the best least square error
x = np.stack((x_square, x, np.ones((len(x)), dtype = int)), axis = 1)
model.solve(x,np.array(data_O2['y']),order*2)

model.visualize(data_O2['x'], data_O2['y'], True)