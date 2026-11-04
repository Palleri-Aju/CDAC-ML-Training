
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Define dataset
X = np.array([1, 2])
y = np.array([2, 4])

# STEP 2: Initialize parameters
m = 0.0
learning_rate = 0.1
iterations = 6

# Store values for plotting
m_history = []
cost_history = []

# STEP 3: Apply Gradient Descent
for i in range(iterations):

    # Predict Y using current slope
    y_pred = m * X

    # Calculate Mean Squared Error
    cost = np.mean((y - y_pred) ** 2)

    # Calculate gradient of MSE with respect to m
    gradient = 2 * np.mean(X * (y_pred - y))

    # Store current values
    m_history.append(m)
    cost_history.append(cost)

    print(
        f"Iteration {i}: "
        f"m = {m:.4f}, "
        f"MSE = {cost:.4f}, "
        f"Gradient = {gradient:.4f}"
    )

    # STEP 4: Update slope
    m = m - learning_rate * gradient

print("\nSlope after 6 updates:", m)

# STEP 5: Plot the cost curve
m_values = np.linspace(0, 4, 100)
cost_values = 2.5 * (m_values - 2) ** 2

plt.figure(figsize=(8, 5))
plt.plot(m_values, cost_values, label="Cost Curve (MSE)")
plt.plot(m_history, cost_history, "ro-", label="Gradient Descent Steps")

plt.xlabel("Slope (m)")
plt.ylabel("Mean Squared Error")
plt.title("Gradient Descent - Finding the Best Slope")
plt.legend()
plt.grid(True)
plt.show()

# STEP 6: Plot the fitted regression line
plt.figure(figsize=(8, 5))
plt.scatter(X, y, label="Actual Data")
plt.plot(X, m * X, label=f"Learned Line: y = {m:.4f}x")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Regression Line After Gradient Descent")
plt.legend()
plt.grid(True)
plt.show()
