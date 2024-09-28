# Refer the Lesson Plan for the concepts to be discussed in the class before
# Explain the necessities needed to draw a graph / plot

import matplotlib.pyplot as plt
"""
# Show the easiest graph (y = x)
x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x, y)
plt.show()

# Add the formatting one by one
plt.plot(x, y, 'ro') # Replace the 'ro' by g^, r--, b--, b- and explain differnce
plt.show()

plt.plot(x, y, 'ro')  # red circles
plt.show()
plt.plot(x, y, 'g^')  # green triangles
plt.show()
plt.plot(x, y, 'r--')  # red dashed line
plt.show()
plt.plot(x, y, 'b--')  # blue dashed line
plt.show()
plt.plot(x, y, 'b-')   # blue solid line
plt.show()

# Show how to limit the numbers on each axis
plt.plot(x, y)
plt.axis([0, 10, 0, 200])
plt.show()

# Add the labels, title, linewidth and legend. Explain the use of each one of them

plt.plot(x, y, 'r--', label = " Y = X", linewidth = 4)
plt.axis([0, 10, 0, 50])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Graph")
plt.legend()
plt.show()

# Plot multiple graphs on a single plot
plt.plot([1,2,3,4,5], [1,4,9,16,25], 'r--', label="Y = X**2", linewidth = 5)
plt.plot([1,2,3,4,5], [1,8,27,64, 125], 'g--', label="Y = X**3", linewidth = 3)
plt.axis([0, 10, 0, 200])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Graph")
plt.legend()
plt.show()

# Notice that the quadratic and cubic graphs do not have a curve
# This is because the plot joins the data points together
# To show a curve you need to have the points close together

import numpy as np

x = np.arange(0, 10, 0.2)
print(x)

y1 = x**2
y2 = x**3

plt.plot(x, x**2, 'g--', x, x**3, 'b--')
plt.show()
"""
# Task - Ask the user for input m and c and plot the line y = mx + c using matplotlib 

import matplotlib.pyplot as plt

# Ask the user for input values of m and c
m = float(input("Enter the value of slope (m): "))
c = float(input("Enter the value of y-intercept (c): "))

# Generate x values
x = range(-10, 11)  # You can adjust the range as needed

# Calculate y values using the equation y = mx + c
y = []
for i in x:
    temp = m*i + c
    y.append(temp)
#y = [m * xi + c for xi in x]

# Plotting the line y = mx + c
plt.figure(figsize=(8, 6))  # Set the size of the figure
plt.plot(x, y, label=f'y = {m}x + {c}')  # Plot the line
plt.title('Plot of y = mx + c')  # Set the title
plt.xlabel('x-axis')  # Label for x-axis
plt.ylabel('y-axis')  # Label for y-axis
plt.grid(True)  # Show grid
plt.legend()  # Show legend
plt.axhline(0, color='black',linewidth=0.5)  # Add x-axis line
plt.axvline(0, color='black',linewidth=0.5)  # Add y-axis line
plt.show()  # Display the plot

# Explain what are the cases of using a  bar graph

# x cordinate = position of bar
# y cordiante = length of bar

plt.bar([1,3,5,7], [2,6,4,9], color = 'b')
plt.show()

# Showing multiple bars in a single plot
plt.bar([1,3,5,7], [2,6,4,9], color = 'b')
plt.bar([2,4,6,8], [3,5,7,9], color = "g")
plt.show()

# Showing the categorical data using bar plot
plt.bar(["Male Literacy", "Female Literacy"], [90, 95])
plt.show()

# Task - Plot the graph of count of passengers in different Pclass on a bar plot

import pandas as pd
import matplotlib.pyplot as plt

# loading the data file
data = pd.read_csv("L5/titanic.csv")

# Counting passengers in different Pclass
pclass_counts = data['Pclass'].value_counts()

# Plotting the counts of passengers in different Pclass
plt.bar(pclass_counts.index, pclass_counts.values)
plt.xlabel('Passenger Class')
plt.ylabel('Count of Passengers')
plt.title('Count of Passengers in Different Pclass')
plt.show()
