# Import NumPy 
import numpy as np

# Define your data points
x = np.array([1, 2.5, 3, 3.25, 6, 8, 9.4])
y = np.array([0, 5, 7, 6.5, 9.5, 23.5, 18.7])

# Define the linear model
def model(x, m):
   return m * x

# Define the error (loss) function
def error_function(m):
   numerator = 0
   n = len(x)
   for i in range(n):
      y_true = y[i]  # Actual y-value
      x_val = x[i]   # Corresponding x-value
      # Calculate the squared difference between predicted and actual y-values
      numerator += (y_true - model(x_val, m)) ** 2
   # Calculate the mean squared error (MSE)
   return numerator / n

# Define the derivative of the error function
def derivative(m):
   numerator = 0
   n = len(x)
   for i in range(n):
      y_true = y[i]  # Actual y-value
      x_val = x[i]   # Corresponding x-value
      # Calculate the term inside the derivative
      bracken_term = y_true - model(x_val, m)
      # Calculate the gradient of the error function
      numerator += -2 * x_val * bracken_term
   return numerator / n

# Define the update step for gradient descent
def update_step(m, learning_rate=0.01):
   # Calculate the derivative
   grad = derivative(m)
   # Update 'm' using gradient descent
   return m - (learning_rate * grad)

# Initial value for the slope 'm'
m = -6

# Number of training epochs
n_epochs = 5

# Iterate for n_epochs
for epoch in range(n_epochs):
   # Update and print 'm' for each epoch
   m = update_step(m)
   print(f'Epoch {epoch + 1}: m = {round(m, 2)} and loss = {round(error_function(m), 2)}')

# Print final results
print("Predictions in x value")
print("FINAL RESULTS")
print("Predictions in y values")

# Print the final values of 'm' and loss
print(f'm = {round(m, 2)} and loss = {round(error_function(m), 2)}')

# Print the regression line equation
print(f"The regression line is: y = {round(m, 2)}x")
