import pandas as pd

data = pd.read_csv("L4/titanic.csv")

# Get the particular column out of a condition
adult_names = data.loc[data["Age"] > 18, "Name"]
print(adult_names)

#Slicing - Same as numpy 2D slicing
# The first index is for rows and the second is for columns, follows the same syntax as range function
print(data.iloc[9:25, 2:5])

# Changing the value in the dataset
# Specify the number of rows and the particular column to change
data.iloc[0:3, 3] = "Pulkit Chawla"
print(data["Name"])

# Save the data to local to verify changes


# Creating a new column in the dataFrame
data["Test"] = data["Fare"] + 2
data["Test2"] = data["Fare"] * data["Pclass"] # Any mathematical operation could be considered
data.to_csv("L4/changedData.csv")
# Renaming the column names
data_renamed = data.rename(
    columns = {
        "Pclass": "Passenger Class",
        "Siblings/Spouses Aboard": "Sibling"
    }
)

print(data_renamed.columns)

# Performing mathematical operation on multiple columns together
print(data["Age"].mean())

print(data[["Age", "Fare"]].mean())

print(data.agg({
    "Age": ["min", "max", "median"],
    "Fare": ["min", "max", "median"]
}))

# Group by data categorically

print(data[["Sex", "Age"]].groupby("Sex").mean())

print(data.groupby("Sex")["Age"].mean())

# Task - Get the mean ticket price for each of sex and cabin class combination
print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

# Get the count of rows in each category
print(data["Pclass"].value_counts())

print(data.groupby("Pclass")["Pclass"].count())

# Sorting the data
x = data.sort_values(by = "Age", ascending = True)
print(x.head())
print(x[["Name", "Age"]].head())

data.sort_values(by = ["Pclass", "Age"], ascending = False)

# Operations on Text Data
data["NameLowercase"] = data["Name"].str.lower()
data.to_csv("L4/changedData.csv")
# Other Examples to be shown
#titanic["Name"].str.split(",")
#titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
#titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
