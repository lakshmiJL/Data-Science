import numpy as np
import pandas as pd

#Creating a series from a list
first_series = pd.Series(list("abcdef"))
print(first_series)

#Creating a series from a nd (n-dimensional) array
np_country = np.array(["USA", "China", "Mexico", "India", "Canada", "Switzerland", "Italy", "Austria", "Germany", "Russia"])
country = pd.Series(np_country)
print("/n")
print(country)

#Creating a series from a dictionary
age = pd.Series([887, 123, 456, 567, 987, 234, 999, 888, 408, 240], index = ["USA", "China", "Mexico", "India", "Canada", "Switzerland", "Italy", "Austria", "Germany", "Russia"] )
print(age)

#Series with Scalar (unidirectional) input
scalor_series = pd.Series(45.0, index = ["a", "b", "c", "d", "e"])
print(scalor_series)

#Access elements in series
print(age["India"])
print(age.iloc[3])
print(age.loc["Italy"])
#loc function is used for custom index names, whereas iloc is based on item index location

print(age.iloc[1:5])
print("\n")

#Vectorization: Vectorizing operations in series
first_vector_series = pd.Series([1, 2, 3, 4], index = ["a", "b", "c", "d"])
second_vector_series = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])

print(first_vector_series + second_vector_series)

second_vector_series = pd.Series([10, 20, 30, 40], index = ["a", "d", "b", "c"])

print(first_vector_series + second_vector_series)
print("\n")

second_vector_series = pd.Series([10, 20, 30, 40], index = ["a", "d", "e", "f"])

print(first_vector_series + second_vector_series)
print("\n")

#Creating data frames from a dictionary of list items
olympic_data_list = {"HostCity" : ["London", "Beijing", "Athens", "Sydney", "Atlanta"], "Year" : [2012, 2008, 2004, 2000, 1996], 
                     "Number of Participating Countries" : [205, 204, 201, 200, 197]}

df_olympic_data = pd.DataFrame(olympic_data_list)
print(df_olympic_data)
print("\n")

#Creating data frames from dictionaries of dictionary items
olympic_data_dict = {"London" : {2012 : 205}, "Beijing" : {2008 : 204}}
df_olympic_data_dict = pd.DataFrame(olympic_data_dict)
print(df_olympic_data_dict)
print("\n")

#Viewing Data Frames
print(df_olympic_data.HostCity)
print("\n")

#Describe function is used to display the content of the data frame
print(df_olympic_data.describe)