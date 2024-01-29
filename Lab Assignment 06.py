# Lab 06 Question No:1
l1 = []
for i in range(1,1001,2):
    l1.append(i)
print(l1)
sum = 0
for i in l1:
    sum = sum + i
print(sum) 

# Lab 06 Question No:2
import random
l1 = []
for i in range(1,21):
    numbers = random.randint(1,21)
    l1.append(numbers)
print(l1)
print(max(l1))
print(min(l1))

# Lab 06 Question No:3
l1 =[]
for i in range(5):
    num = int(input("Enter number"))
    l1.append(num)
print(l1)
sum = 0
for i in l1:
    if i % 2==0:
        sum = sum + i
print("Sum of Even number is:",sum)        

# Lab 06 Question No:4
tuple = ("pakistan","iran","afganistan","canada","german")
for i in tuple:
    if len(i) > 7:
        print(i)

# Lab 06 Question No:5
l1 =[]
for i in range(50):
    l1.append(i)
print(l1)
for a in l1:
    if a % 2==0:
        print(a**2)
    elif a % 2!=0:
        print(a**3)
    else:
        print("check the number")

# Lan 06 Question No:6
set1 = set(input("Enter items of set1").split())
set2 = set(input("Enter items of set2").split())

union_set = set1.union(set2)
print("Union of both Set is:",union_set)

# Lab 06 Question No:7
def list_to_string(list_of_characters):
    
    return ''.join(list_of_chracters)
list_of_chracters = 'p','a','k','i','s','t','a','n'
string = list_to_string(list_of_chracters)
print(string)

# Lab 06 Question No:8
import random
def random_map(list1,list2):
    if not list1 or not list2:
        return None
    
    list1 = random.choice(list1)
    list2 = random.choice(list2)
    return {list1:list2}

list1 = ["apple","banana","orange"]
list2 = [10,100,1000,10000]
result = random_map(list1,list2)
print(result)

# Lab 06 Question No:9
def get_student_grade(student_grades):
    student = input("Enter student name:")
    if student in student_grades:
        grade = student_grades[student]
        print("Grade for:",student,grade)
    else:
        print("Student is not Found")

student_grades = {
    "arslan":"Grade A",
    "hira":"Grade B",
    "fiza":"Grade C",
    "rayan":"Grade D"
}
get_student_grade(student_grades)

