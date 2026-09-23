from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr,field_validator
from typing import List,Optional,Annotated
# student mangement
class StudentCreate(BaseModel):
    # name,age,email,address
    name:Annotated[str, Field(min_length=1,max_length=100)]
    age:Annotated[int, Field(gt=0,lt=100)]
    email:EmailStr
    address:Annotated[str, Field(min_length=1,max_length=200)]

    # email validation is done by EmailStr type from pydantic yahoo,outlook,gmail
    @field_validator("email")
    @classmethod
    def validate_email(cls,value):
        valid_domains=["gmail.com","yahoo.com","outlook.com"]
        domain=value.split("@")[-1]
        if domain not in valid_domains:
            raise ValueError("Email domain must be one of: gmail.com, yahoo.com, outlook.com")
        return value
    
    @field_validator("name")
    @classmethod
    def validate_name(cls,value):
        if not value.isalpha():
            raise ValueError("Name must contain only alphabets")
        return value.lower()

# student data
student_data={
   1:{"name":"yamuna","age":20,"email":"y@gmail.com","address":"bangalore"}
}
app=FastAPI()

# POST /students — create student
@app.post("/students")
def create_student(student:StudentCreate):
    if student_data:
        id =max(student_data.keys())+1 
        student_data[id]=student
    else:
        id=1
        student_data[id]=student
    return {"message":"Student created successfully","student":student},200

# GET /students — list students
@app.get("/students")
def get_students():
    return {"message":"List of students","students":student_data},200

# GET /students/{id} — get student
@app.get("/students/{id}")
def get_student(id:int):
    if id in student_data:
        return {"message":"Student found","student":student_data[id]},200
    else:
        return {"message":"Student not found"},404
    
# PUT /students/{id} — replace student
@app.put("/students/{id}")
def update_student(id:int,student:StudentCreate):
    if id in student_data:
        student_data[id]=student
        return {"message":"Student updated successfully","student":student},200
    else:
        return {"message":"Student not found"},404


class StudentUpdate(BaseModel):
    name: Optional[Annotated[str, Field(min_length=1, max_length=100)]] = None
    age: Optional[Annotated[int, Field(gt=0, lt=100)]] = None
    email: Optional[EmailStr] = None
    address: Optional[Annotated[str, Field(min_length=1, max_length=200)]] = None

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

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError("Name must contain only alphabets")

        return value.lower()
    
# PATCH /students/{id} — partially update student
@app.patch("/students/{id}")
def partial_update_student(id:int, student_update: StudentUpdate):
    if id in student_data:
        update_data = student_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if key in student_data[id]:
                student_data[id][key] = value
        return {"message":"Student updated successfully","student":student_data[id]},200
    else:
        return {"message":"Student not found"},404


# DELETE /students/{id} — delete student
@app.delete("/students/{id}")
def delete_student(id:int):
    if id in student_data:
        del student_data[id]
        return {"message":"Student deleted successfully"},200
    else:
        return {"message":"Student not found"},404
