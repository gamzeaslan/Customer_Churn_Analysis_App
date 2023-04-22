#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import joblib
import Module
import streamlit as st


# In[2]:


loaded_model = joblib.load(open("model.joblib","rb"))


# In[3]:


def churn_prediction(input_data):
    input_data_as_narray = np.asarray(input_data)
    input_data_reshape = input_data_as_narray.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    if (prediction[0] == 0) :
        return 'not churn 😊'
    else:
        return 'churn 😢 '


# In[4]:


def main():
    st.title("Churn  Prediction")
    
    CreditScore=Module.credit_score(st.number_input("Credit Score (Customer's credit score)", min_value=0, max_value=1000, value=400, step=50))
    Age = Module.Age(st.number_input('Age', min_value=18, max_value=100, value=30, step=1))
    Tenure =st.number_input('Tenure (Time of working with the customer bank /in years) ', min_value=1, max_value=20, value=5 ,step=1)
    Balance =st.number_input("Balance (Balance in the customer's account) ", min_value=1, max_value=300000, value=50000 ,step=1000)
    NumOfProducts =st.number_input('Num Of Products (Number of products used by the customer from the bank) ', min_value=0, max_value=10, value=5 ,step=1)
    EstimatedSalary = st.number_input('Salary / years', min_value=0, max_value=300000, value=100000 ,step=1000)
    
    
    
    card_selection=["Yes","No"]
    
    HasCrCard =Module.Question(st.selectbox('Has Cr Card', card_selection))
    
    IsActiveMember =Module.Question(st.selectbox('Is Active Member', card_selection))
    
    
    
    
    
    geo_selection=["France","Germany","Spain"]
    
    geo=st.selectbox("Geography (Customer's country of residence)", geo_selection)
    
    Geography_Germany=Module.Geography_Germany(geo)
    
    Geography_Spain=Module.Geography_Spain(geo)
    
    
    
    
    gender_selection=["Male","Female"]
    
    Gender =Module.Gender(st.selectbox('Gender', gender_selection))
    
    
    
    
    Retirement =Module.retirement(Age,Geography_Germany,Geography_Spain)

    EstimatedSalary_Age = EstimatedSalary / Age
    
    CreditScore_Age = CreditScore / Age
    
    NumOfProducts_Tenure = NumOfProducts / Tenure
    
    EstimatedSalary_CreditScore = EstimatedSalary/ CreditScore
    
    EstimatedSalary_Balance = EstimatedSalary/ Balance
    
    EstimatedSalary_Tenure = EstimatedSalary/ Tenure
    
    EstimatedSalary_NumOfProducts = EstimatedSalary/ NumOfProducts
    
    CreditScore_Tenure = CreditScore / Tenure

    diagnosis = ""
    
    
    
    
    if st.button("Churn Prediction Result"):
        diagnosis = churn_prediction([CreditScore, Age, Tenure,Balance, NumOfProducts , HasCrCard,IsActiveMember,
                                        EstimatedSalary,EstimatedSalary,EstimatedSalary,Gender,Retirement ,
                                        EstimatedSalary_Age,CreditScore_Age ,NumOfProducts_Tenure,
                                        EstimatedSalary_CreditScore,EstimatedSalary_Balance,EstimatedSalary_Balance,
                                        EstimatedSalary_NumOfProducts,CreditScore_Tenure])
        
        
        
    st.success(diagnosis)


# In[5]:


if __name__ == '__main__':
    main() 


# In[ ]:




