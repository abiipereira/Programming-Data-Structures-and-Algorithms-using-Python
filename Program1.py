'''
   The academic office at the Hogwarts School of Witchcraft and Wizardry has compiled data about students' grades.
   The data is provided as text from standard input in three parts: information about courses, information about students and information about grades. 
   Each part has a specific line format, described below..

   Information about courses
   Line format: Course Code~Course Name~Semester~Year~Instructor
   Information about students
   Line format: Roll Number~Full Name
   Information about grades
   Line format: Course Code~Semester~Year~Roll Number~Grade
   The possible grades are A, AB, B, BC, C, CD, D with corresponding grade points 10, 9, 8, 7, 6, 5 and 4. 
   The grade point average of a student is the sum of his/her grade points divided by the number of courses.
   For instance, if a student has taken two courses with grades A and C, the grade point average is 8 = (10+6)÷2. 
   If a student has not completed any courses, the grade point average is defined to be 0.

   You may assume that the data is internally consistent. For every grade, there is a corresponding course code and roll number in the input data.
   Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Courses. 
   The second section begins with a line containing Students. The third section begins with a line containing Grades. The end of the input is marked by a line containing EndOfInput.

   Write a Python program to read the data as described above and print out a line listing the grade point average for each student in the following format:

   Roll Number~Full Name~Grade Point Average
   Your output should be sorted by Roll Number. 
   The grade point average should be rounded off to 2 digits after the decimal point. Use the built-in function round().

'''
flag=1

x=input()
while True:
 if flag!=0:
  a=input()
  a.split('~')
 y=input()
 if y=='Students':
  break
 else:
  y.split('~')
  flag=0

flag=1
uroll_no=[]
name=[]
while True:
 if flag!=0:
  x=input()
  l=x.split('~')
  uroll_no.append(l[0])
  
  
  name.append(l[1])
 y=input()
 if y=='Grades':
  break
 else:
  flag=0
  p=y.split('~')
  uroll_no.append(p[0])
  name.append(p[1])

sums=[]
avg=[]
num=[]
roll_no=[]
snames=[]
for i in range(len(uroll_no)):
  sums.append(0)
  avg.append(0)  
  num.append(0)
  roll_no.append(0)
  snames.append(0)
roll_no=sorted(uroll_no)
for i in range(len(uroll_no)):
  for j in range(len(uroll_no)):
    if uroll_no[i]==roll_no[j]:
      snames[j]=name[i]    
flag=1
while True:
 if flag!=0:
  
  x=input()
  
  q=x.split('~')
  grade=q[4]
  
  
  if grade=='A':
   marks=10
  elif grade=='AB':
   marks=9
   
  elif grade=='B':
   marks=8
   
  elif grade=='BC':
   marks=7
   
  elif grade=='C':
   marks=6
   
  elif grade=='CD':
   marks=5
   
  elif grade=='D':
   marks=4
  i=0 
  while i <(len(roll_no)):
   if q[3]==roll_no[i]:
     sums[i]=sums[i]+marks
     num[i]=num[i]+1
     break
   else:
    i=i+1
   
     
 h=input()
 
 if h=='EndOfInput':
  flag=0  
  break
 else:
  
  
  
  
  flag=0
  
  q=h.split('~')
  
  grade=q[4]
  
  if grade=='A':
   marks=10
  elif grade=='AB':
   marks=9
   
  elif grade=='B':
   marks=8
   
  elif grade=='BC':
   marks=7
   
  elif grade=='C':
   marks=6
   
  elif grade=='CD':
   marks=5
   
  elif grade=='D':
   marks=4
  i=0
  while i <(len(roll_no)):
   
   if q[3]==roll_no[i]:
     sums[i]=sums[i]+marks
     num[i]=num[i]+1
     break
   else:
     i=i+1
  


for i in range(len(uroll_no)):
  if num[i]!=0:
   avg[i]=round((sums[i]/num[i]),2)
  else:
   avg[i]=0
  

for i in range (len(uroll_no)):
 print(roll_no[i],'~',snames[i],'~',avg[i],sep="")  
 

