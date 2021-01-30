#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(type("hello"))


# In[2]:


print(int("55") + int("66"))


# In[4]:


int("55")


# In[5]:


str("33")


# In[8]:


float(33)


# In[13]:


print(10 * str(int(44+5)))


# In[ ]:





# In[14]:


print("Enter your numnber")
inp = input()  #number we enter will be stored as a string 
print("You have entered", inp)
#print("You have entered", inp + 10)      this gives error
#print("You have entered", int(inp) + 10)      this does not gives error


# In[ ]:





# In[23]:


#STRING
a="hello I am Tushar"
a[1]s/a


# In[24]:


a[-1]


# In[25]:


a[1:]


# In[26]:


a[1:100]


# In[27]:


#a[100] This gives error out of index error


# In[28]:


a[::2] #prints alternate character


# In[30]:


a[::3]#skips 2 characters


# In[31]:


a[::33]# resolves the maximum it can


# In[36]:


print(a[-4:-2])
print(a[13:15])


# In[37]:


a[::-2]#reverses the string and then skips 1 character


# In[38]:


type(a)


# In[41]:


a.isalnum()
#Returs false since it is not an alpha numeric string as it has spaces


# In[43]:


a.isalpha()
#Returns false as it is neither alpha nor numeric


# In[44]:


a.endswith("h")


# In[46]:


a.capitalize()
#capatalizes the first character


# In[52]:


a.find("am")


# In[54]:


#If find is able to find the index, it returns the positive value of the index
#If it is not able to find the index, it returns -1
a.find("there")


# In[55]:


a.lower()


# In[56]:


a.upper()


# In[58]:


a.replace("Tushar", "Tushar Kaushik")


# In[59]:


a


# In[ ]:




