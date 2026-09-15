# E-Commerce Sales Analysis and Management Dashboard

## Project Overview

This project analyzes fictional e-commerce sales data for 12 months using **NumPy** and **Plotly**.

The goal is to analyze company performance across revenue, orders, customers, expenses, and profit, and present the results through interactive visualizations suitable for management.

## Objectives

The project focuses on:

* Tracking monthly revenue
* Tracking monthly orders
* Tracking monthly customers
* Tracking monthly expenses
* Calculating monthly profit
* Performing statistical analysis
* Identifying high-performing months
* Comparing revenue and expenses
* Understanding customer growth
* Creating a management performance dashboard

## Technologies and Libraries

### Programming Language

* Python 3.x

### Libraries

#### NumPy

Used for:

* Creating numerical arrays
* Generating fictional data
* Mathematical calculations
* Statistical calculations
* Filtering data
* Finding maximum and minimum values
* Calculating sums and averages

#### Plotly

Used for:

* Interactive visualizations
* Bar charts
* Line charts
* Management dashboard
* Interactive hover information
* Custom chart labels and titles

### Installation

Install the required libraries using:

```bash
pip install numpy plotly
```

## Dataset

The project uses fictional monthly e-commerce data for 12 months.

The following metrics are tracked:

| Metric    | Description                                       |
| --------- | ------------------------------------------------- |
| Revenue   | Total money earned from sales during the month    |
| Orders    | Total number of orders placed during the month    |
| Customers | Total number of customers during the month        |
| Expenses  | Total money spent by the company during the month |
| Profit    | Revenue minus expenses                            |

### Months

The analysis covers:

```text
January
February
March
April
May
June
July
August
September
October
November
December
```

## Data Generation

NumPy is used to generate fictional data.

A random seed is used to make the generated data reproducible.

```python
import numpy as np

np.random.seed(42)
```

Example:

```python
revenue = np.random.randint(80000, 200001, 12)
orders = np.random.randint(800, 2001, 12)
customers = np.random.randint(500, 1501, 12)
expenses = np.random.randint(40000, 120001, 12)
```

## Key Calculations

### Profit

Profit is calculated as:

```text
Profit = Revenue - Expenses
```

Python:

```python
profit = revenue - expenses
```
## Data Analysis

The project analyzes:

### Revenue

* Total revenue
* Average monthly revenue
* Highest revenue month
* Lowest revenue month
* Monthly revenue trends

### Orders

* Total orders
* Monthly order trends
* Highest order month

### Customers

* Monthly customer growth
* Customer trends over the year

### Expenses

* Total expenses
* Monthly expense trends
* Comparison between revenue and expenses

### Profit

* Monthly profit
* Total profit
* Highest profit month
* Profit margin

## Visualizations

The project uses Plotly to create interactive visualizations.

### 1. Revenue Trend

A line chart is used to visualize monthly revenue.

```python
px.line(
    x=months,
    y=revenue,
    title="Monthly Revenue Trends"
)
```

### 2. Monthly Orders

A bar chart is used to compare the number of orders across months.

```python
px.bar(
    x=months,
    y=orders,
    title="Monthly Orders"
)
```

### 3. Revenue vs Expenses

Revenue and expenses are compared using grouped bar charts.

This helps management understand the relationship between money earned and money spent.

### 4. Monthly Profit

Monthly profit is visualized using a bar chart.

```python
profit = revenue - expenses
```

### 5. Customer Growth

A line chart is used to show how the number of customers changes over the year.

```python
px.line(
    x=months,
    y=customers,
    title="Monthly Customer Growth"
)
```

## Management Dashboard

A final dashboard combines multiple visualizations into a single view using:

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go
```

The dashboard provides an overview of:

* Total Revenue
* Total Profit
* Total Orders
* Profit Margin
* Revenue vs Expenses
* Customer Growth

The dashboard is designed to help management quickly understand the company's financial and operational performance.

## Why These Metrics Matter

### Revenue

Shows how much money the business generates from sales.

### Expenses

Shows how much money the company spends to operate the business.

### Profit

Shows the amount remaining after expenses are deducted from revenue.

```text
Profit = Revenue - Expenses
```

### Orders

Shows the level of sales activity.

### Customers

Shows the size and growth of the customer base.

### Average Order Value

Shows how much customers spend per order on average.

## Project Structure

```text
super30-numpy-plotly-analytics/
│
├── super30-numpy-plotly-analytics.py
├── README.md
└── requirements.txt
```

## requirements.txt

The project requires:

```text
numpy
plotly
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## How to Run the Project

### 1. Clone or download the project

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Python file

```bash
python ecommerce_sales_analysis.py
```

Interactive Plotly visualizations will open/display when the program runs.

## Skills Demonstrated

This project demonstrates practical skills in:

* Python
* NumPy
* Array creation
* Array filtering
* Array reshaping
* Mathematical operations
* Statistical analysis
* Random data generation
* Data aggregation
* Business metrics
* Plotly Express
* Plotly Graph Objects
* Plotly Subplots
* Interactive visualization
* Dashboard creation
* Business-oriented data analysis

## Business Insights

The final dashboard can help answer questions such as:

* Which month generated the highest revenue?
* Which month generated the highest profit?
* Are expenses increasing along with revenue?
* Is the customer base growing?
* Which month had the highest number of orders?
* How profitable is the business?
* What is the average order value?
* Is the company generating enough profit relative to its expenses?

## Limitations

This project uses fictional data generated with NumPy for learning purposes.

The data does not represent actual sales transactions or real company performance.

For a real-world analysis, the dataset would typically contain additional information such as:

* Product
* Category
* Customer ID
* Order date
* Region
* Quantity
* Selling price
* Discount
* Cost
* Payment method
* Returns

## Future Improvements

Possible future enhancements include:

* Adding product-level analysis
* Adding regional sales analysis
* Adding customer segmentation
* Adding monthly growth percentages
* Adding sales forecasting
* Connecting the project to a real database
* Building a Power BI dashboard
* Adding machine learning for sales prediction

## Conclusion

This project demonstrates how Python, NumPy, and Plotly can be used to transform numerical sales data into meaningful business insights.

The final management dashboard provides a concise view of financial performance, sales activity, and customer growth, demonstrating both **technical data-analysis skills and business-oriented thinking**.
