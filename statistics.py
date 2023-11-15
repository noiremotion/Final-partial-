#https://replit.com/@Nery-EduardoEdu/Zoo-Statistics?s=app
zooCounter=str(input("Is there another animal to register?: "))
range1=0
range2=0
range3=0
range4=0
while zooCounter=="Yes" or zooCounter=="y":
  age=int(input("What is the age of the animal to register?: "))
  if age<2:
    range1+=1
  elif age>2 and age<5:
    range2+=1
  elif age>5 and age<10:
    range3+=1
  elif age>=10:
    range4+=1
  zooCounter=str(input("Is there another animal to register?: "))
totalAges=range1+range2+range3+range4
orange1=(range1*100)/totalAges
orange2=(range2*100)/totalAges
orange3=(range3*100)/totalAges
orange4=(range4*100)/totalAges
print("The total animals you registered is: ",totalAges)

print("The  total animals in range 1 is: ",range1)
print("This is equivalent to the ",orange1,"percent")

print("The  total animals in range 2 is: ",range2)
print("This is equivalent to the ",orange2,"percent")

print("The  total animals in range 3 is: ",range3)
print("This is equivalent to the ",orange3,"percent")

print("The  total animals in range 4 is: ",range4)
print("This is equivalent to the ",orange4,"percent")
