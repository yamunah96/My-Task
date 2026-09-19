# FastAPI Course Management API

A simple Course Management REST API built with FastAPI and Pydantic.

This project demonstrates how to build API endpoints for creating courses, retrieving all courses, and filtering courses by category, price range, and active status.

The project uses an in-memory Python dictionary as the data store, so the data is not persistent and will be reset whenever the application restarts.

## Features

* Create a new course
* Automatically generate course IDs
* Prevent duplicate courses based on course title
* Retrieve all courses
* Filter courses by category
* Filter courses by price range
* Filter courses by active/inactive status
* Validate request data using Pydantic
* Automatically generate interactive API documentation using FastAPI

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
fastapi-course-api/
│
├── main.py
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd fastapi-course-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

## Running the Application

Run the application using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## Course Model

The API validates course data using Pydantic.

| Field       | Type                  | Validation                   | Required |
| ----------- | --------------------- | ---------------------------- | -------- |
| title       | string                | Minimum 3 characters         | Yes      |
| description | string                | Maximum 100 characters       | Yes      |
| price       | float                 | Greater than 0               | Yes      |
| duration    | integer               | Greater than 0               | Yes      |
| instructor  | string                | Minimum 3 characters         | Yes      |
| category    | list of strings       | Maximum 10 categories        | No       |
| rating      | float                 | Greater than 1 and maximum 5 | Yes      |
| active      | `"true"` or `"false"` | Literal values               | Yes      |

## API Endpoints

### 1. Create a Course

```http
POST /create_course/
```

Creates a new course.

The course ID is generated automatically using the highest existing course ID plus one.

The client does not need to provide an ID.

#### Request Body

```json
{
    "title": "Python for Data Analysis",
    "description": "Learn Python for data analysis and practical projects",
    "price": 4999,
    "duration": 45,
    "instructor": "Yamuna",
    "category": [
        "Python",
        "Data Analytics",
        "Data Science"
    ],
    "rating": 4.7,
    "active": "true"
}
```

#### Successful Response

```json
{
    "message": "Python for Data Analysis course created successfully",
    "course": {
        "title": "Python for Data Analysis",
        "description": "Learn Python for data analysis and practical projects",
        "price": 4999,
        "duration": 45,
        "instructor": "Yamuna",
        "category": [
            "Python",
            "Data Analytics",
            "Data Science"
        ],
        "rating": 4.7,
        "active": "true",
        "id": 6
    }
}
```

#### Duplicate Course

Course titles are checked without considering uppercase/lowercase differences.

For example:

```text
Beginner Python
beginner python
BEGINNER PYTHON
```

are treated as the same course.

Response:

```json
{
    "message": "Course already exists",
    "course": {
        "id": 1,
        "title": "Beginner Python"
    }
}
```

## 2. Get All Courses

```http
GET /get_courses
```

Returns all available courses.

### Example Response

```json
{
    "message": "courses data fetched successfully",
    "courses": {
        "1": {
            "title": "Beginner Python",
            "price": 1999,
            "active": false
        },
        "2": {
            "title": "SQL Beginner to Advanced",
            "price": 3999,
            "active": true
        }
    }
}
```

## 3. Get Courses by Category

```http
GET /get_course/category
```

Returns all courses that belong to a specified category.

### Query Parameter

```text
category
```

### Example

```text
GET /get_course/category?category=python
```

### Example Response

```json
{
    "message": "courses found for category :python",
    "course": [
        {
            "title": "Beginner Python",
            "price": 1999,
            "category": [
                "Python",
                "Data Science",
                "Data Analytics",
                "AI",
                "ML"
            ]
        },
        {
            "title": "Machine Learning with Python",
            "price": 6999,
            "category": [
                "Python",
                "Machine Learning",
                "AI",
                "Data Science"
            ]
        }
    ]
}
```

Category matching is case-insensitive.

For example:

```text
python
Python
PYTHON
```

will match the same courses.

## 4. Get Courses by Price Range

```http
GET /get_course/price
```

Returns all courses whose price falls within the specified range.

### Query Parameters

| Parameter | Type  | Description   |
| --------- | ----- | ------------- |
| min_price | float | Minimum price |
| max_price | float | Maximum price |

### Example

```text
GET /get_course/price?min_price=2000&max_price=7000
```

The API checks:

```python
min_price <= course["price"] <= max_price
```

Therefore, both boundary values are included.

For example, with:

```text
min_price = 2000
max_price = 7000
```

a course costing exactly `2000` or `7000` will be included.

### Example Response

```json
{
    "message": "courses found for btw 2000.0-7000.0",
    "course": [
        {
            "title": "SQL Beginner to Advanced",
            "price": 3999
        },
        {
            "title": "Machine Learning with Python",
            "price": 6999
        }
    ]
}
```

## 5. Get Active or Inactive Courses

```http
GET /get_course/active
```

Returns courses based on their active status.

### Query Parameter

```text
active
```

The parameter accepts a Boolean value:

```text
true
false
```

### Get Active Courses

```text
GET /get_course/active?active=true
```

Returns courses where:

```python
course["active"] == True
```

### Get Inactive Courses

```text
GET /get_course/active?active=false
```

Returns courses where:

```python
course["active"] == False
```

### Example Response

```json
{
    "message": "The active courses",
    "course": [
        {
            "title": "SQL Beginner to Advanced",
            "price": 3999,
            "active": true
        },
        {
            "title": "Machine Learning with Python",
            "price": 6999,
            "active": true
        }
    ]
}
```

## Validation Examples

The API uses Pydantic to validate incoming course data.

### Invalid Title

```json
{
    "title": "Py"
}
```

The title fails because the minimum length is 3 characters.

### Invalid Price

```json
{
    "price": -500
}
```

The price fails because it must be greater than 0.

### Invalid Duration

```json
{
    "duration": 0
}
```

The duration must be greater than 0.

### Invalid Rating

```json
{
    "rating": 5.5
}
```

The rating fails because the maximum allowed value is 5.

### Invalid Active Value

```json
{
    "active": "yes"
}
```

The `active` field only accepts:

```text
true
false
```

as defined by the Pydantic `Literal` type.

## Current Sample Data

The API contains five sample courses:

1. Beginner Python
2. SQL Beginner to Advanced
3. Machine Learning with Python
4. Power BI Data Analytics
5. Deep Learning Fundamentals

The sample data contains both active and inactive courses and multiple categories such as:

* Python
* SQL
* Data Science
* Data Analytics
* AI
* Machine Learning
* Deep Learning
* Power BI
* Database
* Business Intelligence
* Computer Vision

## How Course IDs Are Generated

Course IDs are automatically generated.

If the existing IDs are:

```text
1
2
3
4
5
```

the next course receives:

```text
6
```

The implementation is:

```python
if course_data:
    truet_id = max(course_data.keys()) + 1
else:
    truet_id = 1
```

This approach is suitable for the current in-memory learning project.

For a production application, IDs should normally be generated by the database.

## Data Storage

Currently, courses are stored in a Python dictionary:

```python
course_data = {}
```

Example:

```python
course_data = {
    1: {
        "title": "Beginner Python",
        "price": 1999
    },
    2: {
        "title": "SQL Beginner to Advanced",
        "price": 3999
    }
}
```

This means the application does not use a database.

All data will be lost when the application stops or restarts.

## Example CRUD Roadmap

The project can eventually follow this CRUD structure:

| Operation      | HTTP Method | Endpoint                     |
| -------------- | ----------- | ---------------------------- |
| Create         | POST        | `/create_course/`            |
| Read all       | GET         | `/get_courses`               |
| Read one       | GET         | `/get_course/{course_id}`    |
| Update         | PUT         | `/update_course/{course_id}` |
| Partial update | PATCH       | `/update_course/{course_id}` |
| Delete         | DELETE      | `/delete_course/{course_id}` |

## Author

Yamuna
