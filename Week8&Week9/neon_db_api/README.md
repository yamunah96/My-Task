````markdown
# Student Course Enrollment API

A REST API built with FastAPI for managing students, courses, and course enrollments using PostgreSQL hosted on Neon.

## Project Overview

This project demonstrates how to build a database-driven REST API using FastAPI and PostgreSQL.

The API manages three main entities:

- Students
- Courses
- Enrollments

The application uses SQLAlchemy for database connectivity and Pydantic for request validation.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Neon PostgreSQL
- SQLAlchemy
- Pydantic
- python-dotenv
- psycopg

## Database Structure

### Students Table

Stores student information.

| Column | Description |
|---|---|
| id | Primary key |
| name | Student name |
| email | Unique student email |
| age | Student age |
| city | Student city |
| created_at | Record creation timestamp |

### Courses Table

Stores course information.

| Column | Description |
|---|---|
| id | Primary key |
| title | Course title |
| instructor | Course instructor |
| price | Course price |
| duration_hours | Course duration |
| created_at | Record creation timestamp |

### Enrollments Table

Connects students with courses.

| Column | Description |
|---|---|
| id | Primary key |
| student_id | Foreign key referencing students |
| course_id | Foreign key referencing courses |
| status | Enrollment status |
| enrolled_at | Enrollment timestamp |

The enrollment table prevents the same student from enrolling in the same course more than once.

## Database Relationships

```text
Students
   |
   | student_id
   |
   v
Enrollments
   ^
   |
   | course_id
   |
Courses
````

* One student can enroll in multiple courses.
* One course can have multiple students.
* Enrollments acts as the bridge between students and courses.

## API Endpoints

### Student APIs

| Method | Endpoint                 | Description                          |
| ------ | ------------------------ | ------------------------------------ |
| POST   | `/add_student/`          | Add a new student                    |
| GET    | `/students`              | Get all students                     |
| GET    | `/students/{student_id}` | Get a student by ID                  |
| PATCH  | `/students`              | Partially update student information |
| DELETE | `/students/{student_id}` | Delete a student                     |

### Course APIs

| Method | Endpoint                 | Description                         |
| ------ | ------------------------ | ----------------------------------- |
| POST   | `/add_course/`           | Add a new course                    |
| GET    | `/courses`               | Get all courses                     |
| GET    | `/courses/{course_name}` | Get a course by title               |
| PATCH  | `/courses`               | Partially update course information |
| DELETE | `/courses/{course_id}`   | Delete a course                     |

### Enrollment APIs

| Method | Endpoint                       | Description                |
| ------ | ------------------------------ | -------------------------- |
| POST   | `/add_enrollments/`            | Create a course enrollment |
| GET    | `/enrollments`                 | Get all enrollments        |
| PATCH  | `/enrollments`                 | Update enrollment status   |
| DELETE | `/enrollments/{enrollment_id}` | Delete an enrollment       |

## CRUD Operations

The API supports complete CRUD operations:

```text
Create
   POST

Read
   GET

Update
   PATCH

Delete
   DELETE
```

## Partial Updates

PATCH endpoints allow updating only the required fields.

For example, to update only a student's age:

```json
{
    "age": 25
}
```

The existing name, email, and city remain unchanged.

This is implemented using SQL `COALESCE()`:

```sql
UPDATE students
SET
    name = COALESCE(:name, name),
    email = COALESCE(:email, email),
    age = COALESCE(:age, age),
    city = COALESCE(:city, city)
WHERE id = :student_id
```

## Enrollment Validation

Before creating an enrollment, the API checks whether:

1. The student ID exists.
2. The course ID exists.

If either does not exist, the API returns a `404` error.

Example:

```json
{
    "detail": "student id 999 does not exist"
}
```

## Delete Operations

Students, courses, and enrollments can be deleted using their IDs.

### Delete Student

```text
DELETE /students/{student_id}
```

Example:

```text
DELETE /students/5
```

Deleting a student also deletes their related enrollments because the database uses `ON DELETE CASCADE`.

### Delete Course

```text
DELETE /courses/{course_id}
```

Example:

```text
DELETE /courses/3
```

Deleting a course also deletes its related enrollments.

### Delete Enrollment

```text
DELETE /enrollments/{enrollment_id}
```

Example:

```text
DELETE /enrollments/10
```

Deleting an enrollment does not delete the student or course.

## Database Constraints

The database uses:

* Primary keys
* Foreign keys
* Unique constraints
* NOT NULL constraints
* Default timestamps
* ON DELETE CASCADE

The enrollment table uses:

```sql
UNIQUE(student_id, course_id)
```

to prevent duplicate enrollments.

## Environment Setup

Create a `.env` file in the project directory:

```env
NEON_DATABASE_URL=your_neon_postgresql_connection_string
```

Do not commit `.env` to GitHub.

Add it to `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

## Installation

Install the required dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg python-dotenv pydantic[email]
```

## Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Example Requests

### Add Student

```json
{
    "name": "Rahul",
    "email": "rahul@example.com",
    "age": 20,
    "city": "Bangalore"
}
```

### Add Course

```json
{
    "title": "Python Programming",
    "instructor": "John",
    "price": 5000,
    "duration_hours": 40
}
```

### Create Enrollment

```json
{
    "student_id": 1,
    "course_id": 1
}
```

### Update Student

Only update the required field:

```json
{
    "age": 25
}
```

### Update Course

```json
{
    "price": 4500
}
```

### Update Enrollment Status

```json
{
    "student_id": 1,
    "course_id": 1,
    "status": "completed"
}
```

## Project Structure

```text
student-course-api/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

## Key Concepts Demonstrated

* REST API development
* FastAPI
* PostgreSQL database integration
* Neon cloud database
* SQLAlchemy database sessions
* Raw SQL using SQLAlchemy `text()`
* Pydantic data validation
* Primary and foreign keys
* Database relationships
* CRUD operations
* PATCH and partial updates
* SQL `COALESCE()`
* Database constraints
* Foreign key validation
* Cascade deletion
* Transaction handling
* `commit()` and `rollback()`
* HTTP exception handling

