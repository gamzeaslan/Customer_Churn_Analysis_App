#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


data=pd.read_csv("Module Data.csv")
data=data.drop(["Unnamed: 0","Geography"],axis=1)
data.head()


# In[3]:


#CreditScore 
def credit_score(score):
    score = int(score)
    if score >= 300 and score < 500:
        return (2.0)
    
    elif score >= 500 and score < 601:
        return (3.0)
    
    elif score >= 601 and score < 661:
        return (4.0)
    
    elif score >= 661 and score < 781:
        return (5.0)
    
    elif score >= 851:
        return (7.0)
    
    elif score >= 781 and score < 851:
        return (6.0)
    
    elif score< 300:
        return (1.0)


# In[4]:


#Age
def Age(age):
    age= int(age)
    if age >= 18 and  age <= 30:
        return (1.0)
    
    elif age > 30 and  age <= 40:
        return (2.0)
    
    elif age > 40  and  age <= 50:
        return (3.0)
    
    elif age > 50 and  age <= 60:
        return (4.0)
    
    elif age > 60 and  age <= 92:
        return (5.0)
    



#HasCrCard,IsActiveMember
def Question(answer):
    if(answer.upper() == "yes"):
        return (1.0)
    elif(answer.upper() == "no"):
        return (0.0)


# In[7]:


def Geography_Germany(geography):
    if(geography.upper() == "france"):
        return (0.0 )
    
    elif(geography.upper() == "germany"):
        return (1.0 )
    
    elif(geography.upper() == "spain"):
        return (0.0 )
    
def Geography_Spain(geography):
    if(geography.upper() == "france"):
        return (0.0)
    
    elif(geography.upper() == "germany"):
        return (0.0 )
    
    elif(geography.upper() == "spain"):
        return (1.0 )

# In[8]:


def Gender(gender):
    if(gender.upper == "male"):
        return (1.0)
    elif(gender.upper == "female"):
        return (0.0)


# In[9]:


def  retirement(Age,Geography_Germany,Geography_Spain):
    if(Age >= 65 and Geography_Germany == 1.0):
        return (1.0)
    
    elif(Age>= 65 and Geography_Spain== 1.0):
        return (1.0)
    
    elif(Age>= 66 and  Geography_Spain == 0.0 and  Geography_Germany == 0.0):
        return (1.0)
    
    elif(Age < 65 and  Geography_Germany == 1.0):
        return (0.0)
    
    elif(Age < 65 and  Geography_Spain == 1.0):
        return (0.0)
    
    elif(Age < 65 and Geography_Spain == 0.0 and  Geography_Germany == 0.0):
        return (0.0)


# In[ ]:




