#wap using csv file handling to store emp details .
# the program should perform the following operations
# 1)add emp details into csv file
# 2) display all employees
# 3)Calculate total annual salary all emp
# 4)exit
# note: Each employee should record must contain ("ename","salary","job","dept.no.","annual salary")


import csv
while True:
    print("1-add emp details\n 2- display all employees\n 3-Calculate total annual salary all emp\nexit")
    service=int(input("enter the service serial no."))
    match service:
        case 1:
            with open("employee.csv","a") as file:
                writer=csv.writer(file)
                name=input("enter the employee name")
                salary=eval(input("enter your salary"))
                job=input("enter your resgination")
                annaul_salary=salary*12
                writer.writerow([name,salary,job,annaul_salary])
        case 2:
            with open("employee.csv","r") as file:
                reader=csv.reader(file)
                for i in reader:
                    print(i[0])

        case 3:
            sum=0
            with open("employee.csv","r") as file:
                reader=csv.reader(file)
                for i in reader:
                    sum+=i[4]
                print(f'total annual salary of employees is :{sum}')
        case 4:
            break
    