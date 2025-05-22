#Data type in python

#1. Numeric
num: int = 42
print(type(num))
print(" int num = ",num)

# Floating (float)
num_f: float = 3.14

print(type(num_f))
print(" float num = ", num_f)

#complex
z = 3 + 4j

print("Real Part:", z.real) 
print("Imaginary Part:", z.imag)  

#Boolean
is_giaic_student: bool = True #False

print(type(is_giaic_student))
print(is_giaic_student)

#Sequence Types
#there are three types
#1.string
text: str  = "Hello, Python!"
print(text)

#2.list
list_1: int = [1, 2,  "math", 3.14, True] 
print(type(list_1)) 
print(list_1)

#3.tuple immutable
tup: tuple = (1, 2, 3, "AI", 2.71, False, .3  )
print(type(tup))
print("tuple = ", tup )

# Dictionary
dic:dict = {
    "name": "Sherbaz",
    "rool": 404534,
    "is_giaic_student":True
}

print(dic)