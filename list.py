var1 = [1, "me", 2, 3]
print(var1)
print(type(var1))

# inserting into list
var1.insert(0, "monday ")
print(var1)

# inserting into the end of the list
var1.append("monday")
print(var1)

# Adding a list to another list
weekends = ["saturday", "sunday"]
var1.extend(weekends)
print(var1)

# Removing elements from a list
var1.remove("monday")
print (var1)

# to remove element from the list using index
var1.pop(1)
print(var1)
# to delete anything use the del function
# sorting elements in a list
print(f'unsorted: {var1}\n')
# sorting elements in a list
age = [20, 23, 34, 32, 74, 17, 21]
print(f'{age}')
age.sort()
print(f'{age}')
age.sort(reverse=True)
print(f'{age}')



