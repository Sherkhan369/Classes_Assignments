#The Frozenset
#In Python, a frozenset is an immutable (unchangeable) version of a set. It is a collection of unique elements, just like a set, but it cannot be modified after it is created.

frozenset_1: frozenset = frozenset([1,2,3, "Hello! World"])
print("frozenset 1  = ", frozenset_1)

my_set: set = {1,2,3, "Hello! World"}
frozenset_2: frozenset = frozenset(my_set)
print("my_frozenset2 = ", frozenset_2)


#frozensets Methods:

frozen_set1: frozenset = frozenset([1, 2, 3, 4])
frozen_set2: frozenset = frozenset([3, 4, 5, 6])
frozen_set3: frozenset = frozenset([1, 2])

print(f"frozen_set1: {frozen_set1}")
print(f"frozen_set2: {frozen_set2}")
print(f"frozen_set3: {frozen_set3}")

print("difference()           = ", frozen_set1.difference(frozen_set2, frozen_set3))
print("intersection()         = ", frozen_set1.intersection(frozen_set2, frozen_set3))
print("union()                = ", frozen_set1.union(frozen_set2, frozen_set3))
print("symmetric_difference() = ", frozen_set1.symmetric_difference(frozen_set2))