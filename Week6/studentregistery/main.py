data_list = [
    "101,Yamuna,yamuna@example.com,9845087981,Python,Bangalore",
    "102,Ananya,ananya@example.com,9876543210,Machine Learning,Mumbai",
    "103,Rahul,rahul@example.com,9988776655,Data Science,Delhi",
    "104,Priya,priya@example.com,9123456789,Python,Chennai",
    "105,Arjun,arjun@example.com,9898989898,Deep Learning,Hyderabad",
    "106,Neha,neha@example.com,9765432109,Data Analytics,Pune",
    "107,Rohan,rohan@example.com,9345678901,Python,Kolkata",
    "108,Ishita,ishita@example.com,9654321098,Machine Learning,Jaipur",
    "109,Karan,karan@example.com,9789012345,Data Science,Ahmedabad",
    "110,Meera,meera@example.com,9567890123,Python,Bangalore"
]
# write student records
with open("student_data.txt","w") as file:
  for student in data_list:
    file.write(student+"\n")
  print("Student records created..")

# appending new students
student_id=input("Enter student ID: ")
name=input("Enter Name: ")
email=input("Enter email: ")
phone=input("Enter phone: ")
course=input("Enter course: ")
city=input("Enter city: ")


record=f"{student_id},{name},{email},{phone},{course},{city}"
with open("/content/student_data.txt","a") as file:
  file.write(record+"\n")
print("Student registered successfully")


# Read complete records.
with open("student_data.txt","r") as file:
  data=file.readlines()
  print(data)


# Read individual lines.
with open("student_data.txt","r") as file:
  data=file.readlines()
  for i in data:
    print(i)

# Count number of records.
with open("student_data.txt","r") as file:
  data=file.readlines()
  print(f"Total records is: {len(data)}")


# Copy data into another backup file.
with open("student_data.txt","r") as readfile:
  with open("students_backup.txt","w") as writefile:
    data=readfile.readlines()
    for i in data:
      writefile.write(i)
  print("Backup file created successfully")

# Create another file containing only names and courses.
with open("/content/student_data.txt","r") as readfile:
  with open("/content/name_course.txt","a") as appendfile:
    data= readfile.readlines()
    for record in data:
      student= record.strip().split(",")
      name=student[1]
      course=student[4]

      appendfile.write(f"{name},{course}\n")
  print("Names and courses file create successfully")
