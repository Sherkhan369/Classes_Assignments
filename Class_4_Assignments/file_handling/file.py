#File Handling in Python
#File handling is essential for reading and writing data to files, enabling persistent storage. Python provides built-in functions and methods to handle files efficiently. This tutorial covers the fundamentals with examples.

file = open("file.txt", "w")
file.write("Hello, world!\n") 
file.write("This is another line.\n")
file.close()



file = open("file.txt", "r")
file.seek(0)  
content = file.read()
print(content)


with open("file.txt", "r") as file:
    
    content = file.read()
    print(content)
    
    
    
    
  
with open("file.txt", "r") as file:
  print(file.tell())  


  while True:
    content = file.read(10)
    if not content:
      print("End of file")
      break
    print(content)
    i+=1


    
  print(file.tell()) 