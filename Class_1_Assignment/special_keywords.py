# special keywords in python
 #bool 
False
x = False                                 
True
is_giaic = True

#None                         
None
result = None

#logical keywords                                   
and 
if a > 0 and b > 0:                       
 or  
if name == "Ali" or name == "Ahmed":
not 
if not is_logged_in:
    
#conditional keywords                         
 if       
 if age > 18: print("Adult")
                
elif     
elif age == 18: print("Just turned adult")
 
else     
else: print("Minor")

#Loop                      
 for`       
 for i in range(5): print(i)`               
 while`    
 while x < 5: x += 1                      
 break    
 if x == 3:
break                       
continue`  
 if x == 2:
continue`                        
pass   
 def func(): pass
 
 #functions                           
 def`       `
 def greet(): print("Hello")              
 return
return name.upper()  

#oop                     
class
class Person: pass   

#for error handling                      
 try     
try: x = 5/0`                               
except   
except ZeroDivisionError: print("Error")`   
finally`   
finally: 
print("Done")             
raise  
raise ValueError("Invalid input")`

#modules          
import
import math                            
from    
from math import pi                      
as`       
import math as m                      
global 
global count                             
 nonlocal`  
 `nonlocal x` (used in nested functions)       `lambda`    `square = lambda x: x * x`                   |
 with`      
 with open('file.txt') as f:`                
 assert`    
assert x > 0, "x must be positive"`         
del`       
del my_list[0]`                             
 yield
 yield x` (used in generators)               
 in`        
 if 3 in [1,2,3]:                        
 is
 if a is b:                              
