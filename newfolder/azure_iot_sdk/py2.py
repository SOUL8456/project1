class Employee:
    def __init__(self,e,en,desig,sal):
        self.empno=e
        self.empname=en
        self.designation=desig
        self.salary=sal
def main():
    emp1=Employee(1,"Meraj","Associate_Trainee",10000)
    emp2=Employee(2,"Uttam","Associate_Trainee",15000)
    emp3=Employee(3,"Sarthak","Associate_Trainee",20000)
    emp4=Employee(4,"Shivashreet","Senior Developer",60000)
    emp5=Employee(5,"Tushar","Hardware_Engineer",50000)
    emp6=(Employee(6,"Soubhagya","Associate_Trainee",25000))

    print(emp1.empno, emp1.empname, emp1.designation, emp1.salary)
    print(emp2.empno, emp2.empname, emp2.designation, emp2.salary)
    print(emp3.empno, emp3.empname, emp3.designation, emp3.salary)
    print(emp4.empno, emp4.empname, emp4.designation, emp4.salary)
    print(emp5.empno, emp5.empname, emp5.designation, emp5.salary)
    print(emp6.empno, emp6.empname, emp6.designation, emp6.salary)


main()


