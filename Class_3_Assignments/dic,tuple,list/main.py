# dictionary in python
# dictionaries are use to store data value key:value pairs
# they are unorder mutable and dont not allow duplicate keys

dict = {
    "name":"Sherkhan",
    "age": 24,
    "Subjects":["python","nextjs","javascript"],
    "portal":("password","number",404534),
    "is_giaic":True
}
dict.update({"city":"karachi"})
print(dict)


#lists 
#list is mutible string is immutable

marks = [50,89,77,85,78,96,100]
print(marks)
print(marks[0])
print(marks[2])

marks[0] =55
print(marks)
print(marks[-5:-2])

list =[5,2,3,1,4]
list.append(6)
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)
list.insert(1,7)
print(list)

list =[5,1,2,3,1,4]
list.remove(1) #remove first word who 1 in the list
print(list)

list.pop(4,1)
print(list)

# #Tuples in python
# #a built data type that lets us create immutable sequences of value

tup = (1,3,5,3,1,6,7)
print(type(tup))

tup.pop(2) # this will give an error because tuple is immutable
print(tup[2])
print(tup.index(3))

print(tup.count(3))