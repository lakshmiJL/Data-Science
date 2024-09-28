# Hello World of Machine Learning
# Iris Data Machine Learning Project

# The main purpose of this Project is to get the kid accustomed with the steps of machine learning project discussed in the previous lesson
# The child must be able to relate the sequence of steps in order, understand the need of them

# Import the Required Libraries at the top, No need to explain the DecisionTree Thing, Would be discussed in detail during the ML stuff
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Splitting the data into training and testing
from sklearn.model_selection import train_test_split
# Algorithm that we would be using
from sklearn.tree import DecisionTreeClassifier
# for finding accuracy
from sklearn import metrics

from sklearn.metrics import accuracy_score, classification_report
# get the data into the program
data = pd.read_csv('L4/titanic.csv')

# verify that the data has been successfully imported
print(data.head())
print(data.info())

# data preprocessing
# replacing na in age
data['Age'].fillna(data['Age'].median(), inplace=True)
# Convert 'Sex' column to numerical using label encoding
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
# Extract titles from 'Name' column
data['Title'] = data['Name'].str.extract(r',\s*([^,]*)\.', expand=False)

# Display the updated dataset until the 'Fare' column
print(data.head())


# Define the features (X) and the target variable (y)
features = data.drop(['Survived'], axis=1)
target = data['Survived']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
predictions = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Generate classification report
print("\nClassification Report:")
print(classification_report(y_test, predictions))