n=int(input("Enter the No of employees: "))
employee={}
for i in range(n):
    name=input("Enter the Name of employee: ")
    salary=int(input("Enter the salary of employee: "))
    employee[name]=salary
    #print(employee)
while True:
    name=input("Enter the Name of employee: ")
    salary=employee.get(name, -1)
    if salary == -1:
        print("Employee does not exist: ")
    else:
        print(f"Employee {name} have a salary of : {salary} per annum " )
        Choice=input("Do you want to know the salary of the employee: [YES|NO] : ")
    if Choice=="NO" :
        break
