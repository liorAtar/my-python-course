# with open("myfile.txt") as my_new_file:
#     contents = my_new_file.read()
#     print(contents)

# with open("myfile.txt", mode='r') as my_new_file:
#     contents = my_new_file.read()
#     print(contents)

# with open("myfile.txt", mode='a') as my_new_file:
#     my_new_file.write('\nthis is the forth line')

# with open("myfile.txt", mode='r') as my_new_file:
#     contents = my_new_file.read()
#     print(contents)

# with open("newfile.txt", mode='w') as new_file:
#     new_file.write('I created this file')

# with open("newfile.txt", mode='r') as new_file:
#     contents = new_file.read()
#     print(contents)

file = open('test.txt', 'w')
file.write('Hello World')
file.close()


