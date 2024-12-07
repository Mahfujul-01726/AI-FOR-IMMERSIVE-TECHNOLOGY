# -*- coding: utf-8 -*-
"""linear_regression_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yItYvzA3HinQoZI89bm7q1XIca45bBps
"""

import autograd.numpy as np
from autograd import grad
import matplotlib.pyplot as plt
import glob
from PIL import Image
import re

# Step 1: Define the forward pass (simple linear regression)
def forward(X, W, b):
    return np.dot(X, W) + b

# Step 2: Define the loss function (Mean Squared Error)
def Loss_Function(W, b, X, y):
    y_pred = forward(X, W, b)
    return np.mean((y - y_pred) ** 2)

# Input data
# Step 3: Generate input data
np.random.seed(0)
num_samples = 100
X = np.random.uniform(0, 1.5, (num_samples, 1))  # Input features
y = np.tan(X) + np.random.normal(0, 0.1, (num_samples, 1))  # Target (with noise)

# Plot input data
plt.figure(figsize=(10, 6))
plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.title("Input Data")
plt.show()

# Step 4: Initialize parameters (weights and bias) for linear regression
W = np.random.randn(1, 1)  # Weight
b = np.random.randn(1)  # Bias

# Step 5: Set hyperparameters
num_epochs = 1000
learning_rate = 0.01

# Step 6: Use autograd to compute the gradients of the loss function w.r.t. W and b
gradient_W = grad(Loss_Function, 0)  # Gradient w.r.t. W
gradient_b = grad(Loss_Function, 1)  # Gradient w.r.t. b

losses = []

# Step 7: Training loop using batch gradient descent
for epoch in range(1, num_epochs+1):
    dW = gradient_W(W, b, X, y)
    db = gradient_b(W, b, X, y)

    # Update weights and bias
    W -= learning_rate * dW
    b -= learning_rate * db

    # Calculate and store the loss
    loss = Loss_Function(W, b, X, y)
    losses.append(loss)

    # Print progress
    if epoch % 10 == 0:
        print(f'Epoch {epoch}: loss = {loss:.4f}')

        # Predict
        y_pred = forward(X, W, b)

        # Save the plot in ./prediction folder
        plt.figure(figsize=(10, 6))
        plt.scatter(X, y, label='True')
        plt.scatter(X, y_pred, label='Predicted', color='r')
        plt.xlabel('X')
        plt.ylabel('y')
        plt.legend()
        plt.title(f'Epoch {epoch}: loss = {loss:.4f}')
        plt.savefig(f'./prediction/{epoch}.png')
        plt.close()

# Step 8: Plot the loss curve
plt.figure(figsize=(10, 6))
plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title("Loss Curve")
plt.show()

# Step 9: Final prediction after training
y_pred = forward(X, W, b)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='True')
plt.scatter(X, y_pred, label='Predicted', color='r')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title("Final Prediction")
plt.show()

# Step 10: Save prediction plots as GIF
fp_in = "./prediction/*.png"
fp_out = "linear_regression.gif"

natsort = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)]

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in), key=natsort)]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)

print("GIF saved as linear_regression.gif")
