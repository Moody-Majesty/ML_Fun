#!/usr/bin/env python
# coding: utf-8

# # Python if ... else Statement

# The **if…elif…else** statement is used in Python for decision making.

# # if statement syntax

#     if test expression:
# 
#         statement(s)

# The program evaluates the test expression and will execute statement(s) only if the text expression is True.
# 
# If the text expression is False, the statement(s) is not executed.

# Python interprets non-zero values as True. None and 0 are interpreted as False.

# # Flow Chart

# ![title](Python_if_statement.jpg)

# # Example

# In[ ]:


num = 10

# try 0, -1 and None
if None:
    print("Number is positive")
print("This will print always")      #This print statement always print

#change number 


# # if ... else Statement

# # Syntax:

#     if test expression:
#     
#         Body of if
# 
#     else: 
#     
#         Body of else

# # Flow Chart

# ![title](Python_if_else_statement.jpg)

# # Example

# In[ ]:


num = 10
if num > 0:
    print("Positive number")
else:
    print("Negative Number")


# # if...elif...else Statement

# # Syntax:

#     if test expression:
# 
#         Body of if
#     elif test expression:
#     
#         Body of elif
#     else: 
#     
#         Body of else

# # Flow Chart

# ![title](Python_if_elif_else_statement.jpg)

# # Example:

# In[ ]:


num = 0

if num > 0:
    print("Positive number")
elif num == 0:
    print("ZERO")
else:
    print("Negative Number")


# # Nested if Statements

# We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming.

# # Example:

# In[ ]:


num = 10.5

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative Number")


# # Python program to find the largest element among three Numbers

# In[ ]:


num1 = 10
num2 = 50
num3 = 15

if (num1 >= num2) and (num1 >= num3):           #logical operator   and
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("Largest element among three numbers is: {}".format(largest))


# In[ ]:




