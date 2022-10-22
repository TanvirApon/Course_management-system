import os
import pickle



#add course function for adding course where used pickle module for adding data into dictionary and retrive it 
def add_course():
       file=open("Course.dat","rb")
       file_path='Course.dat'       
       if os.stat(file_path).st_size == 0:
         file=open("Course.dat","wb")
         x=(input("Enter the id of the course: "))

         y=str(input("Enter the name of the course: "))

         z =str(input("Enter the pre-requsite of the course: "))

         #created a dictionary and added data 
         course={"CourseId": x,"CourseName":y,"Pre-requisite":z}

         #adding data into dictionry using pickle module
         pickle.dump(course,file)   
         #file.write("'Course Id': "+x+",\r\n")
         #file.write("'Course name': "+y+",\r\n")
         #file.write("'Course Pre-requsite': "+z+",\r\n\r\n\r\n")
         file.close()
         print("Data Stored ")
       
        
       else:
         file=open("Course.dat","ab")
         x=str(input("Enter the id of the course: "))

         y=str(input("Enter the name of the course: "))

         z =str(input("Enter the pre-requsite of the course: "))

         #created a dictionary and added data
         course={"CourseId": x,"CourseName":y,"Pre-requisite":z}

         #dic = {course}
         #file.write(str(dic))


         #adding data into dictionry using pickle module
         pickle.dump(course,file)
         
         
         #file.write("'Course Id': "+x+",\r\n")
         #file.write("'Course name': "+y+",\r\n")
         #file.write("'Course Pre-requsite': "+z+",\r\n\r\n\r\n")
         file.close()
         print("Data Stored ")
       

# print all the course into the file system     
def course_print():
  #reading a binary file u
  file = open("Course.dat","rb")
  
  while True:
   try:
    #fetching data from file using pickle module
    course=pickle.load(file)
    print("CourseID: ",course["CourseId"])
    print("CourseName: ",course["CourseName"])
    print("Pre-requsite: ",course["Pre-requisite"])

   except EOFError:
    print("No record found !!!")
    break
  file.close()   

  #course = json.loads(file_content)

  #print(type(file_content))
  #print(type(course))
  #print("CourseId:",file_content.get('CourseID'))
  #print("CourseName:",file_content['CourseName'])
  #print("Pre-requisite:",file_content['Pre-requisite'])




# Search the course details by course id
def course_search():
  x=str(input("Please Enter the course id for search: "))
  
  #reading a file 
  file=open("Course.dat",'rb')
  
  while True:
    try:
     
     #fetching data from a file 
     course=pickle.load(file)
     if course["CourseId"] == x:
      print("ID found !!!!")
      print("CourseID: ",course["CourseId"])
      print("CourseName: ",course["CourseName"])
      print("Pre-requsite: ",course["Pre-requisite"])
    except EOFError:
      print("No record Found !!! Please input a valid id")
      break


#Update function for course update
def update_course():
  x=str(input("Please Enter the course id for update: "))
  y=str(input("Please Enter the course Name for update: "))
  z=str(input("Please Enter the course pre-requisite for update: "))
  file=open("Course.dat",'rb')
  #initializing a list
  cour=[]
  while True:
     try:
      course=pickle.load(file)
      cour.append(course)  
     except EOFError:
      break
  file.close()

  for i in range(len(cour)):
    if cour[i]["CourseId"]==x:
       cour[i]["CourseName"]==y 
       cour[i]["Pre-requisite"]==z

  f= open("Course.dat","wb")
  for x in cour:
    pickle.dump(x,f)
  print("Updates sucessfull")
  file.close()        


#Delete function for delete a course by their id
def delete_course():
 
  x=str(input("Please Enter the course id for search: "))  
  file=open("Course.dat",'rb')
  cour=[]
  while True:
     try:
      course=pickle.load(file)
      cour.append(course)  
     except EOFError:
      break
  file.close()

  file=open("Course.dat","wb")
  for i in range(len(cour)):
    if cour[i]["CourseId"]==x:
     pickle.dump(x,file)
  print("Delete sucessfull")
  file.close()        

#Option function where we can see the option 
def option():

 while True:

  print("================================")           
  print("1.Create a new course \n")
  print("2.Update the course\n")
  print("3.Delete the course\n") 
  print("4.Search the course\n")
  print("5.Print all Course\n")
  print("6.Exit\n")
  print("==================================")

  choice=int(input("Enter the action you want: ")) 

  if choice == 1 :
       add_course()

  elif choice == 2 :
      update_course()

  elif choice == 3 :
      delete_course()

  elif choice == 4:
    course_search()

  elif choice == 5:
    course_print()

  
  elif choice == 6 :
       exit() 

  else:
    print("PLease input a legal action as described above")

#Main Function
if __name__ == "__main__":
   option()









       

