# Build this list [0,0,0] two separate ways.

# Method 1:
list1 = []
list1.append(0)
list1.append(0)
list1.append(0)
print(list1)

# Method 2:
list2 = [0]*3
print(list2)

# Method 3:
list2 = [0,0,0]
print(list2)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Sort the list below:

list4 = [5,3,4,6,1]
list4.sort()
print(list4)


