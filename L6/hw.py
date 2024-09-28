import pandas as pd
import matplotlib.pyplot as plt

# Read the Titanic data from a CSV file
titanic_data = pd.read_csv('L4/titanic.csv')

# Calculate the total number of men and women
gender_count = titanic_data['Sex'].value_counts()

# Plot bar graph for the total number of men and women
plt.figure(figsize=(8, 6))
gender_count.plot(kind='bar', color=['blue', 'pink'])
plt.title('Total Number of Men and Women in Titanic')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Calculate average fare for men and women
avg_fare_gender = titanic_data.groupby('Sex')['Fare'].mean()

# Plot bar graph for average fare of men and women
plt.figure(figsize=(8, 6))
avg_fare_gender.plot(kind='bar', color=['blue', 'pink'])
plt.title('Average Fare of Men and Women in Titanic')
plt.xlabel('Gender')
plt.ylabel('Average Fare')
plt.xticks(rotation=0)
plt.show()

# Calculate the number of people in different classes
class_count = titanic_data['Pclass'].value_counts()

# Plot pie chart for the number of people of different classes present
plt.figure(figsize=(8, 6))
class_count.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Distribution of Passenger Classes')
plt.ylabel('')
plt.show()
