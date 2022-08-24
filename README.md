# Assignment 4

## Regression with RANSAC for robust curve fitting

For a given polynomial, \\
$$y_{i}=\beta_{0}+\beta_{1} x_{i}+\beta_{2} x_{i}^{2}+\cdots+\beta_{m} x_{i}^{m}+\varepsilon_{i}(i=1,2, \ldots, n)$$

we can express it in a form of matrix $\mathbf{X}$, a response vector or $\vec{y}$, a parameter vector $\vec{\beta}$, and a vector $\vec{\varepsilon}$ of random errors. The model can be represented as system of linear equations, i.e.



$$\left[\begin{array}{c}y_{1} \\ y_{2} \\ y_{3} \\ \vdots \\ y_{n}\end{array}\right]=\left[\begin{array}{ccccc}1 & x_{1} & x_{1}^{2} & \ldots & x_{1}^{m} \\ 1 & x_{2} & x_{2}^{2} & \ldots & x_{2}^{m} \\ 1 & x_{3} & x_{3}^{2} & \ldots & x_{3}^{m} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n} & x_{n}^{2} & \ldots & x_{n}^{m}\end{array}\right]\left[\begin{array}{c}\beta_{0} \\ \beta_{1} \\ \beta_{2} \\ \vdots \\ \beta_{m}\end{array}\right]+\left[\begin{array}{c}\varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \vdots \\ \varepsilon_{n}\end{array}\right]$$

$$or$$

$$\vec{y}=\mathbf{X} \vec{\beta}+\vec{\varepsilon}$$

For this system, we can calculate $\vec{\beta}$ by using the following formula,
$$\widehat{\vec{\beta}}=\left(\mathbf{X}^{\top} \mathbf{X}\right)^{-1} \mathbf{X}^{\top} \vec{y}$$

Using **RANSAC**, we want to avoid outliers in our curve fitting, and thus we will calculate multiple $\vec{\beta_i}$ s using a set of datapoints. After calculating several $\vec{\beta_i}$ we will find the best value of ${\beta}$ using _least squares_.

## What is Linear Regression?

Linear Regression is essentially a type of predictive analysis. It is a linear approach to model a relationship between a scalar response and one or multiple explanatory variables which can be dependent or independent. The modelling is called simple linear regression there is only one reponse variable and is called multiple linear regression when there are multiple explanatory variables.

We use linear predictor functions whose unknown parameters are estimated using the data. Here we used linear regression to predict the model parameters Beta as shown in the equations above, by using the given expression $$\widehat{\vec{\beta}}=\left(\mathbf{X}^{\top} \mathbf{X}\right)^{-1} \mathbf{X}^{\top} \vec{y}$$

In any dataset y, we assume the relationship between the dependent variable y and the p-vector of regressors in x is linear. This relation is modeled through an sq_erroror variable, an "noise" adding variable. Thus this model takes the form mentioned at the beginning and hence the equation mentioned here to solve the same to obtain the model. The Least Square method reduces the distance between the best fit curve and the data points.

Every time we take a a random sample, we are getting the linear regression model for that sample and sending the resultant model for processing in the solve function.

## Why RANSAC?

Now, as mentinoed in the definition of linear regression, the curve that we obtain to get a best fit for the given dataset is a straight line. This however, might not always be the case to obtain a line to fit the data best. So first of all, we use a polynomial regressor. Also, one of the most important things in curve fitting is to identify if a given datapoint is actually a part of the dataset that represents a correct model or not. That is, whether the given datapoint is an inlier in the dataset or an outlier which does not fit the general pattern of the dataset. Now, to eliminate these outliers, we deploy RANSAC so that we can obtain the best possible set of inliers that generate the model to fit the maximum dataset overall within a certain threshold_lim. These outliers are not normally a problem it is just an extreme observation drawn from a tail of a normal distribution but if the datapoint is the result of a non-normal measurement sq_erroror, or some other violation of standard orinary least squares assumptions, the validity of the results of the regressor become questionable and the regressor is non-robust.

## How does RANSAC help curve fitting?

This is how the algorithm of RANSAC works:

We iterate for a large number of Total_iterations: 
  * randomly select any n samples from the dataset and find the best fit model for these points using linear least square model.
  * find the number of points that are inside (if they lie within a certain threshold_lim from the model) from this current model. 
  * if this number is more than the best number of inlier points so far, set the best points count to this number and the best model obtained so far as the current model. (this is because this model is the model that satisfies most points so far in the Total_iterations.)

return the best model obtained after all the Total_iterations. This ensures that the from the Iteration_count models that will fit any n random sample points in the data, the best model/ curve has been chosen to fit the most points.

