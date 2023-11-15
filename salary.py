#https://replit.com/@Nery-EduardoEdu/Salary?s=app
seller_Cycle=str(input("Is there another seller to register?: "))
while seller_Cycle=="y" or seller_Cycle=="Yes":
  seller_Name=str(input("what is your name?: "))
  basesalary=int(input("What is your base salary?(rounded it please): "))
  total_sales=int(input("What were your sales these month?: "))
  if total_sales<3500:
    commisionP=7
    commision=(commisionP*total_sales)/100
    total_Salary=basesalary+commision
    print("Hi ",seller_Name)
    print("Your total salary is: ",total_Salary)
    print("****************")
    print("Here is your balance: ")
    print("Base salary: ",basesalary)
    print("Sales Commision: ",commision)
  elif total_sales>3500 and total_sales<7000:
    commisionP=10
    commision=(commisionP*total_sales)/100
    total_Salary=basesalary+commision
    print("Hi ",seller_Name)
    print("Your total salary is: ",total_Salary)
    print("****************")
    print("Here is your balance: ")
    print("Base salary: ",basesalary)
    print("Sales Commision: ",commision)
  elif total_sales>7000:
    commisionP=15
    commision=(commisionP*total_sales)/100
    total_Salary=basesalary+commision
    print("Hi ",seller_Name)
    print("Your total salary is: ",total_Salary)
    print("****************")
    print("Here is your balance: ")
    print("Base salary: ",basesalary)
    print("Sales Commision: ",commision)
  seller_Cycle=str(input("Is there another seller to register?: "))
