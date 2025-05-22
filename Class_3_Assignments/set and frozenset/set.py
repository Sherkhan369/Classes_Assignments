#The Set Data Type 
# A set is:

# unordered
# unindexed
# mutable

set_1: set = {12, 452, 5, 6}
set_2: set = set([123, 452, 5, 6])
empty_dic: set = {} 
empty_set: set = set()

print("set 1  = ", set_1)
print("type of set 1 = ", type(set_1))
print("set2   = ", set_2)
print("type of set 2 = ", type(set_2))
print("type of empty dic  = ", type(empty_dic))
print("empty dic = ", empty_dic)
print("empty set = ", empty_set)
print("type of empty set = ", type(empty_set))


# changing in set
my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print(my_set)
# Remove an item
my_set.remove(3)
my_set.remove('A')
print(my_set)  


#example 2
my_set = {10, 3, 5, 8}
print(my_set)  

my_set.add(20)
print(my_set)  


my_set.remove(10)
print(my_set)  


#set methods

set_1:  set = {1,2,3, "Hello! World", 4,5,6}
set_2: set = {1,2,3, "Hello! World", 8,9}
set_3: set = {1,2,3, "Hello! World", 77}

print("difference()           = ", set_1.difference(set_2,set_3)) 
print("intersection()         = ", my_set.intersection(set_2, set_3))
print("union()                = ", my_set.union(set_2, set_3))
print("symmetric_difference() = ", my_set.symmetric_difference(set_2))
