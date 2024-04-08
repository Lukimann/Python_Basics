#Assigning a string a variable name
message = 'Hello, Python!'
print(message)
message
#Length of a string including spaces
mess = 'My name is Elly'
len_of_string = len(mess)
print(len_of_string)

#Concatenating Strings
question = 'Are  you ready?'
answer = 'Yes, I am.'
result = question + answer
print(result)

#Using the format() method to concatenate strings.
name = 'Elly'
age = 25
country = 'USA'
city = 'New York'
print('I am {} and I am {} years old. Live in {}, {}.'.format(name, age, country, city))

#Escape Sequence
question = 'Are  you ready?'
answer = 'Yes, I am.'
print('Are you ready?\nYes, I am.')