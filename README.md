# Churn Analysis (Churn analysis summary information)
* Churn analysis is an analysis method used to determine the churn rate of a business and understand its causes. It is often used in industries such as subscription-based services, telecommunications, banking, and retail.
* Churn analysis calculates the rate at which existing customers abandon the business over a given period (usually one year). This analysis is used to understand the reasons for customer churn and why customers leave the business. This knowledge helps businesses develop strategies to increase customer loyalty.
* Methods used for Churn analysis may include analysis of data on customer behavior, customer satisfaction surveys, customer feedback, and use of customer relationship management data



***********************************************************

# Project Overview
* Purpose of the project I did: I developed a model with XGBoost by performing churn analysis so that banks can predict whether their customers will abandon them. And the accuracy score value of the model I developed is 0.90.
* The variables in the dataset I used for the project are as follows:
  * CreditScore-->Customer's credit score
	* Geography-->Customer's country of residence
	* Gender-->Gender of the customer 
	* Age-->Customer's Age
	* Tenure-->Time of working with the customer bank (in years)
	* Balance-->Balance in the customer's account
	* NumOfProducts--->Number of products used by the customer from the bank
	* HasCrCard--> Whether the customer has a credit card
	* IsActiveMember--> Whether the customer is an active customer of the bank (0: not, 1: yes)
	* EstimatedSalary-->Client's estimated salary
	* Exited--> Whether the customer has left the bank (0: no, 1: yes)
* Built a client facing API using streamlit

# Code and Resources Used:
* **Python Version** : 3.10.9
* * **Packages** : matplotlib ,seaborn,pandas , imblearn,sklearn , joblib , lightgbm, xgboost and lazypredict

# Data Cleaning
* I removed the following columns that I thought were unnecessary: "RowNumber","CustomerId","Surname"
* I used get_dummies function for categorical variables
* I used a pie chart to visualize the churn and non-churn data proportions in the dataset.
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/pie_before.png "Pie Before")
* Since there is an 80 - 20 ratio among the data, I will produce synthetic data with SMOTEC to eliminate this skewed distribution.
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/pie_after.png "Pie After")
* I created a retirement column based on the retirement ages of the countries
* I grouped the Age and CreditScore values
* I created new variables. The new variables are:
  * EstimatedSalary / Age
  * CreditScore / Age
  * NumOfProducts / Tenure
  * EstimatedSalary / CreditScore
  * EstimatedSalary / Balance
  * EstimatedSalary / Tenure
  * EstimatedSalary / NumOfProducts
  * CreditScore / Tenure


* I had the boxplot plot drawn to detect outliers in the variables.
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/boxplot.png "Boxplot")
* I applied the ROBUSTSCALER operation for variables with outliers.

# EDA 
* I used a pie chart to visualize the percentages of bank customers' genders
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/gender_pie.png "Gender Pie")

* I had a pie chart drawn to get information about the age distribution of the customers in the bank.
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/age_pie.png "Age Pie")

* I had a pie chart drawn to get information about the credit scores of the customers in the bank.
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/creditscore_pie.png "Credit Score Pie")

* I used a pie chart to see what percentage of customers at the bank have credit cards
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/hascrcard_pie.png "Has Cr Card Pie")


* I used a pie chart to visualize the percentages of customers in the bank by country
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/geo_pie.png "Geography Pie")


* I calculated the number of churns of women and men in countries with the Groupby method.
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/groupby_1.png "GroupBy_1")

* I use groupby to calculate which age women and men are the most churn 
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/groupby_2.png "GroupBy_2")

# Model Building 
* I used the lazypredict library to find the model with the highest success in the shortest time
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/models.png "Models")

* I used the XGBoost algorithm in line with the graphic above.
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/class_report.png "Classification Report")

# APP
* Since it performs many operations through the parameters entered during the application, I created a file called Module.py that contains all the methods that perform these operations. And this library is imported into the app application, and the entered data is processed to be converted into a format suitable for the model
* 
![alt text](https://github.com/gamzeaslan/Customer_Churn_Analysis_App/blob/main/app.png "App")





