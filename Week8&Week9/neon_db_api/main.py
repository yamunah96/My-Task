import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from fastapi import FastAPI,HTTPException
from pydantic import Field,EmailStr,BaseModel


load_dotenv()
neondb_url=os.getenv("NEON_DATABASE_URL")
print(neondb_url)
if not neondb_url:
    raise "Database URL Not found"

engine= create_engine(neondb_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create student table in neon database i have used below sql code
'''
  CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    age INTEGER,
    city VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''


# create a course table in neon database i have used the below sql code
'''
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    instructor VARCHAR(100),
    price NUMERIC(10,2),
    duration_hours INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''



# create a enrollment table in neon database i have used the below sql code
'''
    CREATE TABLE enrollments (
        id SERIAL PRIMARY KEY,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        status VARCHAR(30) DEFAULT 'active',
        enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        CONSTRAINT fk_student
            FOREIGN KEY (student_id)
            REFERENCES students(id)
            ON DELETE CASCADE,

        CONSTRAINT fk_course
            FOREIGN KEY (course_id)
            REFERENCES courses(id)
            ON DELETE CASCADE,

        CONSTRAINT unique_enrollment
            UNIQUE(student_id, course_id)
    );
'''

app= FastAPI()
# create student api
class Student(BaseModel):
    name:str
    email:EmailStr
    age:int|None=Field(description="enter student age",gt=18)
    city:str=Field(description="enter student city")

@app.post("/add_student/")
def add_student(student:Student):
    session=SessionLocal()
    try:
        query=text("INSERT INTO students (name,email,age,city) VALUES (:name,:email,:age,:city)")
        session.execute(query,{"name":student.name,"email":student.email,"age":student.age,"city":student.city})
        session.commit()
        return {"message":f"student {student.name} name is added successfully to database","student":student}
    except Exception as e:
        session.rollback()
        return {
            "error": str(e)
        }
    finally:
        session.close()

# # create add course api
class Course(BaseModel):
    title:str
    instructor:str
    price:int
    duration_hours:int

@app.post("/add_course/")
def add_course(course:Course):
    session=SessionLocal()
    try:
        query=text("""INSERT INTO courses 
        (title,instructor,price,duration_hours) VALUES (:title,:instructor,:price,:duration_hours)""")

        session.execute(query,{"title":course.title,"instructor":course.instructor,"price":course.price,"duration_hours":course.duration_hours})
        session.commit()
        return {"message":f"{course.title} course added successfully to database","course":course}
    except Exception as e:
        session.rollback()
        return {
            "error": str(e)
        }
    finally:
        session.close()

# create add enrollments api 
class Enrollment(BaseModel):
    student_id: int
    course_id: int

@app.post("/add_enrollments/")
def add_enrollment(enrollment:Enrollment):
    session=SessionLocal()
    try:
        # checking student exists
        student_query= text("""
        SELECT id FROM students WHERE id= :student_id
        """)
        student= session.execute(student_query,{"student_id": enrollment.student_id}).fetchone()
        if not student:
            raise HTTPException(status_code=404,detail=f"student id {enrollment.student_id} does not exist")

         # checking course exists
        course_query= text("""
        SELECT id FROM courses WHERE id= :course_id
        """)
        course= session.execute(course_query,{"course_id": enrollment.course_id}).fetchone()
        if not course:
            raise HTTPException(status_code=404,detail=f"course id {enrollment.course_id} does not exist")

        # create enrollment
        query= text("""INSERT INTO enrollments (student_id,course_id) 
        VALUES(:student_id,:course_id) RETURNING id, student_id, course_id, status, enrolled_at""")
        result =session.execute(query,{"student_id":enrollment.student_id,"course_id":enrollment.course_id})
        new_enrollment=result.fetchone()
        session.commit()
        return {
            "message": "Enrollment created successfully",
            "enrollment": dict(new_enrollment._mapping)
        }
    except HTTPException:
        raise

    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()



# get all student records 
@app.get("/students")
def get_students():
    session=SessionLocal()
    try:
        query= text(""" SELECT * FROM students """)
        result =session.execute(query)
        students=result.fetchall()
        student_list=[]
        if not students:
            raise HTTPException(
                status_code=404,
                detail="Students not found"
            )

        for student_data in students:
            student_list.append({
            "student_id":  student_data.id,
            "name":  student_data.name,
            "email": student_data.email,
            "age":student_data.age,
            "city": student_data.city
            })
        return {
            "message": "Student information",
            "students": student_list
        }
    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()


# get student based on id 
@app.get("/students/{student_id}")
def get_student(student_id:int):
    session=SessionLocal()
    try:
        query= text("SELECT * FROM students WHERE id = :id")
        result= session.execute(query,{"id":student_id})
        student = result.fetchone()
        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )
        return {
            "message": "student info",
            "student": dict(student._mapping)
        }
    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()


# get  all course 
@app.get("/courses")
def get_courses():
    session=SessionLocal()
    try:
        query= text(""" SELECT * FROM courses""")
        result =session.execute(query)
        courses=result.fetchall()
        course_list=[]
        if not courses:
            raise HTTPException(
                status_code=404,
                detail="course not found"
            )
        for course in courses:
            course_list.append({
            "course_id":  course.id,
            "course_name":  course.title,
            "instructor": course.instructor,
            "price":"₹"  + str(course.price),
            "duration": str(course.duration_hours)+ " hrs"
            })
        return {
            "message": "Course information",
            "courses": course_list
        }
    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()

# get course based on the course name
@app.get("/courses/{course_name}")
def get_course(course_name:str):
    session=SessionLocal()
    try:
        query= text("SELECT * FROM courses WHERE title = :title")
        result= session.execute(query,{"title":course_name})
        course= result.fetchone()
        if not course:
            raise HTTPException(
                status_code=404,
                detail="Course not found"
            )
        return {
            "message": "course info",
            "course": dict(course._mapping)
        }
    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()

# get all enrollements
@app.get("/enrollments")
def get_enrollments():
    session=SessionLocal()
    try:
        query= text("""SELECT *from enrollments """)
        ''' we can also fetch student name and course name
           SELECT
                e.id AS enrollment_id,
                s.id AS student_id,
                s.name AS student_name,
                c.id AS course_id,
                c.title AS course_name,
                e.status,
                e.enrolled_at
            FROM enrollments e
            JOIN students s
                ON e.student_id = s.id
            JOIN courses c
                ON e.course_id = c.id

        '''
        result =session.execute(query)
        enrollments=result.fetchall()
        enrollments_list=[]
        if not enrollments:
            raise HTTPException(
                status_code=404,
                detail="No enrollments found"
            )
        for enrollment in enrollments:
            enrollments_list.append({
                "enrollment_id":enrollment.id,
                "student_id":enrollment.student_id,
                "course_id":enrollment.course_id,
                "status":enrollment.status,
                "enrolled_at":enrollment.enrolled_at
                
            })
        return {
            "message": "Course information",
            "enrolled": enrollments_list
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()

# updating student records
class StudentUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = Field(default=None, description="enter student age", ge=18)
    city: str | None = None

@app.patch("/students")
def update_students(student:StudentUpdate,student_id:int|None=None,name:str|None=None):
    session=SessionLocal()
    try:
        if student_id is None and name is None:
            raise HTTPException(
                status_code=400,
                detail="Please prvide either student_id or name"
            )
        if student_id is not None and name is not None:
            raise HTTPException(
                status_code=400,
                detail="Please provide either student_id or name,not both"
            )

        if student_id is not None:
            query =text(
               """SELECT id,name,email,age,city FROM students
                    WHERE id= :student_id
               """
            )
            result= session.execute(
                query,{"student_id":student_id}
            )
        else:
            query =text(
            """SELECT id,name,email,age,city FROM students
                WHERE name= :name
            """
            )
            result= session.execute(
                query,{"name":name}
            )

        students=result.fetchall()
        if not students:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        # multiple students habe same name
        if len(students)>1:
            raise HTTPException(
                status_code=400,
                detail="multiple students found with this name,Please use student_id"
            )
        existing_student=students[0]

        # update the student
        update_query=text("""
            UPDATE students
            SET
               name = COALESCE(:name, name),
                email = COALESCE(:email, email),
                age = COALESCE(:age, age),
                city = COALESCE(:city, city)
              WHERE id=:student_id
              RETURNING id,name,email,age,city
        """)
        result= session.execute(
            update_query,{
                "student_id": existing_student.id,
                "name": student.name,
                "email": student.email,
                "age": student.age,
                "city": student.city
            }
        )
        updated_student= result.fetchone()

        session.commit()
        return{
            "message": "Student updated successfully",
            "student": dict(updated_student._mapping)
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()

# updating course records
class CourseUpdate(BaseModel):
    title: str | None = None
    instructor: str | None = None
    price: float | None = None
    duration_hours: int | None = Field(default=None, gt=0)

@app.put("/courses")
def update_course(course: CourseUpdate,course_id: int | None = None,title: str | None = None):
    session = SessionLocal()
    try:
        # User must provide ID OR title
        if course_id is None and title is None:
            raise HTTPException(
                status_code=400,
                detail="Please provide either course_id or title"
            )

        # Don't allow both
        if course_id is not None and title is not None:
            raise HTTPException(
                status_code=400,
                detail="Please provide either course_id or title, not both"
            )

        # Find course by ID
        if course_id is not None:
            query = text("""
                SELECT id, title,instructor,price,duration_hours
                FROM courses
                WHERE id = :course_id
            """)

            result = session.execute(
                query,
                {"course_id": course_id}
            )

        # Find course by title
        else:

            query = text("""
                SELECT id, title,instructor,price,duration_hours
                FROM courses
                WHERE title = :title
            """)

            result = session.execute(
                query,
                {"title": title}
            )

        courses = result.fetchall()

        # Course not found
        if not courses:
            raise HTTPException(
                status_code=404,
                detail="Course not found"
            )

        # Duplicate course titles
        if len(courses) > 1:
            raise HTTPException(
                status_code=400,
                detail="Multiple courses found with this title. Please use course_id."
            )

        existing_course = courses[0]

        # Update course
        update_query = text("""
            UPDATE courses
            SET
                title = COALESCE(:title, title),
                instructor = COALESCE(:instructor, instructor),
                duration_hours = COALESCE(:duration_hours, duration_hours),
                price = COALESCE(:price, price)
            WHERE id = :course_id
            RETURNING id, title,instructor,price,duration_hours
        """)

        result = session.execute(
            update_query,
            {
                "course_id": existing_course.id,
                "title": course.title,
                "instructor": course.instructor,
                "duration_hours": course.duration_hours,
                "price":course.price
            }
        )

        updated_course = result.fetchone()

        session.commit()

        return {
            "message": "Course updated successfully",
            "course": dict(updated_course._mapping)
        }

    except HTTPException:
        raise

    except Exception as e:
        session.rollback()

        return {
            "error": str(e)
        }

    finally:
        session.close()



# updating enrollment records student status based on the student id  and course id
class EnrollmentUpdate(BaseModel):
    student_id: int
    course_id: int
    status: str|None= None

@app.patch("/enrollments")
def update_enrollment(enrollment:EnrollmentUpdate):
    session= SessionLocal()
    try:
        query= text("""
            UPDATE enrollments 
            SET status= :status
            WHERE student_id= :student_id
            AND course_id= :course_id
            RETURNING
            id,
            student_id,
            course_id,
            status,
            enrolled_at
        """)
        result= session.execute(
            query,{
                "student_id":enrollment.student_id,
                "course_id":enrollment.course_id,
                "status":enrollment.status
            }
        )
        updated_enrollment=result.fetchone()
        if not updated_enrollment:
            raise HTTPException(
                status_code=404,
                detail="Enrollment not found for this student and course"
            )
        session.commit()
        return{
            "message":"Enrollment status updated successfully",
            "enrollment": dict(updated_enrollment._mapping)
        }
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        return {
            "error":str(e)
        }
    finally:
        session.close()


# deleting records students,course and enrollments
# delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    session = SessionLocal()

    try:
        # Check student exists
        check_query = text("""
            SELECT id, name
            FROM students
            WHERE id = :student_id
        """)

        student = session.execute(
            check_query,
            {"student_id": student_id}
        ).fetchone()

        if not student:
            raise HTTPException(
                status_code=404,
                detail=f"Student ID {student_id} does not exist"
            )

        # Delete student
        delete_query = text("""
            DELETE FROM students
            WHERE id = :student_id
        """)

        session.execute(
            delete_query,
            {"student_id": student_id}
        )

        session.commit()

        return {
            "message": f"Student {student.name} deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:
        session.rollback()
        return {
            "error": str(e)
        }

    finally:
        session.close()

# Delete a Course
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    session = SessionLocal()

    try:
        # Check course exists
        check_query = text("""
            SELECT id, title
            FROM courses
            WHERE id = :course_id
        """)

        course = session.execute(
            check_query,
            {"course_id": course_id}
        ).fetchone()

        if not course:
            raise HTTPException(
                status_code=404,
                detail=f"Course ID {course_id} does not exist"
            )

        # Delete course
        delete_query = text("""
            DELETE FROM courses
            WHERE id = :course_id
        """)

        session.execute(
            delete_query,
            {"course_id": course_id}
        )

        session.commit()

        return {
            "message": f"Course '{course.title}' deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:
        session.rollback()
        return {
            "error": str(e)
        }

    finally:
        session.close()

# Delete an Enrollment For an enrollment, delete using its unique enrollment_id
@app.delete("/enrollments/{enrollment_id}")
def delete_enrollment(enrollment_id: int):
    session = SessionLocal()

    try:
        # Check enrollment exists
        check_query = text("""
            SELECT id
            FROM enrollments
            WHERE id = :enrollment_id
        """)

        enrollment = session.execute(
            check_query,
            {"enrollment_id": enrollment_id}
        ).fetchone()

        if not enrollment:
            raise HTTPException(
                status_code=404,
                detail=f"Enrollment ID {enrollment_id} does not exist"
            )

        # Delete enrollment
        delete_query = text("""
            DELETE FROM enrollments
            WHERE id = :enrollment_id
        """)

        session.execute(
            delete_query,
            {"enrollment_id": enrollment_id}
        )

        session.commit()

        return {
            "message": f"Enrollment {enrollment_id} deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:
        session.rollback()
        return {
            "error": str(e)
        }

    finally:
        session.close()