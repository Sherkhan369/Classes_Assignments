# ----Control flow

x: int = 10
y: int = 20

print("x == y = ", x == y)  
print("x != y = ", x != y)  
print("x > y  = ", x > y)   
print("x < y  = ", x < y)  
print("x >= y = ", x >= y)  
print("x <= y = ", x <= y) 

#--------Logical Operators--

age: int = 18
is_student: bool = True

if age >= 18 and is_student:
    print("You are eligible for a student discount.")

if age < 12 or age > 60:
    print("You qualify for a special discount.")

if not is_student:
    print("You are not a student.")
    
    #example 2
marks: int = int(input("Enter your marks"))

if marks >= 90:
    print("grade = A+")
elif marks >= 80:
    print("grade = A")
elif marks >= 70:
    print("grade = B")
elif marks >= 60:
    print("grade = C")
elif marks >= 50:
    print("grade = D")
else:
    print("grade = F")
    

