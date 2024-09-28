import numpy as np
sample = [1,2,3,4]
print(type(sample))

sample_numpy = np.array(sample)
print(type(sample_numpy))

#error_array = np.array([1,2,4],"name")

arrayzero = np.zeros(5)
print(arrayzero)

onesarray = np.ones(5)
print(onesarray)

floatarray = np.array([1,2,3,4,5],dtype = "f")
print(floatarray)

#array_2d_error = np.array([[1,2],[3]])
#print(array_2d_error)

array_2d = np.array([[1,2],[3,4]])
print(array_2d)

print(array_2d.ndim)
print(array_2d.shape)
print(array_2d.size)
print(array_2d.nbytes)

num_array = np.arange(1,101)
print(num_array)

even_array = np.arange(2,100,2)
print(even_array)

random_arr = np.random.permutation(np.arange(1,10))
print(random_arr)

random_num = np.random.randint(1,10)
print(random_num)

random_array = np.random.rand(2,3)
print(random_array)
print(random_array.shape)

reshaped_array = np.arange(1, 10).reshape(3,3)
print(reshaped_array)
print(reshaped_array.shape)

linear_array = np.arange(1,37)

print(linear_array.reshape(6,6))
print(linear_array.reshape(12, 3))
print(linear_array.reshape(18,2))


random_array = np.random.permutation(np.arange(1,10))
print(random_array)
sorted_array = np.sort(random_array)
print(sorted_array)