name = input('Enter your name: ')
print(name)
age = int(input('Enter your age: '))    # convert the input to an integer
print(age)
grade = float(input('Enter your grade: '))   # convert the input to a float
print(grade)

print(type(name))   # type of name is str according to the input function
print(type(age))    # type of age is int because we converted the input to an integer using int()
print(type(grade))  # type of grade is float because we converted the input to a float using float()

name = 4            # reassigning name to an integer
age = 'John'        # reassigning age to a string
grade = [1, 2, 3]   # reassigning grade to a list

print(type(name))   # type of name is change to int
print(type(age))    # type of age is change to str
print(type(grade))  # type of grade is change to list
