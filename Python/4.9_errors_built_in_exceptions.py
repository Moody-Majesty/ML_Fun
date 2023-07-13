#!/usr/bin/env python
# coding: utf-8

# # Python Errors and Built-in-Exceptions

# When writing a program, we, more often than not, will encounter errors.
# 
# Error caused by not following the proper structure (syntax) of the language is called syntax error or parsing error.

# In[ ]:


if a < 3


# Errors can also occur at runtime and these are called exceptions. 
# 
# They occur, for example, when a file we try to open does not exist (FileNotFoundError), dividing a number by zero (ZeroDivisionError), module we try to import is not found (ImportError) etc.

# Whenever these type of runtime error occur, Python creates an exception object. If not handled properly, it prints a traceback to that error along with some details about why that error occurred.

# In[ ]:


1 / 0


# In[ ]:


open('test.txt')


# # Python Built-in Exceptions

# In[ ]:


dir(__builtins__)


# # Python Exception Handling - Try, Except and Finally

# Python has many built-in exceptions which forces your program to output an error when something in it goes wrong.
# 
# When these exceptions occur, it causes the current process to stop and passes it to the calling process until it is handled. If not handled, our program will crash.
# 
# For example, if function A calls function B which in turn calls function C and an exception occurs in function C. If it is not handled in C, the exception passes to B and then to A.
# 
# If never handled, an error message is spit out and our program come to a sudden, unexpected halt.

# # Catching Exceptions in Python

# In Python, exceptions can be handled using a try statement.
# 
# A critical operation which can raise exception is placed inside the try clause and the code that handles exception is written in except clause.

# In[ ]:


# import module sys to get the type of exception
import sys

lst = ['b', 0, 2]

for entry in lst:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
    except:
        print("Oops!", sys.exc_info()[0],"occured.")
        print("Next entry.")
        print("***************************")
print("The reciprocal of", entry, "is", r)


# # Catching Specific Exceptions in Python

# In the above example, we did not mention any exception in the except clause.
# 
# This is not a good programming practice as it will catch all exceptions and handle every case in the same way. We can specify which exceptions an except clause will catch.
# 
# A try clause can have any number of except clause to handle them differently but only one will be executed in case an exception occurs.

# In[ ]:


import sys

lst = ['b', 0, 2]

for entry in lst:
    try:
        print("****************************")
        print("The entry is", entry)
        r = 1 / int(entry)
    except(ValueError):
        print("This is a ValueError.")
    except(ZeroDivisionError):
        print("This is a ZeroError.")
    except:
        print("Some other error")
print("The reciprocal of", entry, "is", r)


# # Raising Exceptions

# In Python programming, exceptions are raised when corresponding errors occur at run time, but we can forcefully raise it using the keyword raise.
# 
# We can also optionally pass in value to the exception to clarify why that exception was raised.

# In[ ]:


raise KeyboardInterrupt


# In[ ]:


raise MemoryError("This is memory Error")


# In[ ]:


try:
    num = int(input("Enter a positive integer:"))
    if num <= 0:
        raise ValueError("Error:Entered negative number")
except ValueError as e:
    print(e)


# # try ... finally

# The try statement in Python can have an optional finally clause. This clause is executed no matter what, and is generally used to release external resources.

# In[ ]:


try:
    f = open('sample.txt')
    #perform file operations
    
finally:
    f.close()

