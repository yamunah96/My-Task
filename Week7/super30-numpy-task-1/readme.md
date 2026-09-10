# NumPy Practice Exercises

A collection of beginner-friendly **NumPy exercises** covering array creation, statistical analysis, filtering, reshaping, indexing, mathematical operations, sorting, unique values, and 2D matrix operations.

## 📌 Topics Covered

* Array Creation
* Statistical Analysis
* Boolean Filtering
* Array Reshaping
* 2D Array Indexing
* Element-wise Mathematical Operations
* Random Number Generation
* Sorting
* Finding Unique Values
* Salary Data Analysis
* Matrix Operations
* Row-wise and Column-wise Aggregation

---

## 🛠️ Requirements

* Python 3.x
* NumPy

Install NumPy using:

```bash
pip install numpy
```

---

# 📚 Exercises

## 1. Array Creation

Create NumPy arrays containing:

* Numbers from 1 to 50
* Even numbers from 2 to 100
* Odd numbers from 1 to 99

### Concepts

* `np.arange()`
* Start, stop, and step
* Creating sequences using NumPy

```python
import numpy as np

a = np.arange(1, 51)
print(a)

even_array = np.arange(2, 101, 2)
print(even_array)

odd_array = np.arange(1, 101, 2)
print(odd_array)
```

---

## 2. Student Marks Analysis

Given the following student marks:

```python
marks = np.array([78, 85, 92, 67, 88, 73, 95, 60, 84, 91])
```

Find:

* Total marks
* Average
* Maximum
* Minimum
* Median

### Concepts

* `np.sum()`
* `np.mean()`
* `np.max()`
* `np.min()`
* `np.median()`

```python
marks = np.array([78, 85, 92, 67, 88, 73, 95, 60, 84, 91])

print(f"Total Marks: {np.sum(marks)}")
print(f"Average: {np.mean(marks)}")
print(f"Maximum: {np.max(marks)}")
print(f"Minimum: {np.min(marks)}")
print(f"Median: {np.median(marks)}")
```

---

## 3. Filtering

From the marks array, find students scoring:

* Above 90
* Above average
* Below 70

### Concepts

* Boolean indexing
* Boolean masking
* Conditional filtering

```python
scores_above_90 = marks[marks > 90]
print(f"Student scores above 90: {scores_above_90}")

above_average = marks[marks > np.mean(marks)]
print(f"Student scores above average: {above_average}")

below_70 = marks[marks < 70]
print(f"Student scores below 70: {below_70}")
```

### Key Idea

```python
marks[marks > 90]
```

means:

> Select values from `marks` where the condition `marks > 90` is `True`.

---

## 4. Reshaping

Create numbers from 1 to 20 and reshape them into a **4 × 5** array.

### Concepts

* `np.arange()`
* `reshape()`
* Rows and columns

```python
array = np.arange(1, 21)
print(array)

reshaped_array = array.reshape(4, 5)
print(reshaped_array)
```

Output:

```text
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]]
```

### Important Rule

The number of elements must remain the same.

```text
20 elements = 4 × 5
```

---

## 5. Two-Dimensional Array

Create a **3 × 3 matrix** and demonstrate:

* Row selection
* Column selection
* Individual element selection
* Slicing
* Negative indexing

```python
array = np.arange(1, 10).reshape(3, 3)
print(array)

# Row selection
print(array[1])

# Column selection
print(array[:, 1])

# Individual element selection
print(array[2, 1])

# Slicing
print(array[0:2, ::2])

# Negative indexing
print(array[-2:, -2:])
```

### Key Indexing Pattern

```python
array[row, column]
```

Examples:

```python
array[1]       # Second row
array[:, 1]    # Second column
array[2, 1]    # Individual element
```

### Negative Indexing

```python
array[-2:, -2:]
```

selects the last two rows and last two columns.

---

## 6. Mathematical Operations

Given:

```python
a = np.array([10, 20, 30, 40, 50])
b = np.array([5, 10, 15, 20, 25])
```

Perform:

* Addition
* Subtraction
* Multiplication
* Division

```python
a = np.array([10, 20, 30, 40, 50])
b = np.array([5, 10, 15, 20, 25])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

### Key Concept: Element-wise Operations

NumPy performs operations position by position.

```text
10 + 5   = 15
20 + 10  = 30
30 + 15  = 45
```

The same principle applies to subtraction, multiplication, and division.

---

## 7. Statistical Analysis

Generate **100 random integers between 1 and 100** and calculate:

* Mean
* Median
* Standard deviation
* Variance

```python
np.random.seed(42)

data = np.random.randint(1, 101, 100)

print(data)

print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Standard Deviation: {np.std(data)}")
print(f"Variance: {np.var(data)}")
```

### Concepts

#### Mean

Represents the average value of the dataset.

#### Median

Represents the central position of the dataset and is less affected by extreme values.

#### Standard Deviation

Describes how much the values typically vary around the mean, in the original units.

#### Variance

Measures overall variability by using squared deviations from the mean.

### Reproducibility

```python
np.random.seed(42)
```

ensures that the same random numbers are generated each time the code runs.

---

## 8. Sorting

Create an unsorted NumPy array and display:

* Ascending order
* Descending order

```python
np.random.seed(42)

data = np.random.randint(1, 101, 10)
print(data)

# Ascending order
data.sort()
print(data)

# Descending order
print(np.sort(data)[::-1])
```

### Important Difference

```python
data.sort()
```

modifies the original array.

Whereas:

```python
np.sort(data)
```

returns a sorted copy.

### Descending Order

```python
np.sort(data)[::-1]
```

The `[::-1]` reverses the sorted array.

---

## 9. Unique Values

Given:

```python
data = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
```

Find the unique values.

```python
data = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

print(np.unique(data))
```

Output:

```text
[1 2 3 4 5 6]
```

### Concept

`np.unique()` removes duplicate values and returns each distinct value once.

---

## 10. Exercise

> Exercise 10 is not included in the current practice set.

---

## 11. Salary Analysis

Create salary data for **15 employees**.

Find:

* Highest salary
* Lowest salary
* Average salary
* Employees earning above average
* Index positions of employees earning above average

```python
salary_data = np.array([
    5000, 10222, 11800, 5600, 7890,
    20000, 4590, 15000, 12500, 3500,
    13450, 12980, 9040, 7800, 5600
])

print(salary_data)

print("Highest salary:", np.max(salary_data))

print("Lowest salary:", np.min(salary_data))

print("Average salary:", np.mean(salary_data))

print(
    "Employees earning above average:",
    salary_data[salary_data > np.mean(salary_data)]
)

print(
    "Employee indices earning above average:",
    np.where(salary_data > np.mean(salary_data))
)
```

### Concepts

* Aggregation
* Mean comparison
* Boolean filtering
* `np.where()`
* Indexing

### `np.where()`

```python
np.where(condition)
```

returns the positions where the condition is `True`.

---

## 12. 5 × 5 Random Matrix Challenge

Generate a **5 × 5 random integer matrix** and determine:

* Maximum value
* Minimum value
* Row-wise sum
* Column-wise sum

```python
np.random.seed(42)

matrix = np.random.randint(1, 100, (5, 5))

print("Matrix:")
print(matrix)

print(f"Maximum value: {np.max(matrix)}")

print(f"Minimum value: {np.min(matrix)}")

# Row-wise sum
print(f"Row-wise sum: {np.sum(matrix, axis=1)}")

# Column-wise sum
print(f"Column-wise sum: {np.sum(matrix, axis=0)}")
```

### Understanding `axis`

This is an important NumPy concept.

```python
np.sum(matrix, axis=1)
```

→ Adds values **across each row**

```python
np.sum(matrix, axis=0)
```

→ Adds values **down each column**

### Easy Way to Remember

```text
axis=0 → column-wise result
axis=1 → row-wise result
```

---

# 🧠 NumPy Functions Practiced

| Function              | Purpose                             |
| --------------------- | ----------------------------------- |
| `np.arange()`         | Create sequences                    |
| `np.array()`          | Create NumPy arrays                 |
| `np.reshape()`        | Change array shape                  |
| `np.sum()`            | Calculate total                     |
| `np.mean()`           | Calculate average                   |
| `np.median()`         | Calculate median                    |
| `np.max()`            | Find maximum                        |
| `np.min()`            | Find minimum                        |
| `np.std()`            | Calculate standard deviation        |
| `np.var()`            | Calculate variance                  |
| `np.random.randint()` | Generate random integers            |
| `np.random.seed()`    | Make random generation reproducible |
| `np.sort()`           | Return sorted array                 |
| `.sort()`             | Sort array in place                 |
| `np.unique()`         | Find unique values                  |
| `np.where()`          | Find positions matching a condition |

---

# 🎯 Key Concepts Learned

By completing these exercises, the following NumPy fundamentals are practiced:

### 1. Array Creation

```python
np.array()
np.arange()
np.random.randint()
```

### 2. Indexing

```python
array[1]
array[2, 1]
array[:, 1]
```

### 3. Slicing

```python
array[0:2]
array[-2:]
array[::-1]
```

### 4. Boolean Filtering

```python
marks[marks > 90]
marks[marks < 70]
```

### 5. Reshaping

```python
array.reshape(4, 5)
```

### 6. Aggregation

```python
np.sum()
np.mean()
np.max()
np.min()
```

### 7. Statistical Measures

```python
np.median()
np.std()
np.var()
```

### 8. Axis Operations

```python
np.sum(matrix, axis=0)
np.sum(matrix, axis=1)
```


