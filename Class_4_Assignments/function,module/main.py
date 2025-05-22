# # Module in python
# # Type of modules in python
# # 1 Built-in modules
# # 2 User-defined modules
# # 3 Third-party modules
# import math
# import requests as req

# num_sqrt = math.sqrt(16)
# print(num_sqrt)

# response =req.get("https://www.abc.xyz/api/profile")

# print(response.json())

# # 2 User-defined modules
# import modules as mod
# z = sum(2,3)
# print(z)

# name = mod.name("Asharib")
# print(name)


# # 3 Third-party modules
# # pip install pandas
# # pip install numpy
# # import numpy as np
# # import pandas as pd

# arr = np.array([1,2,3,4,5])
# print(arr)


# Positional-only arguments
# def position(a,b,/,c):
    
#   print("a=",a,"b=","c=",c)

#   return a,b,c

# z = position(10,20,c=5)
# print(z)

# Keyword-only arguments
# def keyword(*,num1,num2,num3):
    
#   print("sum all numbers = ",num1+num2+num3)
  
#   return num1,num2,num3
# sum =keyword(num1=5,num2=10,num3=15)
# print(sum)


# def multiple_args(a,*args,**kwargs):
    
#     print("a=",a)
#     print("args=",args)
#     print("kwargs=",kwargs)
    
#     return a,args,kwargs
#     mlt = multiple_args(10,20,30,40,50,60,70,80,90,100,name="Asharib",age=25)
#     print(mlt)
   
   
#    def my_function(a, *args, **kwargs):
       
#      print("Fixed argument:", a)
#      print("Positional (args):", args)
#      print("Keyword (kwargs):", kwargs)

# my_function(1, 2, 3, 4, name="Zara", age=22)


# add = lambda x,y: x+y
# print(add(5,10))

# students = [
#     ("Ali", 20),
#     ("Sara", 22),
#     ("Ahmed", 19),
#     ("Zara", 21),
#     ("Omar", 23)
# ]

# students.sort(key =lambda student:student[1])
# print(students)

# Generator Function

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
    
# gen = my_generator()
    
# for num in gen:
#     print(num,gen)
    
    
# def infinite_generator():
#     num <0
#     while True: 
#         yield num
#     num +=1
# gen = infinite_generator()
# for _ in range(10):
#         print(next(gen))

def recursive_function(n):
    if n == 1:
        return 1
    else:
        return n * recursive_function(n - 1)
    
result = recursive_function(5)
print(result)  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1) 
        
     
     
def countdown(n):
    
    if n==0:
        print("Countdown finished!")
    else:
        print(n)
        countdown(n-1)
        
countdown(5)  # Output: 5 4 3 2 1 Countdown finished!
            