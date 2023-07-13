#!/usr/bin/env python
# coding: utf-8

# # Python Input and Output

# # Python Output

# We use the print() function to output data to the standard output device

# In[1]:


print("Hello World")


# In[4]:


a = 10
print("The value of a is", a) #python 3
print "The value of a is " + str(a)


# # Output Formatting

# In[1]:


a = 10; b = 20 #multiple statements in single line.

print("The value of a is {} and b is {}".format(a, b))    #default


# In[5]:


a = 10; b = 20  #multiple statements in single line

print("The value of b is {1} and a is {0}".format(a, b)) #specify position of arguments


# In[6]:


#we can use keyword arguments to format the string
print("Hello {name}, {greeting}".format(name="satish", greeting="Good Morning"))


# In[7]:


#we can combine positional arguments with keyword arguments
print('The story of {0}, {1}, and {other}'.format('Bill', 'Manfred',
                                                       other='Georg'))


# # Python Input

# want to take the input from the user. In Python, we have the input() function to allow this. 

# In[7]:


num = input("Enter a number: ")
print num

