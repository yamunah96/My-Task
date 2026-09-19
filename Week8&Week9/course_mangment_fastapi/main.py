from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import List,Literal,Annotated,Optional
class CourseCreate(BaseModel):
    title:Annotated[str,Field(min_length=3,title="Course name",description="Give the name of the course",examples=["python","sql"])]
    description:Annotated[str,Field(max_length=100,title="Course description",description="Give the course description",examples=["Python course for beginners, covers basics to advance"])]
    price:float=Field(gt=0,description="Course price must be greater than 0")
    duration:int=Field(gt=0,description="Course duration must be greater than 0")
    instructor:Annotated[str,Field(min_length=3,title="Instructor name",description="Give the instructor name")]
    category:Annotated[Optional[List[str]],Field(default=None,max_length=10)]
    rating:float=Field(gt=1,le=5,  description="Rating must be between 1 and 5",examples=[4.5, 3.5])
    active:Literal["true","false"]

app=FastAPI()
course_data={
   1: {
        "title": "Beginner Python",
        "description": "Python course for beginners, covers basics to advanced concepts",
        "price": 1999,
        "duration": 20,
        "instructor": "Yamuna",
        "category": [
            "Python",
            "Data Science",
            "Data Analytics",
            "AI",
            "ML"
        ],
        "rating": 4.5,
        "active":False
    },

    2: {
        "title": "SQL Beginner to Advanced",
        "description": "Master SQL with project based learning and real world queries",
        "price": 3999,
        "duration": 60,
        "instructor": "Sinchana",
        "category": [
            "SQL",
            "Data Analytics",
            "Database",
            "Data Science"
        ],
        "rating": 4.8,
        "active": True
    },

    3: {
        "title": "Machine Learning with Python",
        "description": "Learn machine learning algorithms and build practical projects",
        "price": 6999,
        "duration": 80,
        "instructor": "Rahul",
        "category": [
            "Python",
            "Machine Learning",
            "AI",
            "Data Science"
        ],
        "rating": 4.7,
        "active": True
    },

    4: {
        "title": "Power BI Data Analytics",
        "description": "Learn Power BI, data visualization and intertrue dashboards",
        "price": 2999,
        "duration": 35,
        "instructor": "Priya",
        "category": [
            "Power BI",
            "Data Analytics",
            "Visualization",
            "Business Intelligence"
        ],
        "rating": 4.6,
        "active": True
    },

    5: {
        "title": "Deep Learning Fundamentals",
        "description": "Learn neural networks, deep learning and computer vision basics",
        "price": 8499,
        "duration": 90,
        "instructor": "Arjun",
        "category": [
            "Deep Learning",
            "AI",
            "Machine Learning",
            "Python",
            "Computer Vision"
        ],
        "rating": 4.9,
        "active": False
    },
}

@app.post("/create_course/")
def create_course(course:CourseCreate):
    try:
        for existing_course in course_data.values():
            if existing_course["title"].lower() == course.title.lower():
                return {
                "message": "Course already exists",
                "course": existing_course
                }
        if course_data:
            truet_id= max(course_data.keys())+1
        else:
            truet_id=1
    
        course_dict = course.model_dump()
        course_dict["id"] =truet_id

        course_data[truet_id] = course_dict

        return{
            "message":f"{course.title} course created successfully",
            "course":course_dict
        }
    except Exception as e:
        print(e)

# get all course
@app.get("/get_courses")
def get_course():
    return {
        "message":"courses data fetched successfully",
        "courses":course_data
    }

# GET /courses?category=python
@app.get("/get_course/category")
def get_course_category(category:str):
    matching_course=[]
    for course_id,course in course_data.items():
        if category.lower() in [c.lower() for c in course["category"]]:
            matching_course.append(course)

    if matching_course:
        return {
            "message":f"courses found for category :{category}",
            "course":matching_course
        },200
    else:
        return{"message":f"{category} related courses not available"}


# GET /courses?min_price=500&max_price=5000
@app.get("/get_course/price")
def get_course_price(min_price:float,max_price:float):
    matching_course=[]
    for course_id,course in course_data.items():
        if min_price <= course["price"] <= max_price:
            matching_course.append(course)
    if matching_course:
        return {
            "message":f"courses found for btw {min_price}-{max_price}",
            "course":matching_course
        },200
    else:
        return{"message":f" This price ranged courses not available"}

# GET /courses?active=true
@app.get("/get_course/active")
def get_actuve_course(active:bool):
    matching_courses=[]
    if active==True:
        for course_id,course in course_data.items():
            if course["active"] == active:
                matching_courses.append(course)
    else:
        for course_id,course in course_data.items():
            if course["active"] == active:
                matching_courses.append(course)

    if matching_courses:
        return {
            "message":f"The active courses" if active else "The inactive courses",
            "course":matching_courses
        },200
    return {
        "message":f"No courses found",
    },200