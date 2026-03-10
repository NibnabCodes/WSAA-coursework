from studentDAOLab6 import studentDAO 
 
student = {
  "name":"Fleur", 
  "age":50
  }

#create
student = studentDAO.create(student)
studentid = student["id"]

# find by id
result = studentDAO.findByID(studentid);
print ("test create and find by id")
print (result)


#update
newstudentvalues= {"name":"Phoenix", "age":5}
studentDAO.update(studentid,newstudentvalues)
result = studentDAO.findByID(studentid);
print("test update")
print (result)

# get all 
print("test get all")
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)
  
# delete
studentDAO.delete(studentid)