'''
1. Array Creation

Create NumPy arrays containing
Numbers 1 to 50
Even numbers 2 to 100
Odd numbers 1 to 99
'''

import numpy as np

a=np.arange(1,51)
print(a)

even_array= np.arange(2,101,2)
print(even_array)

odd_array= np.arange(1,101,2)
print(odd_array)


'''
2
Student Marks Analysis
Create
marks = np.array([78, 85, 92, 67, 88,73, 95, 60, 84, 91])

Find: Total marks,Average,Maximum,Minimum,Median'''

marks=np.array([78, 85, 92, 67, 88,73, 95, 60, 84, 91])
print(f"Total Marks: {np.sum(marks)}")
print(f"Average: {np.mean(marks)}")
print(f"Maximum: {np.max(marks)}")
print(f"Minimum: {np.min(marks)}")
print(f"Median: {np.median(marks)}")



'''3
Filtering
From the marks array, find students scoring
Above 90
Above average
Below 70'''

# above 90
scores_above_90 =marks[marks>90]
print(f"student scores above 90: {scores_above_90}")

# above average
above_average = marks[marks>np.mean(marks)]
print(f"student scores above_average: {above_average}")

# Below 70
below_70= marks[marks<70]
print(f"student scores below 70: {below_70}")



'''4 Reshaping-  Create numbers 1 to 20 and reshape them into 4 X 5 '''

array= np.arange(1,21)
print(array)

reshaped_array= array.reshape(4,5)  # 4 rows 5 columns
print(reshaped_array)

'''
5- Two-Dimensional Array
Create a 3×3 matrix and demonstrate
Row selection
Column selection
Individual element selection
'''
array=np.arange(1,10).reshape(3,3)
print(array)

# row selection
print(array[1]) # accessing second row 

# column selection
print(array[:,1]) # accessing second column

# individual element selection
# access number 8
print(array[2,1])

# access number [1 4] [3 6]

print(array[0:2,::2])

# negative indexing [5 6][8 9]
print(array[-2:,-2:])


'''
6 Mathematical Operations
For
a = np.array([10, 20, 30, 40, 50])
b = np.array([5, 10, 15, 20, 25])
perform- Addition,Subtraction,Multiplication,Division
'''
a = np.array([10, 20, 30, 40, 50])
b = np.array([5, 10, 15, 20, 25])
print("Addition: ",a+b)

print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)


'''
7. Statistical Analysis
Generate 100 random numbers and calculate
Mean,Median,Standard deviation,Variance
'''
np.random.seed(42)
data= np.random.randint(1, 101, 100)
print(data)
print(f"mean: {np.mean(data)}")
print(f"median: {np.median(data)}")
print(f"std: {np.std(data)}")
print(f"variance: {np.var(data)}")


'''8
Sorting: Create an unsorted NumPy array and display ascending and descending results.'''
np.random.seed(42)
data= np.random.randint(1, 101, 10)
print(data)

# ascending order
data.sort()
print(data)

# descending order
print(np.sort(data)[::-1])

'''9.Unique Values Given [1,2,2,3,3,3,4,5,5,6] find unique values.'''
data=[1,2,2,3,3,3,4,5,5,6]
print(np.unique(data))


'''11. Salary Analysis

Create salary data for 15 employees.
Find
Highest salary
Lowest salary
Average salary
Employees earning above average'''
np.random.seed(42)
salary_data= np.array([5000,10222,11800,5600,7890,20000,4590,15000,12500,3500,13450,12980,9040,7800,5600])
print(salary_data)

print("Highest salary: ",np.max(salary_data))
print("Lowest salary: ",np.min(salary_data))
print("Employess salary earning above average: ",salary_data[salary_data>np.mean(salary_data)])
print("Employees earning above average: ",np.where(salary_data>np.mean(salary_data)))


'''
12
Challenge
Generate a 5×5 random integer matrix and determine
Maximum value
Minimum value
Row-wise sum
Column-wise sum
'''
np.random.seed(42)
matrix= np.random.randint(1,100,(5,5))
print("Matrix")
print(matrix)

# row wise sum
print(f"Maximum value: {np.max(matrix)}")

print(f"Minimum value: {np.min(matrix)}")

# rowwise sum
print(f"Row wise sum: {np.sum(matrix,axis=1)}") # axis 1 means adds the elements row-wise

# column wise sum
print(f"Column wise sum: {np.sum(matrix,axis=0)}") # axis 0 means adds the elements column-wise