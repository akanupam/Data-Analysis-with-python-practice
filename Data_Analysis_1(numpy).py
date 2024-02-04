

'''Simple calculation of yield of apples in a region'''

weight = [0.3, 0.2, 0.5]

Kanto = [73, 67, 43]
Johto = [91, 88, 64]
Hoenn = [87, 134, 58]
Sinnoh = [102, 43, 37]
Unova = [69, 96, 70]

# def yield_of_apples(weight, region):
#     s = 0
#     for x, w in weight,region:
#         s += x*w
#     return s
'''or'''
# def yield_of_apples(weight, region):
#     s = 0
#     for i in range(len(weight)):
#         s += weight[i]*region[i]
#     return s

# print(yield_of_apples(weight,Unova))


''' Using numpy module'''


# import numpy as np 
# Kanto = np.array(Kanto) # converting list to numpy array
# weight = np.array(weight)
# print(Kanto)
# print(weight)
# print((Kanto*weight).sum()) #multiplying list elements simltaneously and summing that up

# print(type(Kanto))  # numpy.ndarray
# print(type(weight)) 

# print(weight[2]) # accessing values using slicing

'''dot product'''

# print(np.dot(Kanto, weight))
# np.dot(Kanto,weight) = (Kanto*wight).sum()

# arr1 = list(range(1000000))
# arr2 = list(range(1000000,2000000))

# arr1_np = np.array(arr1)
# arr2_np = np.array(arr2)

# print(type(arr2_np))

# result = 0
# for x,w in zip(arr1, arr2):
#     result += x*w
# print(result)



# x = np.dot(arr1_np, arr2_np)
# print(x)


# climate_data = np.array([[73, 67, 43],
#                          [91, 88, 64],
#                          [87, 134, 58],
#                          [102, 43, 37],
#                          [69, 96, 70]])

# print(climate_data)
# print(climate_data.shape) 
''' gives you the dimension of the matrix'''

# arr3 = np.array([[[11,12,12],
#                   [13,14,15]],
#                   [[15,16,17],
#                   [17,18,19.5]]])

# print(arr3.shape)
# print(weight.dtype)
# print(climate_data.dtype)
# print(arr3.dtype)


'''multiplication of matrix'''
# print(np.matmul(climate_data,weight))
'''or'''
# print(climate_data @ weight)


import numpy as np
# import urllib.request 
# urllib.request.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 'climate.txt')

# climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
# print(climate_data)
# print(climate_data.shape)
# print(climate_data.dtype)

# weight = np.array([0.3, 0.2, 0.5])
# yields = climate_data @ weight
# print(yields)
# print(yields.shape)
'''
concatenation of calculated yield to the climate data
'''
# climate_results = np.concatenate((climate_data, yields.reshape(10000,1)), axis=1 ) 
# print(climate_results)



# exam = np.concatenate(([[0,1,2,3],[4,5,6,7]],[[0,1,2,3],[4,5,6,7]]), axis=1)
# print(exam)
'''
saving the the concatenated data to a new file
'''

# np.savetxt ('climate_results.txt',climate_results,
#            fmt = '%.2f',
#            delimiter=',',
#            header = 'temperature,rainfall,humidity,yield',
#            comments = '')

'''

Numpy provides hundreds of functions for performing operations on arrays. Here are some commonly used functions:

Mathematics: np.sum, np.exp, np.round, arithemtic operators
Array manipulation: np.reshape, np.stack, np.concatenate, np.split
Linear Algebra: np.matmul, np.dot, np.transpose, np.eigvals
Statistics: np.mean, np.median, np.std, np.max

'''

# arr2 = np.array([[1,2,3,4],[5,6,7,8],[9,1,2,3]])
# arr3 = np.array([[11,12,13,14],[15,16,17,18],[19,11,12,13]])
# print(arr2)
# print(arr3)

# print(arr2 + 3)
# print(arr3-arr2)

# print(arr2/2)

# print(arr2*arr3)
# print(arr2%4)

# print(arr2.shape)
# arr4 = np.array([4,5,6,7])
# print(arr4.shape)

# print(arr2 + arr4) # interesting

arr1 = np.array([[1, 2, 3], [3, 4, 5]])
arr2 = np.array([[2, 2, 3], [1, 2, 5]])

# print(arr1 == arr2)
# print(arr1!= arr2)
# >=,<=,>,<

# print(arr1 >= arr2)
# print((arr1 >= arr2).sum()) # sums up the number of true values or say true is taken as 1 and false as 0

'''

Indexing and slicing in numpy

'''
# arr3 = np.array([
#     [[11, 12, 13, 14], 
#      [13, 14, 15, 19]], 
    
#     [[15, 16, 17, 21], 
#      [63, 92, 36, 18]], 
    
#     [[98, 32, 81, 23],      
#      [17, 18, 19.5, 43]]])

# print(arr3.shape)
# print(arr3[1, 1, 2]) #for single elements

# print(arr3[0:3,0:2,1]) #for subarray

# print(arr3[1])

'''
Other ways of creating numpy arrays

'''
# print(np.zeros((3,4))) # gives zero matrix
# print(np.ones((2,2,3))) #gives matrix with all values 1

# print(np.eye(5)) # gives identity matrix

'''random vector'''
# print(np.random.rand(5))

'''random matrix'''
# print(np.random.randn(2,3))

'''fixed value'''
# print(np.full([4,3],65))

'''range with start, end and step'''

# print(np.arange(10,70,7))

'''equally spaced numbers in range'''
# print(np.linspace(3,27,18))



