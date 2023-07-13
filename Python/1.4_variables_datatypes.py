#!/usr/bin/env python
# coding: utf-8

# # Variables

# A variable is a location in memory used to store some data (value).
# 
# They are given unique names to differentiate between different memory locations. The rules for writing a variable name is same as the rules for writing identifiers in Python.
# 
# We don't need to declare a variable before using it. In Python, we simply assign a value to a variable and it will exist. We don't even have to declare the type of the variable. This is handled internally according to the type of value we assign to the variable.

# # Variable Assignments

# In[ ]:


#We use the assignment operator (=) to assign values to a variable

a = 10
b = 5.5
c = "ML"


# # Multiple Assignments

# In[ ]:


a, b, c = 10, 5.5, "ML"


# In[ ]:


a = b = c = "AI" #assign the same value to multiple variables at once


# # Storage Locations

# In[ ]:


x = 3

print(id(x))               #print address of variable x


# In[ ]:


y = 3

print(id(y))               #print address of variable y


# Observation:
# 
# x and y points to same memory location
#     

# In[ ]:


y = 2
print(id(y))               #print address of variable y


# # Data Types 

# Every value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

# # Numbers

# Integers, floating point numbers and complex numbers falls under Python numbers category. They are defined as int, float and complex class in Python.
# 
# We can use the type() function to know which class a variable or a value belongs to and the isinstance() function to check if an object belongs to a particular class.

# In[ ]:


a = 5                               #data type is implicitly set to integer
print(a, " is of type", type(a))


# In[ ]:


a = 2.5                            #data type is changed to float
print(a, " is of type", type(a))


# In[ ]:


a = 1 + 2j                          #data type is changed to complex number
print(a, " is complex number?") 
print(isinstance(1+2j, complex))


# # Boolean

#  Boolean represents the truth values False and True

# In[ ]:


a = True                          #a is a boolean type
print(type(a))


# # Python Strings

# String is sequence of Unicode characters. 
# 
# We can use single quotes or double quotes to represent strings. 
# 
# Multi-line strings can be denoted using triple quotes, ''' or """.

# A string in Python consists of a series or sequence of characters - letters, numbers, and special characters. 
# 
# Strings can be indexed - often synonymously called subscripted as well. 
# 
# Similar to C, the first character of a string has the index 0.

# In[ ]:


s = "This is Online AI course"
print(s)


# In[ ]:


print(s[0])
#last char s[len(s)-1] or s[-1]


# In[ ]:


#slicing
s[5:]


# # Python List

# List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.
# 
# Declaring a list is , Items separated by commas are enclosed within brackets [ ].

# In[ ]:


a = [10, 20.5, "Hello"]
print(a[1])               #print 1st index element


# Lists are mutable, meaning, value of elements of a list can be altered.

# In[ ]:


a[1] = 30.7
print(a)


# # Python Tuple

# Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. Tuples once created cannot be modified.

# In[ ]:


t = (1, 1.5, "ML")


# In[ ]:


print(t[1]) #extract particular element


# In[ ]:


t[1] = 1.25


# # Python Set

# Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

# In[ ]:


a = {10, 30, 20, 40, 5}
print(a)


# In[ ]:


print(type(a))             #print type of a


# We can perform set operations like union, intersection on two sets. Set have unique values.

# In[ ]:


s = {10, 20, 20, 30, 30, 30}
print(s)                    #automatically set won't consider duplicate elements


# In[ ]:


print(s[1]) #we can't print particular element in set because 
            #it's unorder collections of items


# # Python Dictionary

# Dictionary is an unordered collection of key-value pairs.

# In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.

# In[ ]:


d = {'a': "apple", 'b': "bat"}
print d['a']


# # Conversion between Datatypes

# We can convert between different data types by using different type conversion functions like int(), float(), str() etc.

# In[ ]:


float(5)     #convert interger to float using float() method


# In[ ]:


int(100.5)   #convert float to integer using int() method


# In[ ]:


str(20)      #convert integer to string


# Conversion to and from string must contain compatible values.

# In[ ]:


int('10p')


# In[ ]:


user = "satish"
lines = 100

print("Congratulations, " + user + "! You just wrote " + str(lines) + " lines of code" )
#remove str and gives error


# We can convert one sequence to other

# In[ ]:


a = [1, 2, 3]

print(type(a))      #type of a is list 

s = set(a)          #convert list to set using set() method

print(type(s))      #now type of s is set


# In[ ]:


list("Hello")       #convert String to list using list() method

