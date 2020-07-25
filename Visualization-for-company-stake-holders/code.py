# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Code starts here

# Step 1 
#Reading the file
data=pd.read_csv(path)



#Creating a new variable to store the value counts
#print(data.head(4))
loan_status=data['Loan_Status'].value_counts()


#Plotting bar plot
loan_status.plot(kind='bar')


# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()

#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot

education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()



#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'
graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind='density',label='Not Graduate')
#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(20,10))

#Plotting scatter plot
data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)

data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)
ax_1.set_title('Applicant Income')
ax_2.set_title('Coapplicant Income')
ax_3.set_title('Total Income')
# Display plot

#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



