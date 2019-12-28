#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


ar = np.arange(0,11)


# In[3]:


ar


# # Selecting Elements from an Array

# ##### variablename[start:stop:stepcount]

# In[4]:


#selecting elements from index 0 to 5
ar[0:5]


# In[7]:


#selecting elements from where the index starts to 6
ar[:6]


# In[8]:


#Selecting elements from index 5 to where the array ends
ar[5:]


# In[18]:


#copying an array
ar_copy = ar.copy()
ar1_copy = ar.copy()


# In[10]:


ar_copy


# In[12]:


slice_of_ar = ar_copy[0:11:2]


# In[13]:


slice_of_ar


# In[14]:


ar_copy


# ##### Broadcasting a number to an array

# In[15]:


#broadcasting 1216 to the array slice_of_ar
slice_of_ar[:] = 1216


# In[16]:


slice_of_ar


# In[17]:


ar_copy


# In[19]:


slice_of_ar1 = ar1_copy[0:11:2]


# In[20]:


#broadcasting 3650 to the slice_of_ar1 with the step count of 2 on the array
slice_of_ar1 [0:6:2] = 3650


# In[21]:


slice_of_ar1


# #### Indexing and selection on 2D arrays

# In[22]:


ar_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[23]:


ar_2d


# ###### Selecting elements from the 2D array

# In[24]:


ar_2d [0]


# In[25]:


#selection using double brackets 
ar_2d [0][0]


# In[30]:


ar_2d[0,0]


# In[29]:


ar_2d [2][2]


# In[33]:


#selection using single brackets and a comma
ar_2d [1,2]


# In[47]:


#slicing 2D array
ar_2d [1:3,1:]


# In[52]:


ar_2d [1:3,0:2]


# In[53]:


ar_1d = np.arange(1,11)


# ##### Conditional Selection

# In[54]:


ar_1d


# In[56]:


bool_ar = ar_1d < 6


# In[57]:


bool_ar


# In[59]:


ar_1d[bool_ar]#it will get only those values that are true in bool_ar


# In[60]:


#another way to do conditional selection is:
ar_1d[ar_1d <6]


# ## Practise 

# In[62]:


prac_ar = np.arange(50).reshape(5,10)


# In[63]:


prac_ar


# In[64]:


prac_ar [2:4,6:8]


# In[65]:


prac_ar [2:,0:2]


# In[66]:


prac_ar [3:,3:5]


# In[67]:


prac_ar [2:,6:]


# In[ ]:




