import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

data_O2 = pd.read_csv("2nd_order.csv")
data_O3 = pd.read_csv("3rd_order.csv")
data_O4 = pd.read_csv("4th_order.csv")

# Calculating Beta to find the best fit in the given sample of data points.
class get_model:
    def fit(self, X, Y): #B (beta) = (inv(X'X)).(X'Y)
        X_T = X.transpose()
        Beta = (np.linalg.inv(X_T.dot(X))).dot(X_T.dot(Y))  
        return Beta

class Regression:
    def __init__(self,order,bias=True):
        """
        Initialize regressor
        :param order: order of the polynomial
        :param bias: boolean, True for our case
        """

        self.order = order
        self.bias = bias

        self.beta = np.zeros(order + bias)

    
    def solve(self,x,y,n):
        '''
        # For 1.5 marks
        Function to solve regression using RANSAC
        :param x: input
        :param y: output
        :param n: number of dataset per iteration
        :param iterations: number of iterations to find best beta 
        '''
        ## TODO
        
        threshold_lim = np.std(y)/5 # setting the threshold as 1/5th of the std deviation of y values after trying different percentage of the standard deviation and finding the best fit.
        max_inliers_overall = 0
        BestModel = None

        itr = 0
        sample_size = n

        Data_Overall = np.column_stack((x,y)) 
        DataSize = len(Data_Overall)
        iterations=10000

        # iterate for till the max iterations count
        for itr in range(iterations):

            # shuffle the entire data and take the first n entires of that data into the current sample
            np.random.shuffle(Data_Overall)
            curr_sample = Data_Overall[:sample_size, :]
            curr_model = get_model()
            try:
                estimated_model = curr_model.fit(curr_sample[:,:-1], curr_sample[:, -1:]) # fit the model on the current sample of n datapoints
                # count the number of datapoints lying within the threshold_lim
                y_hat = x.dot(estimated_model)
                sq_error = np.abs(np.square(y - y_hat.T))
                num_inliers = np.count_nonzero(sq_error < threshold_lim)

                # if the current number of inliers is more than the max inliers so far, then set the max inliers so far = current inliers count and set the best model to the current model
                if num_inliers > max_inliers_overall:
                    BestModel = estimated_model
                    max_inliers_overall = num_inliers
            except:
                pass

        ####
        # this is the best model obtained so far
        self.beta = BestModel
        return BestModel

    def get_func(self, coeff, x_value, y_value, order):
        for i in range(order+1):
          y_value += coeff[i]*(x_value**(order-i))
        return y_value

    def visualize(self,x,y,show=False):
        '''
        # For 0.5 marks
        function to visualize datapoints and optimal solution.
        '''
        # TODO
        coeff = self.beta
        order = self.order
        plt.figure(figsize =(10, 10))
        plt.scatter(x, y)
        x_func = np.linspace(x.min(),x.max(),100)
        y_func = np.zeros(len(x_func))
        y_func = self.get_func(coeff, x_func, y_func, self.order)
        plt.plot(x_func, y_func)

        ####
        if show:
            plt.show()
        return plt
