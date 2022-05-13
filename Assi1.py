'''
Ass.No = 1
Ass.Name =  Write a programme to calculate salary of an employ given his basic pay take as input from user calculate gross salary of employee. let hra 10% of basic pay and ta be 5% of basic pay. let employ pay proffessional tax as 2% at total salary. calculate net salary payble after deductions.
Name = Maniyar Rimsha Jamir 
Rollno. = 03
Batch = MA1
Branch = Mechanical branch
Date = 20/04/2022
'''

basic_sal=int(input("enter basic pay:"))
hra=basic_sal*0.1
ta=basic_sal*0.05
total_sal=basic_sal+hra+ta
tax=total_sal*0.02
salary=total_sal-tax
print("salary of emp : " ,salary)
'''

Output = 
c-24@cc24-OptiPlex-3010:~$ python3 Assi1.py
enter basic pay:12000
salary of emp :  13524.0
'''

