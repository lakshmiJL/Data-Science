# Refer the LP for concepts to be discussed before starting with the code

import pandas as pd

# Create a dataFrame from scratch to relate a dataFrame with a dictionary
df = pd.DataFrame({
    "Name": ["Pulkit Chawla", "Tom Brouwers"],
    "Age": [23, 14],
    "City": ["Agra", "Amsterdam"]
})

# Show the number of rows in the head could be limited by passing a number in head
print(df.head())
print(df.shape)
# Show the way of accessing the column is same as that as of a dictionary
print(df["Name"])
# Also all numpy operations are applicable to the column (pd.Series)
print(df["Age"].max())
print(type(df["Age"]))
print(df["Age"].shape)

# Gives the typical summary of the data
print(df.info())
# Gives the important calculations on the numerical columns
print(df.describe())

# Loading the data from a file
data = pd.read_csv("Datasets/iris.csv")
print(data.head())
print(data.info())
# Prints the datatypes of each column
print(data.dtypes)

# Selecting multiple columns together
nameAndAge = data[["sepal_length","sepal_width"]]

print(nameAndAge.head())
print(nameAndAge.shape)


# Filtering out rows
above5 = data[data["sepal_length"] > 5]
print(above5.head())
print(above5.shape) # To confirm the number of rows, open the csv in excel and filter on the same column
# Calculate mean, min, max for specific columns
selected_columns = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']
summary_stats = data[selected_columns].agg(['mean', 'min', 'max'])
print("\nSummary Statistics:")
print(summary_stats)

# Count of rows for each species
species_counts = data['species'].value_counts()
print("\nCount of rows for each species:")
print(species_counts)
