# learning sets
# used to store collection of variables
var1 = {"monday", "tuesday", "wednesday"}
var2 = {1, 1, 2, 2}
print(var2)
# this only prints unique elements when an element is repeated it brings out one.
var3 = set((2, 2, 2, 9, 1, 8, 8, 8))
print(var3)
# adding elements into a set
var1.add("5")
print(var1)

# updating sets with other sequence eg list, tuples
var1.update(["saturday", "sunday"])

# removing elements from a set
var1.discard("saturday")
print(var1)
# you can either use discard or remove but remove will throw an error when an element that isnt in the set is written
