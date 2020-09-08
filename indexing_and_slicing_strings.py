greeting_string = "Hello Python!"

# print second 'l' in the Hello word
print(greeting_string[3])

# print second 'l' in the Hello word without variables
print("Hello Python!"[3])

# print 'He' minimum by 2 ways
print(greeting_string[:2])
print(greeting_string[0:2])
print(greeting_string[:2:1])
print(greeting_string[0:2:1])
print(greeting_string[0] + greeting_string[1])
print(greeting_string[-13:-11])
print(greeting_string[-13:-11:1])

# make new string 'Path' from 'Hello Python!' with concatenating missing character
print(greeting_string[6] + 'a' + greeting_string[8:10])
