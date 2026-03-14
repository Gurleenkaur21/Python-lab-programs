#WAP to print Search Employee by ID

emps={123:"Gurleen",124:"Arman"}
id=int(input("Enter ID: "))
print(emps.get(id,"Not found"))