#!/usr/bin/env python
# coding: utf-8

# # Python Keywords

# Keywords are the reserved words in python
# 
# We can't use a keyword as variable name, function name or any other identifier
# 
# Keywords are case sentive

# In[2]:


#Get all keywords in python 3.6

import keyword

print(keyword.kwlist)

print("Total number of keywords ", len(keyword.kwlist))


# # Identifiers

# Identifier is the name given to entities like class, functions, variables etc. in Python. It helps differentiating one entity from another.

# Rules for Writing Identifiers:
# 
# 1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
# 
# 2. An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
# 
# 3. Keywords cannot be used as identifiers.

# In[3]:


global = 1


#  We cannot use special symbols like !, @, #, $, % etc. in our identifier.

# In[5]:


a@ = 10             #can't use special symbols as an identifier

