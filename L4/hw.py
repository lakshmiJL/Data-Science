import pandas as pd

data = pd.read_csv("L4/titanic.csv")

# Mean fare of passengers with respect to sex and passenger class
mean_fare_by_class_sex = data.groupby(['Sex', 'Pclass'])['Fare'].mean()
print(mean_fare_by_class_sex)

median_age_deceased = data[data['Survived'] == 0].groupby('Sex')['Age'].median()
print("Median age of deceased passengers by sex:")
print(median_age_deceased)

mean_age_deceased = data[data['Survived'] == 0].groupby('Sex')['Age'].mean()
print("Mean age of deceased passengers by sex:")
print(mean_age_deceased)
