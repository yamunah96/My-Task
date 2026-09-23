# Student Management API

A simple **Student Management REST API** built using **FastAPI** and **Pydantic**.

This project demonstrates how to build a CRUD-based API with request validation, custom Pydantic validators, PUT updates, and properly validated partial PATCH updates.

---

## Features

* Create a new student
* Get all students
* Get a student by ID
* Replace a complete student using PUT
* Partially update a student using PATCH
* Delete a student
* Validate student input using Pydantic
* Validate email format using `EmailStr`
* Restrict email domains
* Validate student names
* Validate student age
* Automatically convert names to lowercase
* Automatically generate student IDs
* Interactive API documentation using Swagger UI

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Email Validator

---

## Project Structure

```text
student-management/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 2. Install Dependencies

Install the required packages:

```bash
pip install fastapi uvicorn email-validator
```

Or create a `requirements.txt` file:

```text
fastapi
uvicorn
email-validator
```

Then install:

```bash
pip install -r requirements.txt
```

---

# Running the Application

If your Python file is named `main.py`:

```bash
uvicorn main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test all API endpoints directly from your browser.

## ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

---

# Data Model

The project uses two Pydantic models:

```text
StudentCreate
     |
     |-- POST
     |-- PUT
     
StudentUpdate
     |
     |-- PATCH
```

The reason for using two models is that POST and PUT require complete student information, while PATCH allows only the fields that need to be changed.

---

# StudentCreate Model

`StudentCreate` is used for:

* POST
* PUT

```python
class StudentCreate(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=100)]
    age: Annotated[int, Field(gt=0, lt=100)]
    email: EmailStr
    address: Annotated[str, Field(min_length=1, max_length=200)]
```

All fields are required.

| Field     | Type       | Validation                          |
| --------- | ---------- | ----------------------------------- |
| `name`    | `str`      | 1–100 characters, alphabets only    |
| `age`     | `int`      | 1–99                                |
| `email`   | `EmailStr` | Valid email format + allowed domain |
| `address` | `str`      | 1–200 characters                    |

---

# StudentUpdate Model

`StudentUpdate` is used for PATCH.

```python
class StudentUpdate(BaseModel):
    name: Optional[Annotated[str, Field(min_length=1, max_length=100)]] = None
    age: Optional[Annotated[int, Field(gt=0, lt=100)]] = None
    email: Optional[EmailStr] = None
    address: Optional[Annotated[str, Field(min_length=1, max_length=200)]] = None
```

All fields are optional because PATCH only updates the fields provided by the client.

For example:

```json
{
    "age": 25
}
```

is valid.

There is no need to send:

```json
{
    "name": "...",
    "email": "...",
    "address": "..."
}
```

when only the age needs to be changed.

---

# Validation

## Name Validation

The name must contain only alphabets.

Valid:

```text
Yamuna
Rahul
Priya
```

Invalid:

```text
Rahul123
Priya@
John Doe
```

The name is automatically converted to lowercase.

For example:

```text
YAMUNA
```

becomes:

```text
yamuna
```

This validation is implemented using:

```python
@field_validator("name")
@classmethod
def validate_name(cls, value):
    if not value.isalpha():
        raise ValueError("Name must contain only alphabets")

    return value.lower()
```

---

# Age Validation

Age must be between `1` and `99`.

This is handled by:

```python
Field(gt=0, lt=100)
```

Valid:

```text
20
35
99
```

Invalid:

```text
0
100
-5
```

---

# Email Validation

`EmailStr` checks whether the value is in a valid email format.

The project also adds a custom business rule that only these domains are allowed:

```text
gmail.com
yahoo.com
outlook.com
```

Valid:

```text
student@gmail.com
student@yahoo.com
student@outlook.com
```

Invalid:

```text
student@example.com
```

The custom validation is implemented using:

```python
@field_validator("email")
@classmethod
def validate_email(cls, value):
    valid_domains = ["gmail.com", "yahoo.com", "outlook.com"]

    domain = value.split("@")[-1]

    if domain not in valid_domains:
        raise ValueError(
            "Email domain must be one of: gmail.com, yahoo.com, outlook.com"
        )

    return value
```

---

# API Endpoints

| Method | Endpoint         | Purpose                  |
| ------ | ---------------- | ------------------------ |
| POST   | `/students`      | Create student           |
| GET    | `/students`      | Get all students         |
| GET    | `/students/{id}` | Get student by ID        |
| PUT    | `/students/{id}` | Replace complete student |
| PATCH  | `/students/{id}` | Partially update student |
| DELETE | `/students/{id}` | Delete student           |

---

# 1. Create Student

## POST `/students`

Creates a new student.

### Request Body

```json
{
    "name": "Rahul",
    "age": 22,
    "email": "rahul@gmail.com",
    "address": "Bangalore"
}
```

The name will be converted to lowercase:

```text
rahul
```

### Example Response

```json
{
    "message": "Student created successfully",
    "student": {
        "name": "rahul",
        "age": 22,
        "email": "rahul@gmail.com",
        "address": "Bangalore"
    }
}
```

The student ID is automatically generated using the maximum existing ID plus one.

---

# 2. Get All Students

## GET `/students`

Returns all students currently stored in the application.

### Example Response

```json
{
    "message": "List of students",
    "students": {
        "1": {
            "name": "yamuna",
            "age": 20,
            "email": "y@gmail.com",
            "address": "bangalore"
        }
    }
}
```

---

# 3. Get Student by ID

## GET `/students/{id}`

Example:

```text
GET /students/1
```

### Successful Response

```json
{
    "message": "Student found",
    "student": {
        "name": "yamuna",
        "age": 20,
        "email": "y@gmail.com",
        "address": "bangalore"
    }
}
```

If the student does not exist:

```json
{
    "message": "Student not found"
}
```

---

# 4. Replace Student

## PUT `/students/{id}`

PUT is used to replace the complete student record.

This endpoint uses the `StudentCreate` model, so all fields are required.

### Request

```json
{
    "name": "Yamuna",
    "age": 21,
    "email": "yamuna@gmail.com",
    "address": "Bangalore"
}
```

### Important

Because PUT represents a complete replacement, sending only:

```json
{
    "age": 21
}
```

will result in a validation error because `name`, `email`, and `address` are required.

---

# 5. Partially Update Student

## PATCH `/students/{id}`

PATCH is used when only specific fields need to be changed.

For example:

```json
{
    "age": 25
}
```

Only the age will be updated.

Another example:

```json
{
    "address": "Chennai"
}
```

Only the address will be updated.

You can also update multiple fields:

```json
{
    "age": 25,
    "address": "Mumbai"
}
```

---

# PATCH Validation

The PATCH endpoint uses:

```python
StudentUpdate
```

where every field is optional.

However, optional does not mean that validation is removed.

For example:

```json
{
    "age": 150
}
```

will fail because:

```python
Field(gt=0, lt=100)
```

only allows ages from `1` to `99`.

Similarly:

```json
{
    "name": "Rahul123"
}
```

will fail because the custom name validator only allows alphabets.

---

## `exclude_unset=True`

The PATCH implementation uses:

```python
update_data = student_update.model_dump(exclude_unset=True)
```

This is important for partial updates.

Suppose the client sends:

```json
{
    "age": 25
}
```

Without `exclude_unset=True`, the model contains optional fields with default `None`.

With:

```python
model_dump(exclude_unset=True)
```

only the field actually supplied by the client is returned:

```python
{
    "age": 25
}
```

Then the code updates only that field:

```python
for key, value in update_data.items():
    if key in student_data[id]:
        student_data[id][key] = value
```

---

# 6. Delete Student

## DELETE `/students/{id}`

Deletes a student using their ID.

Example:

```text
DELETE /students/1
```

### Successful Response

```json
{
    "message": "Student deleted successfully"
}
```

If the student does not exist:

```json
{
    "message": "Student not found"
}
```

---

# CRUD Operations

This project demonstrates all four basic CRUD operations.

| CRUD Operation | HTTP Method | Endpoint         |
| -------------- | ----------- | ---------------- |
| Create         | POST        | `/students`      |
| Read           | GET         | `/students`      |
| Update         | PUT / PATCH | `/students/{id}` |
| Delete         | DELETE      | `/students/{id}` |

---

# PUT vs PATCH

A key concept demonstrated by this project is the difference between PUT and PATCH.

## PUT

PUT replaces the complete student.

```json
{
    "name": "Rahul",
    "age": 25,
    "email": "rahul@gmail.com",
    "address": "Bangalore"
}
```

All fields are required.

## PATCH

PATCH updates only selected fields.

```json
{
    "age": 25
}
```

Only the age changes.

### Simple way to remember

```text
PUT   → Replace everything
PATCH → Change only what I send
```

---

# Initial Student Data

The application starts with one student:

```python
student_data = {
    1: {
        "name": "yamuna",
        "age": 20,
        "email": "y@gmail.com",
        "address": "bangalore"
    }
}
```

The data is stored in a Python dictionary.

This means the application currently does not use a permanent database.

When the server restarts, newly created, updated, or deleted data will be lost.

---

# HTTP Status Codes

The API uses the following responses:

| Status Code | Meaning                   |
| ----------- | ------------------------- |
| `200`       | Request successful        |
| `404`       | Student not found         |
| `422`       | Request validation failed |

For example:

```text
GET /students/999
```

when student `999` does not exist returns:

```text
404 Not Found
```

An invalid request such as:

```json
{
    "age": 150
}
```

returns a validation error:

```text
422 Unprocessable Entity
```

---

# Important FastAPI Concepts

## Request Body

Pydantic models define the structure of incoming JSON data.

Example:

```python
@app.post("/students")
def create_student(student: StudentCreate):
    ...
```

FastAPI automatically reads and validates the request body.

---

## Path Parameter

The student ID is received from the URL:

```python
@app.get("/students/{id}")
def get_student(id: int):
    ...
```

For:

```text
/students/5
```

FastAPI converts:

```text
5
```

to an integer because the parameter is declared as:

```python
id: int
```

---

## Pydantic Validation

Pydantic automatically validates:

```python
Field(...)
```

constraints and:

```python
EmailStr
```

email format.

Custom business rules are implemented using:

```python
@field_validator
```

---

# Testing

The API can be tested using:

* Swagger UI
* Postman
* Thunder Client
* curl

The easiest method is Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Limitations

This project is designed for learning and currently has some limitations:

* Data is stored in memory.
* There is no database.
* Data disappears when the application restarts.
* There is no authentication.
* There is no authorization.
* There is no pagination.
* There is no search or filtering.
* `StudentCreate` and `StudentUpdate` contain some duplicated validation logic.
* There are no automated tests.
* There are no response models.
---

# Learning Outcomes

After completing this project, you should understand:

1. How to create a FastAPI application.
2. How REST API endpoints work.
3. How to create Pydantic models.
4. How request-body validation works.
5. How `Field()` constraints work.
6. How `EmailStr` validates emails.
7. How custom `field_validator` functions work.
8. How path parameters work.
9. How CRUD operations are implemented.
10. The difference between PUT and PATCH.
11. Why PATCH requires optional fields.
12. How `model_dump(exclude_unset=True)` supports partial updates.
13. How FastAPI automatically generates Swagger documentation.
14. The limitations of using an in-memory dictionary instead of a database.
