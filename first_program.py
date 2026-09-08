print("Hello World")

name="Srushti"
print("Hello, " + name)

# For the type of data, we can use the type() function to check the data type of a variable. For example:
print(type(name))

######################################################################################################################
#Input in Python can be taken using the input() function. For example:
age = input("Enter your age: ")
print(type(age))  # This will print <class 'str'> because input() returns a string

# To have it as an integer, we can  convert it using the int() function. For example:
age = int(input("Enter your age: "))

######################################################################################################################

# Conditional statements

light=input("Give light input: ")
if light=="green":
    print("Go") 
elif light=="yellow":
    print("Slow down")  
else:
    print("Stop")

######################################################################################################################

# STRINGS

# Basic operations with strings:
concatenation = "Hello" + " " + "World";
print(concatenation);

len1 = len(concatenation);
print(len1);

# slicing
print(concatenation[1:4])
# negative indexing
print(concatenation[-5:-1])

# String Functions
str="I am studing Python from Apna College"
print(str.endswith("College"))
print(str.capitalize()) #will not change the original string 
print(str.replace("Python", "Java"))
print(str.find("o")) #will return the index of first occurrence of "o"
print(str.count("a")) #will return the count of "a" in the string

#######################################################################################################################

# LIST 

# a built-in data structure in Python that can hold an ordered collection of items, which can be of different types. 
# Lists are mutable, meaning you can change their content without changing their identity.
students = ["Srushti", "Rohit", 65, 78.5, True]
print(students)
students[1] = "Ajinkya"  # Changing the second element
print(students)

# Slicing - same as strings
print(students[1:4])  # This will print elements from index 1 to 3 (4 is not included)
# It also supports negative indexing, so students[-1] will give you the last element of the list.

# List Functions
list=[1, 2, 3, 4, 5]
list.append(6)  # Adds 6 to the end of the list
list.sort()  # Sorts the list in ascending order
list.sort(reverse=True)  # Sorts the list in descending order   
list.reverse()  # Reverses the order of the list
list.insert(2, 10)  # Inserts 10 at index 2
list.remove(3)  # Removes the first occurrence of 3 from the list
list.pop(4)

#######################################################################################################################
# Tuples   They are immutable, meaning once a tuple is created, its elements cannot be changed, added, or removed. Tuples are defined by enclosing the elements in parentheses ().
tuples = (1, 2, 3, 4, 5)
single_element_tuple = (1,)  # Note the comma, which is necessary for single-element tuples
tuples.index(3)  # Returns the index of the first occurrence of 3
tuples.count(2)  # Returns the count of 2 in the tuple

#######################################################################################################################
# Dictionaries   They are mutable, meaning you can change their content without changing their identity. 
# Dictionaries are defined by enclosing the elements in curly braces {} and consist of key-value pairs.
info = {
    "name": "Srushti", 
    "age": 20,
    "city": "Pune",
    "subjects": ["Python", "Java", "C++"]
}

# Nested Dictionary
student={
    "name": "Srushti",
    "age": 20,
    "address": {
        "street": "123 Main St",
        "city": "Pune",
        "state": "Maharashtra"
    },
    "subjects": ["Python", "Java", "C++"]
}
print(student["address"]["city"])  # Accessing nested dictionary value

# Dictionary Functions
student.keys()  # Returns a view object that displays a list of all the keys in the dictionary
student.values()  # Returns a view object that displays a list of all the values in the dictionary
student.items()  # Returns a view object that displays a list of all the key-value pairs in the dictionary
student.get("name")  # Returns the value for the specified key ("Srushti" in this case)
student.update({"age": 21})  # Updates the value of the specified key (age is now 21)

#######################################################################################################################
# SETS
sets = {1, 2, 3, 4, 5}  # Sets are unordered collections of unique elements
sets.add(6)  # Adds 6 to the set
sets.remove(3)  # Removes 3 from the set
sets.discard(10)  # Removes 10 from the set if it exists, otherwise does nothing
sets.clear()  # Removes all elements from the set
sets.pop()  # Removes and returns an arbitrary element from the set
sets.union({4, 5, 6})  # Returns a new set with elements from both sets
sets.intersection({4, 5, 6})  # Returns a new set with elements common to both sets

#######################################################################################################################

# Functions in Python are defined using the def keyword, followed by the function name and parentheses. Functions can take parameters and return values. Here's an example of a simple function:
def cal_sum(a, b):
    sum= a + b
    print(sum)
    return sum
cal_sum(5, 10)  # This will print 15 and return 15

# Recursion is a programming technique where a function calls itself in order to solve a problem. It is often used to solve problems that can be broken down into smaller, similar subproblems. Here's an example of a recursive function that calculates the factorial of a number:
def show(n):
    if n==0:
        return 
    print(n)
    show(n-1)
show(5)  # This will print 5, 4, 3, 2, 1

#######################################################################################################################

# File Handling in Python can be done using the built-in open() function, which allows you to read from and write to files.
f=open("test.txt", "r")  # Opens a file named "test.txt" in read mode
f=open("test.txt", "w")  # Opens a file named "test.txt" in write mode
print(f.read())  # Reads and prints the contents of the file
f.close()  # Closes the file

# File Characters:
# r - Read mode, which is used to read the contents of a file. If the file does not exist, it will raise an error.
# w - Write mode, which is used to write data to a file. If the file already exists, it will overwrite the existing content. If the file does not exist, it will create a new file.
# a - Append mode, which is used to add data to the end of a file.  
# x - Exclusive creation mode, which is used to create a new file. If the file already exists, it will raise an error.
# b - Binary mode, which is used to read or write binary files (e.g., images, audio files). It can be combined with other modes (e.g., rb for reading a binary file).
# t - Text mode, which is the default mode for reading and writing text files. It can be combined with other modes (e.g., rt for reading a text file).
# + - Update mode, which allows you to read and write to a file. It can be combined with other modes (e.g., r+ for reading and writing to a file).

# for binary file
f=open("test.txt", "rb")  # Opens a file named "test.txt" in binary read mode

# file.read(5)  # Reads the first 5 bytes of the file
# file. readline()  # Reads the next line of the file

#######################################################################################################################

# OOPS
# Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. In Python, classes are defined using the class keyword, followed by the class name and a colon. Here's an example of a simple class:
# Object is an instance of a class. It is created using the class constructor and can have its own unique attributes and methods. In Python, objects are created by calling the class name as if it were a function. 
class Student:
    def __init__(self, name):
        print("adding new student in DB...")
        self.name = name  # This is an attribute of the Student class

s1=Student("Srushti")  # Creating an object of the Student class
print(s1.name)  # Accessing the name attribute of the s1 object

# Abstraction is a programming concept that allows you to hide the implementation details of a class and expose only the necessary functionality. In Python, abstraction can be achieved using abstract classes and methods. An abstract class is a class that cannot be instantiated and is meant to be subclassed. An abstract method is a method that is declared in an abstract class but does not have an implementation. Subclasses of the abstract class must provide an implementation for the abstract methods.
# Encapsulation is a programming concept that restricts access to the internal state and behavior of an object. In Python, encapsulation can be achieved using private attributes and methods. Private attributes and methods are defined by prefixing their names with a double underscore (__). This makes them inaccessible from outside the class, providing a way to protect the internal state of the object.
# inheritance is a programming concept that allows a class to inherit attributes and methods from another class. In Python, inheritance is achieved by defining a subclass that extends a superclass. The subclass inherits all the attributes and methods of the superclass and can also have its own unique attributes and methods. This allows for code reuse and the creation of more specialized classes based on existing ones.
# Polymorphism is a programming concept that allows objects of different classes to be treated as objects of a common superclass. In Python, polymorphism can be achieved through method overriding and operator overloading. Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. Operator overloading allows you to define how operators (like +, -, *, etc.) behave for objects of your class, enabling you to use them in a way that is intuitive for your specific class.

#######################################################################################################################

# Exception Handling
# try: we write the suspicious code here
# except: we write the code to handle the exception here
# finally: we write the code that will always be executed here, regardless of whether an exception occurred or not

try:
    a=int(input("Enter a number: "))
    b=7/a
    print(b)
except Exception as e:
    print("Error: ", e)

# Exception is a super class which has all errors classes in it like valueerror, type error, zero division error etc.

# We can also just use ValueError class to handle only value errors. For example:
try:
    a=int(input("Enter a number: "))
    b=7/a
    print(b)
except ValueError as e:
    print("Error: ", e)
# Above code will only handle value errors, and if any other type of exception occurs, it will not be caught by this except block.
# We can have multiple except blocks to handle different types of exceptions. For example:
try:
    a=int(input("Enter a number: "))
    b=7/a
    print(b)
except ValueError as e:
    print("Error: ", e)
except ZeroDivisionError as e:
    print("Error: ", e)




